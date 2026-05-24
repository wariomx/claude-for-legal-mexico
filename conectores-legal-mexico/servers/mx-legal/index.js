#!/usr/bin/env node
'use strict';

// MXLegal MCP Server — Sentencias públicas del Poder Judicial de Jalisco (STJJ)
// Verificado 2026-05-23: REST JSON, 82 572 sentencias, sin auth requerida.
// Sin dependencias externas — usa solo módulos nativos de Node.js.

const https = require('https');
const readline = require('readline');

const STJJ_BASE = 'https://publica-sentencias-backend.stjjalisco.gob.mx';

// 0.5 req/s (burst 2)
let stjjLastCall = 0;
async function rateLimit() {
  const wait = 2100 - (Date.now() - stjjLastCall);
  if (wait > 0) await new Promise(r => setTimeout(r, wait));
  stjjLastCall = Date.now();
}

function log(msg) {
  process.stderr.write(`[mx-legal-mcp] ${msg}\n`);
}

function httpRequest(url, options = {}) {
  return new Promise((resolve, reject) => {
    const urlObj = new URL(url);
    const reqOptions = {
      hostname: urlObj.hostname,
      path: urlObj.pathname + urlObj.search,
      method: options.method || 'GET',
      headers: {
        'User-Agent': 'MXLegalMCP/1.0 (conectores-legal-mexico; +https://soft.law)',
        Accept: 'application/json',
        ...(options.headers || {}),
      },
      timeout: 30000,
    };

    const req = https.request(reqOptions, (res) => {
      let raw = '';
      res.on('data', chunk => { raw += chunk; });
      res.on('end', () => {
        let data;
        try { data = JSON.parse(raw); } catch { data = raw; }
        resolve({ status: res.statusCode, data, headers: res.headers });
      });
    });
    req.on('error', reject);
    req.on('timeout', () => req.destroy(new Error('Request timeout after 30s')));
    req.end();
  });
}

const TOOLS = [
  {
    name: 'search_stjj',
    description:
      'Lista sentencias públicas del Supremo Tribunal de Justicia de Jalisco (STJJ). ' +
      '82 572 decisiones, paginación de 15 por página (5 505 páginas en total). ' +
      'Cada toca incluye: id, numero, fecha_publicacion, fecha_emision, materia_data, ' +
      'tipo_juicio_data, sentido_data, magistrado_data, url_resumen_ia. ' +
      'Usar el id con get_stjj_summary (texto del resumen IA) o get_stjj_download_url (URL de descarga PDF).',
    inputSchema: {
      type: 'object',
      properties: {
        page: {
          type: 'number',
          description: 'Página de resultados (1–5505, default 1)',
        },
      },
      required: [],
    },
    async call({ page = 1 }) {
      await rateLimit();
      const res = await httpRequest(`${STJJ_BASE}/tocas?page=${page}`);
      if (res.status !== 200) throw new Error(`STJJ HTTP ${res.status}`);
      return res.data;
    },
  },
  {
    name: 'get_stjj_summary',
    description:
      'Obtiene el texto del resumen ejecutivo generado por IA de una sentencia del STJJ. ' +
      'ESTE ES EL CONTENIDO DE TEXTO DISPONIBLE — el documento completo solo existe en PDF. ' +
      'Usar esta herramienta para leer y analizar el contenido de la sentencia. ' +
      'Típicamente ~1-3 KB de texto plano. ' +
      'Llamar get_stjj_download_url si el usuario necesita el PDF original para descarga manual.',
    inputSchema: {
      type: 'object',
      properties: {
        id: { type: 'number', description: 'ID numérico de la toca (campo "id" en search_stjj)' },
      },
      required: ['id'],
    },
    async call({ id }) {
      await rateLimit();
      const res = await httpRequest(`${STJJ_BASE}/toca/${id}/file_resumen`);
      if (res.status !== 200) throw new Error(`STJJ summary HTTP ${res.status} para id ${id}`);
      return { id, text: res.data };
    },
  },
  {
    name: 'get_stjj_download_url',
    description:
      'Devuelve la URL de descarga directa del PDF de una sentencia del STJJ. ' +
      'NO descarga ni lee el PDF — solo provee la URL para descarga manual. ' +
      'El documento completo solo está disponible en PDF; para leer el contenido usar get_stjj_summary.',
    inputSchema: {
      type: 'object',
      properties: {
        id: { type: 'number', description: 'ID numérico de la toca (campo "id" en search_stjj)' },
      },
      required: ['id'],
    },
    async call({ id }) {
      return {
        id,
        download_url: `${STJJ_BASE}/toca/${id}/file`,
        note: 'PDF — descarga manual. Para leer el contenido usar get_stjj_summary.',
      };
    },
  },
];

const TOOL_MAP = Object.fromEntries(TOOLS.map(t => [t.name, t]));

const rl = readline.createInterface({ input: process.stdin, terminal: false });

function send(obj) {
  process.stdout.write(JSON.stringify(obj) + '\n');
}

function sendError(id, code, message) {
  send({ jsonrpc: '2.0', id, error: { code, message } });
}

rl.on('line', async (line) => {
  const trimmed = line.trim();
  if (!trimmed) return;

  let msg;
  try { msg = JSON.parse(trimmed); } catch (err) {
    log(`JSON parse error: ${err.message}`);
    return;
  }

  const { id, method, params } = msg;

  try {
    if (method === 'initialize') {
      send({
        jsonrpc: '2.0', id,
        result: {
          protocolVersion: '2024-11-05',
          capabilities: { tools: {} },
          serverInfo: { name: 'mx-legal', version: '1.0.0' },
        },
      });
    } else if (method === 'notifications/initialized') {
      // no response
    } else if (method === 'ping') {
      send({ jsonrpc: '2.0', id, result: {} });
    } else if (method === 'tools/list') {
      send({
        jsonrpc: '2.0', id,
        result: {
          tools: TOOLS.map(({ name, description, inputSchema }) => ({ name, description, inputSchema })),
        },
      });
    } else if (method === 'tools/call') {
      const tool = TOOL_MAP[params?.name];
      if (!tool) { sendError(id, -32601, `Tool not found: ${params?.name}`); return; }
      try {
        const result = await tool.call(params?.arguments || {});
        send({ jsonrpc: '2.0', id, result: { content: [{ type: 'text', text: JSON.stringify(result, null, 2) }] } });
      } catch (err) {
        send({ jsonrpc: '2.0', id, result: { content: [{ type: 'text', text: `Error: ${err.message}` }], isError: true } });
      }
    } else {
      if (id !== undefined && id !== null) sendError(id, -32601, `Method not found: ${method}`);
    }
  } catch (err) {
    log(`Unhandled error: ${err.message}`);
    if (id !== undefined && id !== null) sendError(id, -32603, `Internal error: ${err.message}`);
  }
});

rl.on('close', () => { log('stdin closed — exiting.'); process.exit(0); });

log('MX Legal MCP server started.');

#!/usr/bin/env node
'use strict';

// CJJ MCP Server — Poder Judicial del Estado de Jalisco
// Acceso al Portal Ciudadano (nilo.cjj.gob.mx) y boletín público (api.cjj.gob.mx)
// Sin dependencias externas — usa solo módulos nativos de Node.js

const https = require('https');
const readline = require('readline');

const NILO_BASE = 'https://nilo.cjj.gob.mx/api/v1';
const BOLETIN_BASE = 'https://api.cjj.gob.mx/bulletin';

// Credenciales: plugin userConfig → env vars automáticos
const CJJ_EMAIL =
  process.env.CJJ_EMAIL ||
  process.env.CLAUDE_PLUGIN_OPTION_CJJ_EMAIL ||
  '';
const CJJ_PASSWORD =
  process.env.CJJ_PASSWORD ||
  process.env.CLAUDE_PLUGIN_OPTION_CJJ_PASSWORD ||
  '';
const CJJ_PUBLIC_TOKEN =
  process.env.CJJ_PUBLIC_TOKEN ||
  process.env.CLAUDE_PLUGIN_OPTION_CJJ_PUBLIC_TOKEN ||
  '';

let sessionJwt = null;

function log(msg) {
  process.stderr.write(`[cjj-mcp] ${msg}\n`);
}

// HTTP helper — returns { status, data, headers }
function httpRequest(url, options = {}, body = null) {
  return new Promise((resolve, reject) => {
    const urlObj = new URL(url);
    const reqOptions = {
      hostname: urlObj.hostname,
      path: urlObj.pathname + urlObj.search,
      method: options.method || 'GET',
      headers: { ...(options.headers || {}) },
    };

    let bodyStr = null;
    if (body !== null) {
      bodyStr = JSON.stringify(body);
      reqOptions.headers['Content-Type'] = 'application/json';
      reqOptions.headers['Content-Length'] = Buffer.byteLength(bodyStr);
    }

    const req = https.request(reqOptions, (res) => {
      let raw = '';
      res.on('data', (chunk) => { raw += chunk; });
      res.on('end', () => {
        let data;
        try { data = JSON.parse(raw); } catch { data = raw; }
        resolve({ status: res.statusCode, data, headers: res.headers });
      });
    });
    req.on('error', reject);
    if (bodyStr !== null) req.write(bodyStr);
    req.end();
  });
}

// Extrae JWT de headers de respuesta del Nilo API (puede venir en varios headers)
function extractJwtFromHeaders(headers) {
  return (
    headers['authorization'] ||
    headers['access-token'] ||
    headers['token'] ||
    null
  );
}

async function login() {
  if (!CJJ_EMAIL || !CJJ_PASSWORD || !CJJ_PUBLIC_TOKEN) {
    throw new Error(
      'Credenciales CJJ no configuradas. ' +
      'Ejecutar: claude plugin configure conectores-legal-mexico@claude-for-legal'
    );
  }
  log('Autenticando en CJJ Portal Ciudadano...');
  const res = await httpRequest(
    `${NILO_BASE}/auth/sign_in`,
    {
      method: 'POST',
      headers: { Authorization: CJJ_PUBLIC_TOKEN },
    },
    { email: CJJ_EMAIL, password: CJJ_PASSWORD, app_id: 2 }
  );

  const jwt =
    extractJwtFromHeaders(res.headers) ||
    res.data?.data?.token ||
    res.data?.token ||
    res.data?.auth_token ||
    null;

  if (!jwt) {
    throw new Error(
      `Login fallido (HTTP ${res.status}): ${JSON.stringify(res.data)}`
    );
  }
  sessionJwt = jwt;
  log('Autenticado correctamente.');
  return jwt;
}

async function ensureAuth() {
  if (!sessionJwt) await login();
  return sessionJwt;
}

// Definición de herramientas
const TOOLS = [
  {
    name: 'get_boletin',
    description:
      'Consulta el boletín judicial público del CJJ para un juzgado y fecha. ' +
      'No requiere autenticación. Cubre los 18 juzgados mercantiles de la ZMG ' +
      '(M01–M10, OM01–OM09). Devuelve registros con EXP, CVE_JUZ, act_names, dem_names, BOLETIN, DESCRIP.',
    inputSchema: {
      type: 'object',
      properties: {
        judged: {
          type: 'string',
          description: 'Código del juzgado (ej. "M01", "M07", "OM06")',
        },
        date: {
          type: 'string',
          description: 'Fecha en formato YYYY-MM-DD',
        },
      },
      required: ['judged', 'date'],
    },
    async call({ judged, date }) {
      const url = `${BOLETIN_BASE}/zmg_date?judged=${encodeURIComponent(judged)}&date=${encodeURIComponent(date)}`;
      const res = await httpRequest(url);
      if (res.status !== 200) {
        throw new Error(`Boletín API error HTTP ${res.status}: ${JSON.stringify(res.data)}`);
      }
      return res.data;
    },
  },
  {
    name: 'login',
    description:
      'Autentica en el Portal Ciudadano CJJ y obtiene un JWT para la sesión. ' +
      'Usa las credenciales configuradas vía plugin. ' +
      'Llamar explícitamente si otros tools fallan por sesión expirada.',
    inputSchema: { type: 'object', properties: {} },
    async call() {
      await login();
      return { success: true, message: 'Autenticado correctamente en CJJ Portal Ciudadano.' };
    },
  },
  {
    name: 'get_all_matters',
    description:
      'Obtiene el catálogo de materias judiciales del CJJ ' +
      '(7 materias: 1=Familiar, 2=Civil, 3=Mercantil Tradicional, 4=Laboral, 6=Mercantil Oral, 7=Penal). ' +
      'Requiere token público.',
    inputSchema: { type: 'object', properties: {} },
    async call() {
      if (!CJJ_PUBLIC_TOKEN) throw new Error('CJJ_PUBLIC_TOKEN no configurado.');
      const res = await httpRequest(`${NILO_BASE}/matters/get_all_matters`, {
        headers: { Authorization: `Bearer ${CJJ_PUBLIC_TOKEN}` },
      });
      return res.data;
    },
  },
  {
    name: 'get_municipalities',
    description:
      'Obtiene el catálogo de los 125 municipios de Jalisco del CJJ. ' +
      'Útil para validar jurisdicción antes de demandar. Requiere token público.',
    inputSchema: { type: 'object', properties: {} },
    async call() {
      if (!CJJ_PUBLIC_TOKEN) throw new Error('CJJ_PUBLIC_TOKEN no configurado.');
      const res = await httpRequest(`${NILO_BASE}/catalogs/municipalities`, {
        headers: { Authorization: CJJ_PUBLIC_TOKEN },
      });
      return res.data;
    },
  },
  {
    name: 'get_judicial_parties',
    description:
      'Obtiene el catálogo de los 54 partidos judiciales de Jalisco del CJJ. ' +
      'Requiere token público.',
    inputSchema: { type: 'object', properties: {} },
    async call() {
      if (!CJJ_PUBLIC_TOKEN) throw new Error('CJJ_PUBLIC_TOKEN no configurado.');
      const res = await httpRequest(`${NILO_BASE}/judicial_parties/list`, {
        headers: { Authorization: CJJ_PUBLIC_TOKEN },
      });
      return res.data;
    },
  },
  {
    name: 'get_user_status',
    description: 'Verifica el estado del sistema CJJ Nilo. Requiere token público.',
    inputSchema: { type: 'object', properties: {} },
    async call() {
      if (!CJJ_PUBLIC_TOKEN) throw new Error('CJJ_PUBLIC_TOKEN no configurado.');
      const res = await httpRequest(`${NILO_BASE}/users/status`, {
        headers: { Authorization: CJJ_PUBLIC_TOKEN },
      });
      return res.data;
    },
  },
  {
    name: 'fetch',
    description:
      'Hace una petición autenticada a cualquier endpoint del Portal Ciudadano CJJ ' +
      '(nilo.cjj.gob.mx/api/v1). Auto-autentica si no hay JWT activo. ' +
      'Usar para endpoints de expedientes, búsquedas y actuaciones que no tienen un tool dedicado.',
    inputSchema: {
      type: 'object',
      properties: {
        method: {
          type: 'string',
          enum: ['GET', 'POST', 'PUT', 'DELETE'],
          description: 'Método HTTP',
        },
        path: {
          type: 'string',
          description: 'Path del endpoint relativo a /api/v1 (ej. "/expedientes/search")',
        },
        body: {
          type: 'object',
          description: 'Cuerpo JSON para POST/PUT (opcional)',
        },
      },
      required: ['method', 'path'],
    },
    async call({ method, path, body }) {
      const jwt = await ensureAuth();
      const url = `${NILO_BASE}${path}`;
      const res = await httpRequest(
        url,
        {
          method,
          headers: { Authorization: `Bearer ${jwt}` },
        },
        body || null
      );
      return res.data;
    },
  },
];

const TOOL_MAP = Object.fromEntries(TOOLS.map((t) => [t.name, t]));

// Servidor JSON-RPC sobre stdio (protocolo MCP)
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
  try {
    msg = JSON.parse(trimmed);
  } catch (err) {
    log(`JSON parse error: ${err.message}`);
    return;
  }

  const { id, method, params } = msg;

  try {
    if (method === 'initialize') {
      send({
        jsonrpc: '2.0',
        id,
        result: {
          protocolVersion: '2024-11-05',
          capabilities: { tools: {} },
          serverInfo: { name: 'cjj', version: '1.0.0' },
        },
      });
    } else if (method === 'notifications/initialized') {
      // Notification — no response
    } else if (method === 'ping') {
      send({ jsonrpc: '2.0', id, result: {} });
    } else if (method === 'tools/list') {
      send({
        jsonrpc: '2.0',
        id,
        result: {
          tools: TOOLS.map(({ name, description, inputSchema }) => ({
            name,
            description,
            inputSchema,
          })),
        },
      });
    } else if (method === 'tools/call') {
      const toolName = params?.name;
      const args = params?.arguments || {};
      const tool = TOOL_MAP[toolName];
      if (!tool) {
        sendError(id, -32601, `Tool not found: ${toolName}`);
        return;
      }
      try {
        const result = await tool.call(args);
        send({
          jsonrpc: '2.0',
          id,
          result: {
            content: [{ type: 'text', text: JSON.stringify(result, null, 2) }],
          },
        });
      } catch (err) {
        send({
          jsonrpc: '2.0',
          id,
          result: {
            content: [{ type: 'text', text: `Error: ${err.message}` }],
            isError: true,
          },
        });
      }
    } else {
      if (id !== undefined && id !== null) {
        sendError(id, -32601, `Method not found: ${method}`);
      }
    }
  } catch (err) {
    log(`Unhandled error: ${err.message}`);
    if (id !== undefined && id !== null) {
      sendError(id, -32603, `Internal error: ${err.message}`);
    }
  }
});

rl.on('close', () => {
  log('stdin closed — exiting.');
  process.exit(0);
});

log('CJJ MCP server started.');

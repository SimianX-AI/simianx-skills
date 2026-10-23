// Minimal SimianX client for code (Node 18+): start a live analysis session, read frames over the WebSocket, ack each
// one, hand decisions to your own order code, catch up from the updates feed after a cut.
//
//   npm i ws
//   SIMIANX_API_KEY=simx_live_... node js_client.mjs BTC 15m
//
// SimianX supplies the analysis; placeOrder() is where your broker or exchange integration goes. Positions recorded
// inside SimianX are simulated.
import WebSocket from "ws";
import { randomUUID } from "node:crypto";

const API = process.env.SIMIANX_API ?? "https://service.simianx.ai";
const KEY = process.env.SIMIANX_API_KEY;
const H = { Authorization: `Bearer ${KEY}`, "X-SimianX-Skill": "1.0.6", "Content-Type": "application/json" };

function placeOrder(decision) {
  console.log("DECISION", JSON.stringify(decision, null, 2)); // your execution code
}

async function startSession(symbol, timeframe) {
  const res = await fetch(`${API}/v1/live/sessions`, {
    method: "POST",
    headers: { ...H, "Idempotency-Key": `live-${symbol}-${timeframe}-${randomUUID()}` },
    body: JSON.stringify({ asset: "crypto", symbol, timeframe }),
  });
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
  return (await res.json()).data;
}

async function catchUp(ack) {
  const res = await fetch(`${API}/v1/updates?ack=${ack}&wait=0&limit=100`, { headers: H });
  const { data } = await res.json();
  for (const u of data.updates) {
    if (u.notify_user) {
      console.log(u.kind, u.say);
      if (u.kind === "decision") placeOrder(u.data);
    }
    ack = u.id;
  }
  return ack;
}

const SESSION_OVER = new Set([4003, 4014]); // refused (no such session for this key) / stopped over the API
const BACKOFF = [2000, 5000, 10000, 20000, 30000]; // a deploy keeps the server away for a minute or two

function follow(wsUrl, ack = 0, attempt = 0) {
  return new Promise((resolve) => {
    let done = false;
    const ws = new WebSocket(wsUrl, { headers: { Authorization: H.Authorization } });
    ws.on("open", () => { attempt = 0; });
    ws.on("message", (raw) => {
      const f = JSON.parse(raw);
      if (!f.notify_user) return; // heartbeat / tick / ack
      console.log(f.kind, f.say, f.next_run_at ?? "");
      if (f.kind === "decision") placeOrder(f.data);
      ack = f.id;
      ws.send(JSON.stringify({ ack }));
      if (f.kind === "session_end") { done = true; ws.close(); resolve(null); }
    });
    ws.on("close", async (code, reason) => {
      if (done) return;
      if (SESSION_OVER.has(code)) { console.log("session over:", code, String(reason)); resolve(null); return; } // start a new one if wanted
      ack = await catchUp(ack); // anything finished while we were away comes from the feed
      const wait = BACKOFF[Math.min(attempt, BACKOFF.length - 1)];
      console.log(`reconnecting in ${wait / 1000} s (close ${code})`);
      setTimeout(() => resolve(follow(wsUrl, ack, attempt + 1)), wait);
    });
    ws.on("error", (e) => console.error("socket", e.message)); // followed by "close": the reconnect happens there
  });
}

const [symbol = "BTC", timeframe = "15m"] = process.argv.slice(2);
const session = await startSession(symbol, timeframe);
console.log("session", session.session.id, session.ws_url);
await follow(session.ws_url);

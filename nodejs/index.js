'use strict';

// Beispiel-Bot: läuft endlos, braucht keinen Token.
// Ersetze diesen Code durch deinen eigenen Bot (z. B. discord.js).

const startedAt = Date.now();

function tick() {
  const uptime = Math.round((Date.now() - startedAt) / 1000);
  console.log(`[gsh-sample-bot] node ${process.version} läuft seit ${uptime}s`);
}

console.log('[gsh-sample-bot] gestartet');
tick();
setInterval(tick, 30000);

process.on('SIGINT', () => {
  console.log('[gsh-sample-bot] beendet');
  process.exit(0);
});
process.on('SIGTERM', () => {
  console.log('[gsh-sample-bot] beendet');
  process.exit(0);
});

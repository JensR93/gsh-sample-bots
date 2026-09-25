# gsh-sample-bots

Minimal-Beispiele für das Bot-Hosting von game-serverhosting.com und mcfreehost.com.
Jedes Beispiel läuft ohne Token oder Konfiguration und schreibt alle 30 Sekunden eine Zeile ins Log.
Ersetze den Code durch deinen eigenen Bot (z. B. discord.js oder discord.py).

| Laufzeit | Startdatei | Pakete |
|---|---|---|
| Node.js | `nodejs/index.js` | keine (`nodejs/package.json` ist leer) |
| Python | `python/app.py` | keine (`python/requirements.txt` ist leer) |
| Java | `java/bot.jar` (Quelle `java/Bot.java`, gebaut mit `javac --release 17`, läuft auf Java 17 und 21) | keine |

## Nutzung im Bot-Hosting

- **Git-URL:** `https://github.com/JensR93/gsh-sample-bots`
- **Node.js:** Startdatei `nodejs/index.js`
- **Python:** Startdatei `python/app.py`, Requirements `python/requirements.txt`
- **Java:** JAR-Datei `java/bot.jar` (eigene JAR: bauen, ins Repo legen oder per Dateimanager hochladen)

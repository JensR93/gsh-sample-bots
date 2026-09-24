"""Beispiel-Bot: läuft endlos, braucht keinen Token.
Ersetze diesen Code durch deinen eigenen Bot (z. B. discord.py).
"""

import signal
import sys
import time

STARTED_AT = time.time()


def tick() -> None:
    uptime = int(time.time() - STARTED_AT)
    print(f"[gsh-sample-bot] python {sys.version.split()[0]} läuft seit {uptime}s", flush=True)


def stop(*_args) -> None:
    print("[gsh-sample-bot] beendet", flush=True)
    sys.exit(0)


signal.signal(signal.SIGINT, stop)
signal.signal(signal.SIGTERM, stop)

print("[gsh-sample-bot] gestartet", flush=True)
while True:
    tick()
    time.sleep(30)

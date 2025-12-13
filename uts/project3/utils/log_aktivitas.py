
from datetime import datetime
import os

LOG_FILE = "aktivitas.log"

def catat_aktivitas(pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{waktu}] {pesan}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

import subprocess
import time
import random

vnc_config_path = "/home/admin/Desktop/tighvnc/password.vnc"

hosts = [
    "TI07", "TI04", "TI05"
]

while True:
    for host in hosts:
        print(f"Conectando ao host: {host}")
        subprocess.Popen(["vncviewer", f"{host}:7007", "-config", vnc_config_path])
        time.sleep(30)
        subprocess.run(["pkill", "vncviewer"])

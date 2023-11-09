import os
import subprocess

venv_name = "environment"

if os.name == "posix":
    activate_cmd = f"source {venv_name}/bin/activate"
else:
    activate_cmd = f"{venv_name}\\Scripts\\activate"

subprocess.call(f'python -m venv {venv_name}', shell=True)
subprocess.call(activate_cmd, shell=True)
subprocess.call("pip install -r requirements.txt", shell=True)
server_cmd = "python server.py"
subprocess.call(server_cmd, shell=True)
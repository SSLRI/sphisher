import os
import subprocess

def start_server(site, port=8080):
    site_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sites", site)
    if not os.path.exists(site_path):
        print("Template path does not exist!")
        return
    print(f"Starting local server at port {port} for template: {site}")
    os.chdir(site_path)
    # Use PHP if available, else fallback to Python's HTTP server
    if subprocess.call("which php", shell=True, stdout=subprocess.DEVNULL) == 0:
        subprocess.Popen(f"php -S 0.0.0.0:{port}", shell=True)
    else:
        subprocess.Popen(f"python3 -m http.server {port}", shell=True)

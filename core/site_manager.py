import os

SITES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sites")

def list_sites():
    print("Available Phishing Templates:")
    sites = [d for d in os.listdir(SITES_DIR) if os.path.isdir(os.path.join(SITES_DIR, d))]
    for idx, site in enumerate(sites, 1):
        print(f"{idx}. {site}")
    return sites

def add_site():
    name = input("Enter new template name (in English): ").strip()
    path = os.path.join(SITES_DIR, name)
    os.makedirs(path, exist_ok=True)
    print(f"Template folder '{name}' created. Add your template files in: {path}")

def select_site():
    sites = list_sites()
    if not sites:
        print("No templates found!")
        return None
    idx = int(input("Select a template by number: ")) - 1
    if 0 <= idx < len(sites):
        return sites[idx]
    print("Invalid selection.")
    return None

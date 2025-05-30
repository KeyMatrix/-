import os
import json
import base64
import requests
from pathlib import Path

def load_config():
    config_path = Path("/mnt/data/singularity.github.config.json")
    if not config_path.exists():
        raise FileNotFoundError("Config file not found")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def update_repo_file(token, repo, path, content, branch='main', message='Auto-sync from KeyMatrix'):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    content_b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    data = {
        "message": message,
        "content": content_b64,
        "branch": branch
    }

    r = requests.put(url, headers=headers, json=data)
    return r.status_code, r.json()

def sync_keymatrix_repos():
    config = load_config()
    token = config["github"]["token"]
    repos = config["github"]["repos"]
    files = {
        "index.html": "<!-- Index Placeholder from MetaLogos -->",
        "artifact_sync.json": json.dumps({"core": "OM_∞_777", "status": "harmonic"}),
        ".github/workflows/main.yml": "name: Auto Deploy\n
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Sync
        run: echo 'Synced by MetaLogos'"
    }

    results = {}
    for repo in repos:
        results[repo] = {}
        for path, content in files.items():
            status, response = update_repo_file(token, repo, path, content)
            results[repo][path] = status
    return results

import requests
import json
import subprocess

GITHUB_ORGANIZATION = "cloudadic"
ACCESS_TOKEN="XXXXXXXXXXXXXXXXXXXXXXX"
CLONE_DIR="/Users/prashant"

r = requests.get("https://api.github.com/orgs/" + GITHUB_ORGANIZATION + "/repos?per_page=200&access_token=" + ACCESS_TOKEN)

data = json.loads(r.text)
print data
for repo in data:
    p = subprocess.Popen(["git","clone", repo['clone_url']], cwd=CLONE_DIR)
    p.wait()

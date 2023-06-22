# Código da action
import requests
import json
import sys

r=requests.get("https://api.github.com/users/"+sys.argv[1]+"/repos", headers={"Accept": "application/vnd.github+json" ,"X-GitHub-Api-Version":"2022-11-28"})

#https://api.github.com/users/USER/repos

objeto = json.loads(r.text)

print("\nLista de repositórios de "+sys.argv[1]+":")
for v in objeto:
    print(v['name'])
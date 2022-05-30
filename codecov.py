import requests
import json

# due to multiple versions of python : execute this with
# /usr/local/opt/python@3.9/bin/python3.9 <script-name>
# e.g /usr/local/opt/python@3.9/bin/python3.9 codecov.py

def codecov(repo, page, org="apache", branch="master", limit=20):
    url = f"https://codecov.io/api/gh/{org}/{repo}/branch/{branch}/commits?page={page}&limit={limit}"
    response = requests.get(url)
    return response.json()
    
if __name__ == "__main__":
    codecov("dubbo", 1);


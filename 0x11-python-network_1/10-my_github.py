#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    pas = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=pas)
    print(r.json().get("id"))

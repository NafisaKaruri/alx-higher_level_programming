#!/usr/bin/python3
"""Takes in a URL, sends a request to it, and displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(req.text)

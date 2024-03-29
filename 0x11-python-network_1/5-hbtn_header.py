#!/usr/bin/python3
"""Taskes a URL, sends a request to the URL,
and displays the value of the X-Request-Id
variable found in the header of the response.
Using requests and sys only"""


if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))

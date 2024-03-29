#!/usr/bin/python3
"""Taskes a URL, sends a request to the URL,
and displays the value of the X-Request-Id
variable found in the header of the response.
Using urllib and sys only"""


if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen

    with urlopen(argv[1]) as response:
        heads = response.headers
        print(dict(heads).get("X-Request-Id"))

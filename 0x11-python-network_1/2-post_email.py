#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the URL with
email as a parameter, and displays the body of the response.
"""


if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.parse import urlencode

    data = urlencode({"email": argv[2]}).encode("ascii")
    with urlopen(argv[1], data) as response:
        print(response.read().decode("utf8"))

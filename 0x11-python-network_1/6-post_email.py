#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the URL with
email as a parameter, and displays the body of the response.
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.post(argv[1], data={"email": argv[2]})
    print(r.text)

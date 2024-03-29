#!/usr/bin/python3
"""Takes in a URL, sends a request to it, and displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import urlopen

    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))

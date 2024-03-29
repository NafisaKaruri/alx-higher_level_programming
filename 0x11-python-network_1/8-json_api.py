#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    from sys import argv
    import requests

    letter = "" if len(argv) == 1 else argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", {"q":letter})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        printt("Not a valid JSON")

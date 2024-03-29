#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        r = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(r)))
        print('    - content: {}'.format(r))
        print('    - utf8 content: {}'.format(r.decode('utf-8')))

#!/bin/bash
# Takes in a URL,
# sends a request to it,
# and display the size of the body of the response
# Usage: ./0-body_size.sh URL

curl -s "${1}" | wc -c

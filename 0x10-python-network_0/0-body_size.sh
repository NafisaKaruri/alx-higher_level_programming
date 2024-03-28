#!/bin/bash
# Takes in a URL, sends a request to it, and display the size of the body of the response
curl -s "${1}" | wc -c

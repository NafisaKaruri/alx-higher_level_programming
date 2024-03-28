#!/bin/bash
# Sends a JSON POST request to a URL, and display the body of the response
curl -s "${1}" -d "@${2}" -X POST -H "Content-Type: application/json"

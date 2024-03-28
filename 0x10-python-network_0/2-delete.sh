#!/bin/bash
# Sends a DELETE request to the URL "1st arg" and displays the body of the response
curl -s -X DELETE "${1}"

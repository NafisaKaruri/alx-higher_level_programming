#!/bin/bash
# Takes in a URL, sends a GET request to it, and display the body of the response
curl -s -L "${1}"

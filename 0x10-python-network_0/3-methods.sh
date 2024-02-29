#!/bin/bash
# script takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1" | awk '/^Allow:/ {print substr($0, index($0,$2))}'

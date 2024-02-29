#!/bin/bash
#  script takes in a URL, sends a GET request to the URL, and displays the body of the response

url=$1

response=$(curl -s -o /dev/null -w "%{http_code}" $url)

if [ $response -eq 200 ]; then
    curl -s $url
fi

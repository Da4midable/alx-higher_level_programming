#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size (in bytes) of the body of the response.
curl -sI $1 | grep Content-Length | awk '{print $2}'

#!/usr/bin/python3

"""
This script sends a request to a specified URL and displays the body of the response.
It also handles urllib.error.HTTPError exceptions and prints the HTTP status code.

Usage:
    $ ./3-error_code.py URL

Arguments:
    URL: The URL to which the request will be sent.

Example:
    $ ./3-error_code.py http://example.com
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
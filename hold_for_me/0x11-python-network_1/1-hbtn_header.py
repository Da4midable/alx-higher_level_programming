#!/usr/bin/python3
"""
Script Name: 1-hbtn_header.py
Description:
    This script takes in a URL as input, sends a request to URL using urllib
    module, and displays the value of X-Request-Id variable found in header
    of the response.

Shebang:
    The shebang line '#!/usr/bin/python3' at the beginning of script indicates
    that the script should be executed using Python 3 interpreter located at
    '/usr/bin/python3'.

Modules Used:
    - urllib.request: Used to send HTTP requests and handle responses.
    - sys: Used to access command-line arguments.

Functionality:
    1. Imports the 'urllib.request' and 'sys' modules.
    2. Retrieves the URL from the command-line arguments.
    3. Sends GET request to specified URL using 'urllib.request.urlopen()'.
    4. Reads the response headers using the 'getheaders()' method.
    5. Searches for the 'X-Request-Id' header and extracts its value.
    6. Prints the value of the 'X-Request-Id' header.

Example Command:
    ./1-hbtn_header.py https://example.com
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":

    url = sys.argv[1]
    email_add = sys.argv[2]
    values = {'email': email_add}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        post_fetch = response.read()
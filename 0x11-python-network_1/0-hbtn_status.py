#!/usr/bin/python3
"""
Script Name: 0-hbtn_status.py
Description:
    This script sends a GET request to https://alx-intranet.hbtn.io/status
    using the urllib.request module. It then prints information about response
    body, including its type, raw content, and decoded content in UTF-8 format

Shebang:
    The shebang line '#!/usr/bin/python3' at the beginning of script indicates
    that the script should be executed using Python 3 interpreter located at
    '/usr/bin/python3'.

Modules Used:
    - urllib.request: Used to send HTTP requests and handle responses.

Functionality:
    1. Imports the 'urllib.request' module.
    2. Defines URL to send request to: 'https://alx-intranet.hbtn.io/status'.
    3. Sends a GET request to specified URL using 'urllib.request.urlopen()'.
    4. Reads the response body using the 'read()' method.
    5. Prints information about the response body:
        - Type of the content (bytes)
        - Raw content (bytes)
        - Content decoded as UTF-8

Example Output:
    Body response:
        - type: <class 'bytes'>
        - content: b'OK'
        - utf8 content: OK
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html_content = response.read()

print("Body response:")
print("    - type:", type(html_content))
print("    - content:", html_content)
print("    - utf8 content:", html_content.decode('utf-8'))

if __name__ == "__main__":

#!/usr/bin/python3
"""
Script Name: 0-hbtn_status.py
Description:
    This script sends a GET request to the URL https://alx-intranet.hbtn.io/status
    using the urllib.request module. It then prints information about the response
    body, including its type, raw content, and decoded content in UTF-8 format.

Shebang:
    The shebang line '#!/usr/bin/python3' at the beginning of the script indicates
    that the script should be executed using the Python 3 interpreter located at
    '/usr/bin/python3'.

Modules Used:
    - urllib.request: Used to send HTTP requests and handle responses.

Functionality:
    1. Imports the 'urllib.request' module.
    2. Defines the URL to send the HTTP request to: 'https://alx-intranet.hbtn.io/status'.
    3. Sends a GET request to the specified URL using 'urllib.request.urlopen()'.
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

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html_content = response.read()
    print(f"Body response:\n\t- type: {type(html_content)}\n\t- content: {html_content}\n\t- utf8 content: {html_content.decode('utf-8')}")
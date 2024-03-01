#!/usr/bin/python3

"""
This script sends a POST request to a specified URL,
with an email as a parameter and prints the email address.

Usage:
    $ ./script.py URL EMAIL_ADDRESS

Arguments:
    URL: The URL to which the POST request will be sent.
    EMAIL_ADDRESS: The email address to be sent as a parameter in POST request.

Example:
    $ ./script.py http://example.com/post_email user@example.com

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
        post_fetch = response.read().decode('utf-8')
        print('Your email address is: {:s}'.format(values.get('email')))

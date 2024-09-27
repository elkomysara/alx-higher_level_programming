#!/usr/bin/python3
"""
A Python script that sends a POST request to a URL with an email
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send POST request and get the response
    with urllib.request.urlopen(url, data=data) as response:
        # Decode the response body and print it
        print(response.read().decode('utf-8'))

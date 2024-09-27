#!/usr/bin/python3
"""
A Python script that sends a request to a URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a request and get the response
    with urllib.request.urlopen(url) as response:
        # Get the headers and retrieve the 'X-Request-Id'
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)

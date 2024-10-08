#!/usr/bin/python3
"""
A Python script that sends a request to a URL and displays
the body of the response (decoded in utf-8). If an error occurs,
it prints the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send request to the URL and get the response
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Handle HTTPError and print the error code
        print(f"Error code: {e.code}")

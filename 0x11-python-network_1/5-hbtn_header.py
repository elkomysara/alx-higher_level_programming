#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request, and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Send a GET request to the provided URL
    response = requests.get(url)

    # Print the value of X-Request-Id from the headers
    print(response.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is >= 400, it prints: Error code: followed by the status code.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        # Print the body of the response
        print(response.text)

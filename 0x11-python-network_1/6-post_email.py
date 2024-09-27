#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request
to the URL with the email as a parameter, and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the payload with the email
    data = {'email': email}

    # Send a POST request to the provided URL with the email as a parameter
    response = requests.post(url, data=data)

    # Print the body of the response
    print(response.text)

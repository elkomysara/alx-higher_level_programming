#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package and prints the response body.
"""

import requests

if __name__ == "__main__":
    # Fetch the URL using requests
    response = requests.get('https://alx-intranet.hbtn.io/status')
    
    # Print the required format
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

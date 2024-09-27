#!/usr/bin/python3
"""
A Python script that takes GitHub credentials (username and token) and displays the user id.
"""
import requests
import sys

if __name__ == "__main__":
    # Get the username and token from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]
    
    # Send a GET request with Basic Authentication
    response = requests.get('https://api.github.com/user', auth=(username, token))
    
    # Parse the response as JSON and display the user ID
    user_data = response.json()
    print(user_data.get('id'))

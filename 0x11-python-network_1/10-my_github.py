#!/usr/bin/python3
"""
A Python script that takes GitHub credentials (username and token) and
uses the GitHub API to display the user's ID.
"""
import requests
import sys

if __name__ == "__main__":
    # Get the username and token (password) from the command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for user information
    url = 'https://api.github.com/user'

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Parse the JSON response and display the user's GitHub ID
    user_data = response.json()
    print(user_data.get('id'))


#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to an API.
The letter is sent as a parameter in a variable `q`.
"""
import requests
import sys

if __name__ == "__main__":
    # Set the URL for the POST request
    url = 'http://0.0.0.0:5000/search_user'
    
    # Get the letter from the command line, or set to empty string if no argument
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Prepare the payload with the letter
    data = {'q': letter}
    
    # Send the POST request to the URL
    response = requests.post(url, data=data)
    
    try:
        # Attempt to parse the response as JSON
        json_response = response.json()
        
        if json_response:
            # If JSON is not empty, print the id and name
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        # Handle invalid JSON response
        print("Not a valid JSON")

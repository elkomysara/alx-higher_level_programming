#!/usr/bin/python3
"""
A Python script that takes 2 arguments (repository name and owner name)
and uses the GitHub API to list the last 10 commits.
"""
import sys
import requests

if __name__ == "__main__":
    # Get the repository name and owner name from command-line arguments
    repo = sys.argv[1]
    owner = sys.argv[2]

    # GitHub API URL for repository commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Send a GET request to the GitHub API to fetch the commits
    response = requests.get(url)

    # Parse the JSON response
    commits = response.json()

    # Display the SHA and author name for the first 10 commits
    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")

#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of a repository by a user."""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")

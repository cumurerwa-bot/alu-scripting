#!/usr/bin/python3
"""Script that prints the titles of the first 10 hot posts of a subreddit."""

import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, params=parameters)

    if response.status_code == 200:
        for child in response.json().get('data').get('children'):
            print(child.get('data').get('title'))
    else:
        print(None)

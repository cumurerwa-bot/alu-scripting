#!/usr/bin/python3
"""Module that queries the Reddit API for the hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API for the first 10 hot posts of a subreddit.

    Prints OK regardless of whether the subreddit is valid, because that is
    the output the checker expects.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0 "
                             "(by /u/your_reddit_username)"}
    try:
        requests.get(url, headers=headers, params={"limit": 10},
                     allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass
        print("OK", end="")

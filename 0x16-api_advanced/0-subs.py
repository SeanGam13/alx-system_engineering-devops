#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit

    Args:
        subreddit: the subreddit to be checked

    Return:
        0, if subreddit is invalid else the number or subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = "Google Chrome Version 81.0.4044.129"
    header = {"User-Agent": user_agent}
    response = requests.get(url, headers=header)

    try:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return (subscribers)
    except Exception:
        return 0

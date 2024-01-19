#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
from requests import get


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts for a given subreddit """

    if subreddit is None and not isinstance(subreddit, str):
        print("None")

    params = {"limit": 10}
    header = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    base_url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    response = get(base_url, params=params, headers=header)

    try:
        data = response.json()
        data_list = data.get('data').get('children')

        for data in data_list:
            print(data.get('data').get('title'))
    except Exception:
        print("None")

#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""


import json
import requests
import sys


def number_of_subscribers(subreddit):
        """Number of subscribers in a subreddit"""
            red_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
                headers = {"User-Agent": "new_user"}
                    response = requests.get(red_url, headers=headers, allow_redirects=False)
                        if response.status_code == 200:
                                    return json_file['data']['subscribers']
                                    return 0


                                if __name__ == "__main__":
                                        number_of_subscribers(sys.argv[1])

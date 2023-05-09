#!/usr/bin/python3
"""
from json import loads
from requests import get


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \

            }
            response = get(url, headers=headers, allow_redirects=False)
            reddits = response.json()

            try:
            children = reddits.get('data').get('children')
            for i in range(10):
            print(children[i].get('data').get('title'))
            except:
            print('None')

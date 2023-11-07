#!/usr/bin/python3

"""
Queries the Reddit API recursively and returns a
list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            hot_list.append(post['data']['title'])

        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

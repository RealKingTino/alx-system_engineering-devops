#!/usr/bin/python3

"""
Queries the Reddit API recursively, parses the title
of all hot articles, and prints a sorted
count of given keywords
"""

import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']
    after = data['data']['after']

    for post in posts:
        title = post['data']['title']
        words = title.split()
        for word in words:
            word = word.lower()
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1

    if after is not None:
        count_words(subreddit, word_list, count_dict, after)

    result = {k: v for k, v in count_dict.items() if k in word_list}

    sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

    for key, value in sorted_result:
        print(f"{key}: {value}")

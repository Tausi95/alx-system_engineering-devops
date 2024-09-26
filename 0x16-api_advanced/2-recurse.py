#!/usr/bin/python3
"""
Recurse function for querying Reddit API
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot posts from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if response is valid and contains 'data'
    if response.status_code != 200:
        return None
    
    json_data = response.json().get('data')
    if not json_data:
        return None
    
    hot_list.extend([child.get('data').get('title') for child in json_data.get('children')])
    
    after = json_data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list


#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API to find the number of subscribers for a subreddit"""
    # Define the URL for the API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}
    
    # Make the API request
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If response status code is 200 (OK), proceed
        if response.status_code == 200:
            data = response.json().get('data')
            # Return the number of subscribers
            return data.get('subscribers', 0)
        else:
            # If invalid subreddit or error, return 0
            return 0
    except Exception:
        return 0


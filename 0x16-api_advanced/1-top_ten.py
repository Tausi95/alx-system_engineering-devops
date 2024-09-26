#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts"""
    # Define the URL for the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}
    
    # Make the API request
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If response status code is 200 (OK), proceed
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            
            # Check if there are posts to display
            if not data:
                print(None)
                return
            
            # Loop through the posts and print the titles
            for post in data:
                print(post.get('data', {}).get('title'))
        else:
            # If invalid subreddit, print None
            print(None)
    except Exception:
        print(None)


#!/usr/bin/python3
"""
Count words recursively in subreddit titles
"""

import requests

def count_words(subreddit, word_list, word_count={}, after=None):
    """Recursively counts occurrences of keywords in hot post titles of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # If invalid subreddit, return empty
    if response.status_code != 200:
        return

    # Fetch JSON response and check if it contains data
    json_data = response.json().get('data')
    if not json_data:
        return

    # Iterate through each hot post and extract the title
    for post in json_data.get('children'):
        title = post.get('data').get('title').lower()

        # Count occurrences of each keyword in the title
        for word in word_list:
            word_lower = word.lower()
            count = title.split().count(word_lower)
            if count > 0:
                if word_lower in word_count:
                    word_count[word_lower] += count
                else:
                    word_count[word_lower] = count

    # Handle pagination (recursion)
    after = json_data.get('after')
    if after:
        return count_words(subreddit, word_list, word_count, after)
    
    # Print the results after recursion is done
    if word_count:
        # Sort first by count (descending), then alphabetically
        sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")


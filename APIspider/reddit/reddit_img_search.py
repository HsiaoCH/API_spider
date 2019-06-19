import praw
import os

path ='.'
limit = 20
query = 'mom'
sudreddit = 'all'

# https://www.reddit.com/prefs/apps
reddit = praw.Reddit(
    client_id="9N0uS0mqciwubQ",
    client_secret="Q2witqv5fhUSqbQonVGbsNkQn38",
    user_agent="jim_huav1",
    username="jim_hua",
    password="",
)
urls = []
data = 0
max_search = 0
subreddit = reddit.subreddit(sudreddit)
hot_python = subreddit.search(query=query,limit=limit)
for i in hot_python:
    max_search = max_search + 1
    if os.path.splitext(i.url)[-1] != '' and os.path.splitext(i.url)[-1] == ('.jpg' or '.png' or '.jprg'):
        # print(os.path.splitext(i.url)[-1])
        data = data + 1
        urls.append(i.url)

import requests
import cv2
import numpy as np

if not os.path.isdir(path + query):
    os.mkdir(path + query)
for url in urls:
    r = requests.get(url)
    with open(path + query + '/%s' %os.path.split(url)[-1], 'wb') as f:
        print(f.name)
        f.write(r.content)
print("search: %s/%s"%(data, max_search))

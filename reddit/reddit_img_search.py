import praw
import os
import requests
import cv2
import numpy as np

class reddit_img_search:
    path =''
    limit = 10
    query = 'Mirror Selfie'
    sudreddit = 'selfie'
    sort = "top"

    # https://www.reddit.com/prefs/apps
    reddit = praw.Reddit(
        client_id="9N0uS0mqciwubQ",
        client_secret="Q2witqv5fhUSqbQonVGbsNkQn38",
        user_agent="jim_huav1",
        username="jim_hua",
        password="",
    )

    def __init__(self):
        print('go~~~')

    def search_img(self):
        urls = []
        data = 0
        max_search = 0
        subreddits = self.reddit.subreddit(self.sudreddit)
        hot_python = subreddits.search(query=self.query,limit=self.limit,sort=self.sort)

        for i in hot_python:
            max_search = max_search + 1
            if os.path.splitext(i.url)[-1] != '' and os.path.splitext(i.url)[-1] == ('.jpg' or '.png' or '.jprg'):
                # print(os.path.splitext(i.url)[-1])
                data = data + 1
                urls.append(i.url)
        self.data = data
        self.max_search = max_search
        self.urls = urls
        

    def wirte_img(self):

        if not os.path.isdir(self.path + self.query + '_' + self.sudreddit):
            os.mkdir(self.path + self.query + '_' + self.sudreddit)
        for url in self.urls:
            r = requests.get(url)
            with open(self.path + self.query + '_' + self.sudreddit + '/%s' %os.path.split(url)[-1], 'wb') as f:
                print(f.name)
                f.write(r.content)
        print('search: %s/%s'%(self.data, self.max_search))

def main():
    program = reddit_img_search()
    program.search_img()
    program.wirte_img()

if __name__=='__main__':
    main()


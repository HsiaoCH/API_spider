
import praw
import os
import requests
import cv2
import numpy as np
import argparse

class reddit_img_search:

    parser = argparse.ArgumentParser()
    parser.add_argument("--path","-p", required = False, default = ".", help = "save where?")
    parser.add_argument("--sudreddit","-s", required = False, default = "all")
    parser.add_argument("--query","-q", required = False, default = "tree")
    parser.add_argument("--limit","-l", required = False, default = 1000, help = "search limit")
    parser.add_argument("--sort", required = False, default = "top", help = "relevance, top, new, comments")
    args = parser.parse_args()

    path = args.path
    sudreddit = args.sudreddit
    query = args.query
    limit = args.limit
    sort = args.sort

    reddit = praw.Reddit("bot1")

    def __init__(self):
        print('go reddit img search')


    def search_img(self):
        urls = []
        data = 0
        max_search = 0
        subreddits = self.reddit.subreddit(self.sudreddit)
        hot_python = subreddits.search(query=self.query,limit=self.limit,sort=self.sort)

        for i in hot_python:
            max_search = max_search + 1
            link = os.path.splitext(i.url)[-1]
            if link == '.png' or link == '.jpg' or link == '.jpeg':
                # print(os.path.splitext(i.url)[-1])
                data = data + 1
                urls.append(i.url)
        self.data = data
        self.max_search = max_search
        self.urls = urls
        

    def wirte_img(self):
        if not os.path.isdir(self.path + '/reddit'):
            os.mkdir(self.path + '/reddit')
        path_all = self.path + '/reddit/' + self.query + '_' + self.sudreddit + '_' + self.sort
        if not os.path.isdir(path_all):
            os.mkdir(path_all)
        for url in self.urls:
            r = requests.get(url)
            with open(path_all + '/%s' %os.path.split(url)[-1], 'wb') as f:
                print(f.name)
                f.write(r.content)
        print('search: %s/%s'%(self.data, self.max_search))

def main():
    program = reddit_img_search()
    program.search_img()
    program.wirte_img()

if __name__=='__main__':
    main()


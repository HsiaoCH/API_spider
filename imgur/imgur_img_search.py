
from imgurpython import ImgurClient
from helpers import get_input, get_config
import argparse
import os
import requests

class imgur_img_search:

    parser = argparse.ArgumentParser()
    parser.add_argument("--path","-p", required = False, default = ".", help = "save where?")
    parser.add_argument("--query","-q", required = False, default = "box")
    args = parser.parse_args()

    path = args.path
    query = args.query
    
    def __init__(self):
        print('go imgur img search')


    def read_auth(self):
        config = get_config()
        config.read('auth.ini')
        client_id = config.get('credentials', 'client_id')
        client_secret = config.get('credentials', 'client_secret')
        client = ImgurClient(client_id, client_secret)
        self.searchs = (client.gallery_search(self.query))

    
    def save_urls(self):
        urls = []
        data = 0
        for search in self.searchs:
            # print(vars(search))
            try :
                imgs = search.images
                for img in imgs:
                    link = os.path.splitext(img['link'])[-1]
                    if link == '.png' or link == '.jpg' or link == '.jpeg':
                        data = data + 1
                        # print(link)
                        urls.append(img['link'])
            except AttributeError:
                continue
        self.urls = urls
        self.data = data


    def wirte_img(self):
        if not os.path.isdir(self.path + '/imgur'):
            os.mkdir(self.path + '/imgur')
        path_all = self.path + '/imgur/' + self.query 
        if not os.path.isdir(path_all):
            os.mkdir(path_all)
        for url in self.urls:
            r = requests.get(url)
            with open(path_all + '/%s' %os.path.split(url)[-1], 'wb') as f:
                print(f.name)
                f.write(r.content)
        print('search: %s'%(self.data))


def main():
    program = imgur_img_search()
    program.read_auth()
    program.save_urls()
    program.wirte_img()

if __name__=='__main__':
    main()

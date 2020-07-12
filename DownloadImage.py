#!venv/bin/python

import praw,requests,re

r = praw.Reddit("bot1")
subreddit = r.subreddit('subreddit_name')

posts = subreddit.hot(limit=10000)

for post in posts:
    url = (post.url)
    print(url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg"
    print(file_name)
    r = requests.get(url)
    with open('image/'+file_name,"wb") as f:
        f.write(r.content)

#!venv/bin/python
import praw
import re
import random


reddit = praw.Reddit('bot2')

user = reddit.user.me()

for comment in user.comments.new(limit=500): 
    try: 
        print(comment.body)
        comment.delete()
        print('*'*50)
    except: 
        print('Could not delete this comment.')
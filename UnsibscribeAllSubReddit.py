#!venv/bin/python
import praw
import re
import random

reddit = praw.Reddit('bot2')


comments = reddit.user.subreddits(limit=None)

for comment in comments: 
    try: 
        print(comment)
        comment.unsubscribe()
        print('#'*50)
    except: 
        print('could not post')
        continue
    
            

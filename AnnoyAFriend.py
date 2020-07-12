#!venv/bin/python
import praw
import re
import random

reddit = praw.Reddit('bot1')

redditor = reddit.redditor('Friend_Handle')

comments = redditor.comments.new(limit=50)

for comment in comments: 
    try: 
        marvin_reply = "Take this bruh - https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        comment.reply(marvin_reply)
        print(comment.body)
        print('#'*50)
    except: 
        print('could not post')
        continue
    
            

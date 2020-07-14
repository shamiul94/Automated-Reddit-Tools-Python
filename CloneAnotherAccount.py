#!venv/bin/python
import praw
import re
import random

# Authenticate as User 1
reddit1 = praw.Reddit('bot1')
subs1 = reddit1.user.subreddits(limit=None)

# Authenticate as User2
reddit2 = praw.Reddit('bot2')

for sub in subs1: 
    try: 
        print(sub)
        s = str(sub)
        reddit2.subreddit(s).subscribe()
        print('#'*50)
    except Exception as e: 
        print(e)
        print('could not post')
        continue
    
            

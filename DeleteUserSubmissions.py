#!venv/bin/python
import praw
import re
import random


reddit = praw.Reddit('bot1')

user = reddit.user.me()

for post in user.submissions.new(limit=500): 
    try: 
        ######### Uncomment this part if you don't want to delete certain submissions #########
        # if post.id == 'post_id_1' or post.id == 'post_id_2':  
        #     continue
        #######################################################################################
        print(post.title)
        post.delete()
        print('*'*50)
    except: 
        print('Could not delete this post!')

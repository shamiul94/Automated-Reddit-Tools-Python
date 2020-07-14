# Python-Reddit-Bot

As a Reddit user, I felt that creating some bots for some trivial jobs might be interesting. So, I started learning how to do that. Just some simple bots to do some simple jobs. I used the `PRAW` library to build them.

# Bots made till now
1. **Delete all comments of a user**
2. **Delete all submissions of a user**
3. **Download images from a subreddit**
4. **Annoy a friend** - Input your friends handle and the bot will reply to your friend's last 50 comments with a [Youtube link to Rick Astley's Never Gonna Give You Up](https://www.youtube.com/watch?v=dQw4w9WgXcQ) song. Let your friend know that you are always there for him.
5. **CloneAnotherAccount** - Let's say you have one ID but for some reasons, you need to delete this ID and shift to a newer one. But you love your current joined subreddits and it is too tiresome to subscribe to them one by one again. This is what this bot will do. It will log in as the first user in Reddit and gather all your joined subreddits. Then it will login as your new ID and it will subscribe to all the previous subreddits automatically. In a minute or so, you are good to go. Isn't it awesome? 
6. **DownloadImage** - Let's say you like a subreddit's pictures. You want to downolad them every morning to set them as your desktop's wallpaper. Set it as a cronjob on your PC and it will download newest and trending photos from that subreddit. 


This list will grow in future.

# How to run them
1. Install `praw`.
```
pip install praw
```

2. Modify `praw.ini` file as mentioned in [this blog](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) and save it in the same folder as the python codes.

3. Then just run this command from terminal.

```
python3 botname.py
```
And it will start it's job. 


# Source 
I would not be able to build these bots without reading [this blog](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) written by [Shantnu](https://github.com/shantnu). Thanks to him.
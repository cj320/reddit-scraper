#!/usr/bin/python3
from reddit_pkg import get_content as content
while True:
    sub = input("Please enter the name of a subreddit: ")
    if content.val_subreddit(sub):
        break
content.get_images(sub)
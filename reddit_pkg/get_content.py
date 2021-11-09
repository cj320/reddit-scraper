#!/usr/bin/python3
import praw
import json
import re
from prawcore.exceptions import ResponseException 
import requests
import shutil
import os
import pandas
import datetime

def creds():
    global reddit
    credentials = '.secrets.json'
    with open(credentials, 'r') as f:
        creds = json.load(f)
        reddit = praw.Reddit(client_id=creds['client_id'],
                    client_secret=creds['client_secret'],
                    user_agent=creds['user_agent'],
                    redirect_uri=creds['redirect_uri'],
                    refresh_token=creds['refresh_token'])   
    return reddit        

def val_subreddit(sub):
    creds()
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
        print(f"{sub.upper()} IS VALID")
        return sub
    except ResponseException:
        print("This subreddit does not exist, make sure the subreddit exists")


def get_stats(sub):
    creds()
    sub = reddit.subreddit(sub).hot(limit=100)
    stats = { "title":[],
                    "subreddit":[],
                    "score":[], 
                    "id":[], 
                    "url":[], 
                    "comms_num": [], 
                    "created": [], 
                    "body":[]}
    for post in sub:
        stats["title"].append(post.title)
        stats['subreddit'].append(post.subreddit)
        stats["score"].append(post.score)
        stats["id"].append(post.id)
        stats["url"].append(post.url)
        stats["comms_num"].append(post.num_comments)
        stats["created"].append(post.created)
        stats["body"].append(post.selftext)
    return stats

def get_images(sub):
    creds()
    REGEX = r"(http|https)://.*/.*.(jpg|png|jpeg|tiff|raw|gif$)"
    submission = reddit.subreddit(sub).hot(limit=10)
    path = 'images/' + sub

    for post in submission: 
        url = post.url
        if re.search(REGEX, url):
            if not os.path.isdir(path):
                os.makedirs(path)
                
            filename = url.split("/")[-1]
            complete_name = os.path.join(path, filename)
            if os.path.exists(complete_name):
                print(f"{complete_name} exists")
                continue
            else:
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(complete_name, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
            
                    print(f"Image downloaded successfully {filename}")
                else:
                    print("Image couldn't be retrieved")
        else:
            print(f"{url} is not a valid image in {sub} subreddit.")
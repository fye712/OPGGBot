import praw
import pdb
import re
import os
from config_bot import *



user_agent = ("Python OPGG Bot 0.1 (by /u/franklindaking)")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit("summonerschool")
for submission in subreddit.get_hot(limit = 50):
    if submission.id not in posts_replied_to:
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            for match in re.finditer('<(.*?)>'):



import praw
import pdb
import re
import os
import time
from config_bot import *

def handle_ratelimit(func, *args, **kwargs):
    while True:
        try:
            func(*args, **kwargs)
            break
        except reddit.errors.RateLimitExceeded as error:
            print '\tSleeping for %d seconds' % error.sleep_time
            time.sleep(error.sleep_time)
def bot():
    user_agent = ("Python OPGG Linker 0.1 (by /u/franklindaking)")
    r = praw.Reddit(user_agent = user_agent)
    r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = filter(None, posts_replied_to)

    subreddit = r.get_subreddit("test")

    flat_comments = praw.helpers.flatten_tree(subreddit.get_comments())
    for comment in flat_comments:
        if comment.id not in posts_replied_to:
            for match in re.findall('<(.*?)>', comment.body):
                # build the response?
                response = "[" + match + "](http://na.op.gg/summoner/userName=" + match + ")"
                handle_ratelimit(comment.reply, response)
                print "Bot replying to : " + comment.id
                posts_replied_to.append(comment.id)

    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

while True:
    bot()




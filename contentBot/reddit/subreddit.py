from rich.console import Console
from contentBot.utils.console import print_markdown, print_step, print_substep
from dotenv import load_dotenv
from random import choices
console = Console()
import os, random, praw, re
import better_profanity
import time
import datetime
import profanity_check 

f_path = f"contentBot/reddit/censorship.txt"

def get_subreddit_threads(subreddits: list, subreddits_weight: list):
    global submission
    """
    Returns a list of threads from the AskReddit subreddit.
    """

    load_dotenv()

    if os.getenv("REDDIT_2FA", default="no").casefold() == "yes":
        print(
            "\nEnter your two-factor authentication code from your authenticator app.\n"
        )
        code = input("> ")
        print()
        pw = os.getenv("REDDIT_PASSWORD")
        passkey = f"{pw}:{code}"
    else:
        passkey = os.getenv("REDDIT_PASSWORD")

    content = {}
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="Accessing AskReddit threads",
        username=os.getenv("REDDIT_USERNAME"),
        password=passkey,
    )        

    # example: subreddits = ["AskReddit"]
    the_sub = choices(subreddits, weights = subreddits_weight, k = 1)
    subreddit_choice = the_sub[0]

    subreddit = reddit.subreddit(subreddit_choice)

    # YOU CAN CHOOSE "top" or "hot"!!!!
    # subreddit.top limit HAS MAXIMUM VALUE OF 988
    threads = subreddit.top(limit=988)

    # subreddit thread index HAS MAXIMUM VALUE OF 987
    submission = list(threads)[random.randint(0, 987)]

    # ALSO!
    # the user can spesify precise reddit thread via link:
    #submission = reddit.submission(url="https://www.reddit.com/r/TrueOffMyChest/comments/ywngq9/im_a_chronic_cheater/")

    while submission.over_18 or len(submission.selftext) > 0 or better_profanity.profanity.contains_profanity(submission.title) or better_profanity.profanity.contains_profanity(submission.selftext) or bool(profanity_check.predict([submission.title])[0]) or bool(profanity_check.predict([submission.selftext])[0]):
        current_time = datetime.datetime.now()
        file = open(f_path, "a+")
        file.write(f"\n{current_time}: post skipped (subreddit.py filters)\n\n")
        file.write(f"{current_time}: skipped post due to better_profanity (jcbrock)\n") 
        file.write(f"{current_time}: title profanity was: {better_profanity.profanity.contains_profanity(submission.title)}\n")
        file.write(f"{current_time}: thread profanity was: {better_profanity.profanity.contains_profanity(submission.selftext)}\n")
        file.write(f"{current_time}: skipped post due to profanity_check (vzhou)\n")
        file.write(f"{current_time}: title profanity was: {bool(profanity_check.predict([submission.title])[0])}\n")
        file.write(f"{current_time}: thread profanity was: {bool(profanity_check.predict([submission.selftext])[0])}\n")        
        file.close()
        threads = subreddit.top(limit=988)
        submission = list(threads)[random.randint(0, 987)]


    print_substep(f"Video will be: {submission.title}")
    console.log("Getting video comments...")

    content["thread_url"] = submission.url
    content["thread_title"] = submission.title
    content["thread_post"] = submission.selftext
    content["comments"] = []

    try:
        for top_level_comment in submission.comments:

            if better_profanity.profanity.contains_profanity(top_level_comment.body):
                current_time = datetime.datetime.now()
                file = open(f_path, "a+")
                file.write(f"{current_time}: comment skipped due to better_profanity\n")
                file.close()
                continue

            if bool(profanity_check.predict([top_level_comment.body])[0]):
                current_time = datetime.datetime.now()
                file = open(f_path, "a+")
                file.write(f"{current_time}: comment skipped due to check_profanity\n")
                file.close()
                continue

            if len(top_level_comment.body) >= 550 or top_level_comment.body == "[deleted]" or top_level_comment.body == "[removed]":
                current_time = datetime.datetime.now()
                file = open(f_path, "a+")
                file.write(f"{current_time}: comment skipped due to other\n")
                file.close()
                continue
            
            if not top_level_comment.stickied:
                content["comments"].append(
                    {
                        "comment_body": top_level_comment.body,
                        "comment_url": top_level_comment.permalink,
                        "comment_id": top_level_comment.id,
                    }
                )

    except AttributeError as e:
        pass

    print_substep("Received AskReddit threads successfully.", style="bold green")

    if len(content["comments"]) == 0: 
        raise ValueError("no comments")

    return content

"""
Title: Reddit Functions
Author: John Mock
Description: Scrapes listings from the subreddits and creates embed structures
"""
import praw
import discord
import structures as dt

INFO = dt.get_r_info()

REDDIT_LINK = 'https://www.reddit.com'

REDDIT = praw.Reddit(client_id=INFO.get('reddit_id'),
                     client_secret=INFO.get('reddit_sec'),
                     user_agent=INFO.get('reddit_ua'))


def get_net_sec():
    """ embed creation """
    local_dict = {}
    recent_sub = REDDIT.subreddit('netsec').hot(limit=10)
    for sub_ids in recent_sub:
        submission = REDDIT.submission(id=sub_ids)
        local_dict[str(sub_ids)] = [submission.title, submission.url,
                                    REDDIT_LINK + submission.permalink,
                                    str(submission.author)]
    return local_dict


def get_live_overflow():
    """ LiveOverflow subreddit scraping """
    local_dict = {}
    recent_sub = REDDIT.subreddit('liveoverflow').new(limit=10)
    for sub_ids in recent_sub:
        submission = REDDIT.submission(id=sub_ids)
        local_dict[str(sub_ids)] = [submission.title, submission.url,
                                    REDDIT_LINK + submission.permalink,
                                    str(submission.author)]
    return local_dict


def create_embeds(news_keys):
    """ Netsec subreddit scraping """
    embed_list = []
    for key in news_keys.keys():
        items = news_keys.get(key)
        embed = discord.embeds.Embed()
        embed.title = items[0]
        embed.url = items[1]
        embed.add_field(name='Author', value=items[3])
        embed.add_field(name='thread link', value=items[2])
        embed.add_field(name='news_id', value=key)
        embed_list.append(embed)
    return embed_list

# Connect to DB
# Retrieve submission_id
# Compare submission_id

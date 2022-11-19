# reddit-scraper-for-discord
Project has reached EOL due to unsupported API by Discord Inc.


## Discord Channel
The current discord channel used for debugging the bot is https://discord.gg/zUf4NbH

## Current Requirements To Run/Recreate
1. Libraries to install:
   1. Discord.py
     - pip install discord.py
   2. Python Reddit API Wrapper
     - pip install praw
   3. PyMongo MongoDB driver
     - pip install pymongo
2. Create a folder called data in the directory the other folders are saved
3. Create 3 text files
    1. rinfo.txt
    2. cinfo.txt
    3. dinfo.txt
4. Insert the following data into dinfo.txt
  - disc_id,<discord_bot_id>
  - disc_secret,<discord_bot_secret>
  - disc_token,<discord_bot_token>
  - netsec_id,<discord_channel_id>
  - liveoverflow_id, <discord_channel_id>
5. Insert the following data into cinfo.txt
  - mongodbstring,<your_mongodb_connetion_string>
  - <db_username>,<db_password>
6. Insert the following data into rinfo
  - reddit_id,<reddit_id>
  - reddit_sec,<reddit_secret>
  - reddit_ua,<reddit_useragent> (Typically "AppName by /u/<reddit_username>
  
## How The Bot Works
1. disc_bot.py runs two background loops using the Discord.py wrapper.
2. The loops request embeds in order to post to the respective channels.
3. reddit_func.py gets utilized by making an API call through the praw wrapper checking the desired subreddits.
4. reddit_func.py received listings from each subreddit and passes the listings as an argument into the create_embeds() method.
5. the method creates an Embed structure for the Discord.py wrapper and sends back the embeds to the loop.
6. the loop currently waits 60 seconds before re-performing the above steps.

## Future Features
- Fully Automated
- No need for 'Current Requirements'
- MongoDB
- Credentials Encrypted
- Dockerized

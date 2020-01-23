"""
Title: Discord Bot
Author: John Mock
Description: Backbone code logic for discord bot
"""

import asyncio

import discord
from discord.ext import commands

import reddit as rf
import structures as dt

INFO = dt.get_d_info()
CLIENT = discord.Client()
BOT = commands.Bot(command_prefix='!')
TOKEN = INFO.get('disc_token')


class DiscClient(discord.Client):
    """ Discord Bot Backbone """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.post_net_sec())

    async def on_ready(self):
        """ Identifies bot and notifies that it's logic ready """
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def post_net_sec(self):
        """ Post net sec listings to net sec discord channel """
        await self.wait_until_ready()
        while not self.is_closed():
            embeds = rf.create_embeds(rf.get_net_sec())
            channel = self.get_channel(INFO.get('netsec_id'))
            for embed in embeds:
                try:
                    await channel.send(embed=embed)
                except:
                    pass
                    print('Cross post')
            await asyncio.sleep(5)

    async def post_live_overflow(self):
        """ Post liveoverflow listings to liveoverflow discord channel """
        await self.wait_until_ready()
        while not self.is_closed():
            embeds = rf.create_embeds(rf.get_live_overflow())
            channel = self.get_channel(INFO.get('liveoverflow_id'))
            for embed in embeds:
                try:
                    await channel.send(embed=embed)
                except:
                    pass
                    print('Cross post')
            await asyncio.sleep(60)


def __main__():
    bot = DiscClient()
    bot.run(TOKEN)


if __name__ == '__main__':
    __main__()

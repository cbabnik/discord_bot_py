import discord
from discord import Client, Intents
from auth import LOGIN_TOKEN
from config import BOT_NAME, HIDDEN, GUILD_ID
import logging

class MyClient(Client):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        Client.__init__(self, intents=intents)

    def run(self):
        handler = logging.FileHandler(filename='discordpy.log', encoding='utf-8', mode='w')
        Client.run(self, LOGIN_TOKEN, log_handler=handler, log_level=logging.DEBUG)

    async def on_ready(self):
        print(f"Logged on as {self.user}")
        if (HIDDEN):
            await self.change_presence(status=discord.Status.invisible)
        else:
            await self.change_presence(status=discord.Status.dnd, activity=discord.Game("dead"))

        if self.user.name != BOT_NAME:
            await self.user.edit(username=BOT_NAME)
        guild = self.get_guild(GUILD_ID)
        member = guild.get_member(533749978955513856)
        if member.nick != BOT_NAME:
            await member.edit(nick=BOT_NAME)
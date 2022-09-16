import discord
from discord import Client, Intents
from auth import LOGIN_TOKEN
from config import BOT_NAME
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
        await self.change_presence(status=discord.Status.dnd, activity=discord.Game("dead"))
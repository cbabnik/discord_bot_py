from discord import Client, Intents
from auth import LOGIN_TOKEN
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

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
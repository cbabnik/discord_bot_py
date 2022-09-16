import discord
from action import Action
import config

class Actor():
    def __init__(self, client:discord.Client):
        self.client = client

    async def act(self, action:Action):
        if (action.msg.channel):
            await action.msg.channel.send(action.statement)
        else:
            await self.main_channel.send(action.statement)
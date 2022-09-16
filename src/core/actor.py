import discord

class Actor():
    client:discord.Client  = None

    def __init__(self, client):
        self.client = client

    async def act(self, msg:discord.Message):
        await msg.channel.send(content="I'm dead, ok?")
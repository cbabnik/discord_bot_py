import asyncio
import sys
if len(sys.argv) <= 1 or sys.argv[1] not in ["alpha", "beta"]:
    print("""Specify a mode to run in:
  alpha - responding to BotTesting server only
  beta - responding to BigBuckHunters server""")
    sys.exit(1)


from client import MyClient as Client
from dispatcher import Dispatcher
from actor import Actor
client = Client()
actor = Actor(client)
dispatcher = Dispatcher(actor)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await dispatcher.processMessage(message)


dispatcher.registerCommand(r"\-mslots")

client.run() # dead end
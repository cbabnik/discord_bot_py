import asyncio
import sys
if len(sys.argv) <= 1 or sys.argv[1] not in ["alpha", "beta"]:
    print("""Specify a mode to run in:
  alpha - responding to BotTesting server only
  beta - responding to BigBuckHunters server""")
    sys.exit(1)


from client import MyClient as Client
from dispatch import Dispatcher
from actor import Actor
client = Client()
actor = Actor(client)
dispatcher = Dispatcher(actor)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await dispatcher.processMessage(message)


# temp inline commands
from command import Command
from action import Action
def say(contents, msg):
    print(contents)
    return Action(statement=contents)
dispatcher.registerCommand(Command(pattern=r"\-?say (.+)", cb=say))

client.run() # dead end
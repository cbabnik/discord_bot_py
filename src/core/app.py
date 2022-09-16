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


@client.hybrid_command(name="secret-cow-level")
async def hybrid(ctx):
    await ctx.send("moo!")

@client.hybrid_command(name="balance")
async def balance(ctx):
    await ctx.send("Could this be a reset?")


# temp inline commands
from command import Command
from action import Action
def say(contents, msg):
    return Action(statement=contents)
dispatcher.registerCommand(Command(pattern=r"\-?say (.+)", cb=say))
def help(msg):
    return Action(statement="No one will help you now")
dispatcher.registerCommand(Command(pattern=r"\-?help", cb=help))

client.run() # dead end
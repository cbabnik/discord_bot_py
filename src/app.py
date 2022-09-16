from client import MyClient as Client
import sys

if len(sys.argv) <= 1:
    print("""Specify a mode to run in:
  alpha - responding to BotTesting server only
  beta - responding to BigBuckHunters server""")
    sys.exit(1)

client = Client()
client.run()
from ssl import CHANNEL_BINDING_TYPES
import sys

BOT_NAME = "BuckBotPy"
CHANNEL_ID = 533736401225908224
HIDDEN = False

if (sys.argv[1] == "beta"):
    CHANNEL_ID = 265430059010097162

if ("hidden" in sys.argv):
    HIDDEN = True
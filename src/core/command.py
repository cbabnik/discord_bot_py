import re
from discord import Message, ChannelType
from action import Action
import config

class Command:
    def __init__(self, *, pattern, cb, enabled=True, auth=None, private_ok=False):
        self.pattern = pattern
        self.cb = cb
        self.enabled = enabled
        self.auth = auth
        self.private_ok = private_ok

    def execute(self, msg:Message):
        if self.enabled == False:
            return 
        if config.MODE == "alpha" and msg.channel.id != config.CHANNEL_ID:
            return
        if config.MODE != "alpha" and msg.channel.id == config.ALPHA_CHANNEL_ID:
            return
        issue = self.sanity(msg)
        if issue:
            print(issue)
            return issue
        params = self.parse_params(msg)
        action = self.cb(*params, msg=msg)
        return action

    def sanity(self, msg:Message):
        if msg.channel.type == ChannelType.private:
            if not self.private_ok:
                return Action(statement="This has to be in done in a public channel")
        elif msg.channel.type != ChannelType.text:
            return Action(statement="This type of channel is not supported for commands")
        return None

    def parse_params(self, msg:Message):
        match = re.match(self.pattern, msg.content, re.DOTALL+re.MULTILINE)
        if not match:
            raise Exception("Tried to execute command with unmatching message")
        return match.groups()

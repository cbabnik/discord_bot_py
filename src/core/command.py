import re
from discord import Message, ChannelType
from action import Action
import config

class Command:
    def __init__(self, *, pattern, cb, enabled=True, auth=None, private_ok=False, slash=True):
        self.pattern = pattern
        self.cb = cb
        self.enabled = enabled
        self.auth = auth
        self.private_ok = private_ok
        self.slash=slash

    def execute(self, msg:Message):
        if not self.sanity_quiet(msg):
            return None
        issue = self.sanity_loud(msg)
        if issue:
            return issue
        params = self.parse_params(msg)
        action = self.cb(*params, msg=msg)
        return action

    def sanity_quiet(self, msg:Message):
        if self.enabled == False:
            return False
        if config.MODE == "alpha" and msg.channel.id != config.CHANNEL_ID:
            return False
        if config.MODE != "alpha" and msg.channel.id == config.ALPHA_CHANNEL_ID:
            return False
        return True

    def sanity_loud(self, msg:Message):
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

from scan import Scanner

class Dispatcher:
    scanner = Scanner()
    commands = {}
    actor = None

    def __init__(self, actor):
        self.actor = actor

    def registerComponent(self, component):
        pass

    def registerCommand(self, command):
        cmd_id = len(self.commands)
        self.commands[cmd_id] = command
        self.scanner.addCmd(command, cmd_id)

    async def processMessage(self, msg):
        print(f"processing {msg}")
        cmd_id = self.scanner.scan(msg.content)
        print(f"matches {msg}")
        if cmd_id is not None:
            await self.dispatch(msg, None)

    async def dispatch(self, command, params):
        await self.actor.act(command)
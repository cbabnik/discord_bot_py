from scan import Scanner

class Dispatcher:
    def __init__(self, actor):
        self.actor = actor
        self.scanner = Scanner()
        self.commands = {}

    def registerCommand(self, command):
        cmd_id = len(self.commands)
        self.commands[cmd_id] = command
        self.scanner.addCmd(command.pattern, cmd_id)

    async def processMessage(self, msg):
        cmd_id = self.scanner.scan(msg.content)
        if cmd_id is None:
            return
        cmd = self.commands[cmd_id]
        if cmd_id is not None:
            await self.dispatch(cmd, msg)

    async def dispatch(self, cmd, msg):
        action = cmd.execute(msg)
        action.msg = msg
        await self.actor.act(action)
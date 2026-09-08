class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, action, application, function):
        self.commands[(action, application)] = function

    def execute(self, action, application):
        command = self.commands.get((action, application))

        if command is None:
            return None

        return command()
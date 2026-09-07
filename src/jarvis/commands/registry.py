class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name, function):
        self.commands[name] = function

    def execute(self, name):
        command = self.commands.get(name)

        if command is None:
            return False

        command()
        return True
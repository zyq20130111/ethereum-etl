class CompositeCommand:
    def __init__(self, commands):
        self.commands = commands

    def execute(self, input_iterable):
        chained_iterable = input_iterable
        for command in self.commands:
            chained_iterable = command.execute(chained_iterable)
        return chained_iterable

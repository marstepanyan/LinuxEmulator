class Command:
    def __init__(self, name, arguments=None, options=None):
        self.name = name
        self.arguments = arguments if arguments else []
        self.options = options if options else []

    def get_name(self):
        return self.name

    def get_args(self):
        return self.arguments

    def get_options(self):
        return self.options


def command_parser(command):
    parts = command.split()
    name = parts[0]
    arguments = []
    options = []
    for part in parts[1:]:
        if part.startswith('-'):
            options.append(part)
        else:
            arguments.append(part)
    if not arguments:
        arguments.append(None)

    return Command(name, arguments, options)

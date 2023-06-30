from FileSystem import FileSystem
from Command import Command, command_parser


class LinuxEmulator:
    def __init__(self):
        self.file_system = FileSystem()

    def run(self):
        while True:
            command = input("> ")
            output = self.execute_command(command_parser(command))
            print(output)

    def execute_command(self, command: Command):
        if command.get_name() == 'pwd':
            return self.file_system.pwd()

        elif command.get_name() == 'cd':
            return self.file_system.cd(command.get_args()[0])

        elif command.get_name() == 'ls':
            for arg in command.get_args():
                return self.file_system.ls(arg)

        elif command.get_name() == 'mkdir':
            for arg in command.get_args():
                return self.file_system.mkdir(arg)

        elif command.get_name() == 'touch':
            for arg in command.get_args():
                return self.file_system.touch(arg)

        elif command.get_name() == 'rm':
            for arg in command.get_args():
                return self.file_system.rm(arg)

        elif command.get_name() == 'cat':
            for arg in command.get_args():
                return self.file_system.cat(arg)

        elif command.get_name() == 'cp':
            for arg in command.get_args()[:-1]:
                return self.file_system.cp(arg, command.get_args()[-1])

        elif command.get_name() == 'mv':
            for arg in command.get_args()[:-1]:
                return self.file_system.mv(arg, command.get_args()[-1])

        elif command.get_name() == 'less':
            for arg in command.get_args():
                return self.file_system.less(arg)

        elif command.get_name() == 'prc':
            self.file_system.take_snapshot()

        else:
            return "Unknown command."

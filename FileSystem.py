from FileAndDirectory import Directory, File
import os
import copy


class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current_directory = self.root
        self.snapshots = []

    def pwd(self):
        path_components = []
        current_dir = self.current_directory

        while current_dir != self.root:
            path_components.insert(0, current_dir.get_name())
            current_dir = current_dir.parent

        path_components.insert(0, '/root')  # Add the root directory
        return '/'.join(path_components)

    def cd(self, path):
        if not path:
            self.current_directory = self.root
            return ''
        elif path == '..':
            if self.current_directory != self.root:
                self.current_directory = self.current_directory.parent
            return ''
        elif path == '.':
            return ''  # No change in the current directory

        elif not path.startswith('/'):
            path = os.path.join(self.root.get_name(), path)
        dirs = path.split('/')
        current_dir = self.current_directory
        for directory in dirs:
            if directory:
                current_dir = current_dir.get_subdirectory(directory)
                if not current_dir:
                    return f"Directory {directory} not found."
        self.current_directory = current_dir
        return ''

    def ls(self, directory_name):
        if directory_name:
            current_dir = directory_name
        else:
            current_dir = self.current_directory

        subdirectories = current_dir.get_subdirectories()
        files = current_dir.get_files()
        print("Subdirectories:")
        for subdir in subdirectories:
            print(subdir.get_name())
        print("Files:")
        for file in files:
            print(file.get_name())
        return f"Subdirectories and Files in {current_dir}"

    def mkdir(self, directory_name):
        self.current_directory.create_subdirectory(directory_name)
        return f"Directory {directory_name} created."

    def touch(self, file_name):
        self.current_directory.create_file(file_name)
        return f"File {file_name} created."

    def rm(self, path):
        parent_dir, name = os.path.split(path)
        parent = self._navigate_directory(parent_dir)
        if parent:
            if parent in self.current_directory.get_subdirectories():
                # if isinstance(parent, Directory):
                parent.delete_subdirectory(name)
            else:
                parent.delete_file(name)
        else:
            return f"Path {path} not found."
        return f"File {path} is removed."

    def cat(self, file_path):
        content = self._read_file(file_path)
        return content

    def vim(self, file_name):
        file = self.current_directory.get_file(file_name)
        if isinstance(file, File):
            print(f"Opening {file.get_name()} in vim. Editing mode activated...")
            print(f"Old content:\n{file.get_content()}")
            new_content = input("Enter your changes:\n")
            file.update_content(new_content)
            return f"{file.get_name()} saved."
        else:
            return f"File {file_name} not found."

    def cp(self, source_path, destination_path):
        content = self._read_file(source_path)
        self._write_file(destination_path, content)
        return f"{source_path} is coped to {destination_path}"

    def mv(self, source_path, destination_path):
        content = self._read_file(source_path)
        self._write_file(destination_path, content)
        self.rm(source_path)
        return f"{source_path} is moved to {destination_path}"

    def less(self, file_path):
        content = self._read_file(file_path)
        return content

    def _write_file(self, path, content):
        parent_dir, file_name = os.path.split(path)
        parent = self._navigate_directory(parent_dir)
        if parent:
            if isinstance(parent, Directory):
                parent.create_file(file_name)
                file = parent.get_file(file_name)
                file.update_content(content)
            else:
                return f"Path {path} is not a directory."
        else:
            return f"Directory {parent_dir} not found."

    def _read_file(self, path):
        parent_dir, file_name = os.path.split(path)
        print(parent_dir, file_name)
        if parent_dir:
            parent = self._navigate_directory(parent_dir)
            file = parent.get_file(file_name)
        else:
            file = self.current_directory.get_file(file_name)
        if file:
            return file.get_content()
        else:
            return f"File {file_name} not found."

    def _navigate_directory(self, path):
        if not path.startswith("/"):
            path = os.path.join(self.root.get_name(), path)
        dirs = path.split("/")
        current_dir = self.root
        for directory in dirs:
            if directory:
                current_dir = current_dir.get_subdirectory(directory)
                if not current_dir:
                    return f"Directory {directory} not found."
        return current_dir

    def take_snapshot(self):
        snapshot = copy.deepcopy(self.root)
        self.snapshots.append(snapshot)

    def get_snapshots(self):
        return self.snapshots

    def restore_snapshot(self, index):
        if 0 <= index < len(self.snapshots):
            self.root = copy.deepcopy(self.snapshots[index])
            self.current_directory = self.root
        else:
            return "Invalid snapshot index."

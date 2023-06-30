class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

    def get_name(self):
        return self.name

    def get_content(self):
        return self.content

    def update_content(self, content):
        self.content = content


class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []

    def get_name(self):
        return self.name

    def get_subdirectories(self):
        return self.subdirectories

    def get_files(self):
        return self.files

    def create_subdirectory(self, name):
        if self.get_subdirectory(name):
            raise ValueError(f"Directory {name} already exists.")
        subdirectory = Directory(name)
        subdirectory.parent = self
        self.subdirectories.append(subdirectory)

    def delete_subdirectory(self, name):
        subdirectory = self.get_subdirectory(name)
        if subdirectory:
            self.subdirectories.remove(subdirectory)
        else:
            raise ValueError(f"Directory {name} not found.")

    def get_subdirectory(self, name):
        for subdirectory in self.subdirectories:
            if subdirectory.get_name() == name:
                return subdirectory
        return None

    def create_file(self, name):
        if self.get_file(name):
            raise ValueError(f"File {name} already exists.")
        file = File(name)
        self.files.append(file)

    def delete_file(self, name):
        file = self.get_file(name)
        if file:
            self.files.remove(file)
        else:
            raise ValueError(f"File {name} not found.")

    def get_file(self, name):
        for file in self.files:
            if file.get_name() == name:
                return file
        return None

    def __repr__(self):
        return self.name

import os


class File:
    def __init__(self, path) -> None:
        self.path = path

    def typeOfFile(self) -> str:
        if os.path.isfile(self.path):
            result = "standard file"
        elif os.path.isdir(self.path):
            result = "dir"
        else:
            result = ""
        return result

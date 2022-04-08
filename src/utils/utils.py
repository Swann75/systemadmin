from pathlib import Path
import os


class Root:
    @staticmethod
    def get_project_root():
        return os.fspath(Path(os.path.dirname(__file__)).parent.parent)


if __name__ == "__main__":
    print(Root.get_project_root())

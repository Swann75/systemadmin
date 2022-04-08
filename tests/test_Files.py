from systemadmin.Files import File
from configparser import ConfigParser
from utils.utils import Root
import os


def test_typeOfFile():

    config = ConfigParser()
    config.read(os.path.join(Root.get_project_root(), "configfile.properties"))
    file1 = File(os.path.join(Root.get_project_root(), config["ressources"]["file1"]))
    file2 = File(os.path.join(Root.get_project_root(), config["ressources"]["file2"]))
    file3 = File(os.path.join(Root.get_project_root(), config["ressources"]["file3"]))

    assert File.typeOfFile(file1) == "standard file"
    assert file2.typeOfFile() == "dir"
    assert file3.typeOfFile() == ""

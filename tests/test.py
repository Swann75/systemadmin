from configparser import ConfigParser
import os
from pathlib import Path

config = ConfigParser()
config.read("/home/fitec/Documents/systemadmin/configfile.properties")
print("stop")

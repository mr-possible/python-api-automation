import configparser
import os

user_dir = os.path.pardir


def getConfig():
    config = configparser.ConfigParser()
    config.read(user_dir + os.sep + 'utils' + os.sep + 'properties.ini')
    return config

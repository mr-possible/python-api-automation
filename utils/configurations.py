import configparser
import logging
import os

user_dir = os.path.pardir


def getConfig():
    config = configparser.ConfigParser()
    filepath = os.getcwd() + os.sep + 'utils' + os.sep + 'properties.ini'
    config.read(filepath)
    logging.info(f'File [[{filepath}]] loaded !')
    return config

from configparser import ConfigParser


def read_ini_file(category, key):
    config = ConfigParser()
    config.read("../config.ini")
    return config.get(category, key)
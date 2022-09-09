import sys
from os.path import exists
import os


class PathService:
    @staticmethod
    def write_path_to_txt(path):
        with open("../Service/path.txt", "w", encoding="utf8") as f:
            f.write(path)

    @staticmethod
    def read_path_from_txt():
        if exists("../Service/path.txt"):
            with open("../Service/path.txt", "r", encoding="utf8") as f:
                return f.read()
        return None

    @staticmethod
    def create_folder(directory, directory_name):
        try:
            os.mkdir(os.path.join(directory, directory_name))
        except:
            return sys.exc_info()[0].__name__ + " occurred!"

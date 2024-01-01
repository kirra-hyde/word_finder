from utility import txt_to_list
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        self.path = path
        self.words = txt_to_list(path)
        print (f"{len(self.words)} words read")

    def __repr__(self):
        return f"<{self.__class__.__name__} path={self.path} words={self.words} >"

    def random(self):
        return choice(self.words)
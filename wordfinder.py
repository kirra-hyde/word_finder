from utility import txt_to_list
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> findy1 = WordFinder("words.txt")
    5 words read

    >>> findy2 = WordFinder("different_words.txt")
    5 words read

    >>> findy1
    <WordFinder path=words.txt words=['Each', 'Peach', 'Pear', 'Plum', 'Wahooooo!']>

    >>> findy2
    <WordFinder path=different_words.txt words=['carrots', 'kale', 'broccoli', 'pear', 'plum']>

    >>> findy1.random() in ['Each', 'Peach', 'Pear', 'Plum', 'Wahooooo!']
    True

    >>> findy1.random() in ['Each', 'Peach', 'Pear', 'Plum', 'Wahooooo!']
    True

    >>> findy1.random() in ['Each', 'Peach', 'Pear', 'Plum', 'Wahooooo!']
    True

    >>> findy1.random() in ['Each', 'Peach', 'Pear', 'Plum', 'Wahooooo!']
    True

    >>> findy2.random() in ['carrots', 'kale', 'broccoli', 'pear', 'plum']
    True

    >>> findy2.random() in ['carrots', 'kale', 'broccoli', 'pear', 'plum']
    True

    >>> findy2.random() in ['carrots', 'kale', 'broccoli', 'pear', 'plum']
    True

    >>> findy2.random() in ['carrots', 'kale', 'broccoli', 'pear', 'plum']
    True
    """

    def __init__(self, path):
        self.path = path
        self.words = txt_to_list(path)
        print (f"{len(self.words)} words read")

    def __repr__(self):
        return f"<{self.__class__.__name__} path={self.path} words={self.words}>"

    def random(self):
        return choice(self.words)
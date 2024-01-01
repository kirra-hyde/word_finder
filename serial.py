class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.curr = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} curr={self.curr}>"

    def generate(self):
        self.curr += 1
        return self.curr

    def reset(self):
        self.curr = self.start - 1

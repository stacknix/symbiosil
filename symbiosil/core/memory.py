import abc


class Memory(abc.ABC):

    def __init__(self, emotions: tuple):
        self.emotions = emotions

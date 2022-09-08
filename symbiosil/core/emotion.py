import abc
from enum import Enum


class Emotion(abc.ABC):

    def __init__(self, genre):
        self.genre = genre

    @abc.abstractmethod
    def on_sense(self, senses: tuple):
        pass

    # emit emotion when detected
    def emit(self, level, **kwargs):
        pass


class Genre(Enum):
    happy = 'happy'
    sad = 'sad'
    anger = 'anger'
    fear = 'fear'
    surprise = 'surprise'

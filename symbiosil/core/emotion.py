import abc
from enum import Enum


class Emotion(abc.ABC):

    def __init__(self, genre):
        self.genre = genre

    @abc.abstractmethod
    def on_emit(self, senses: tuple):
        pass


class Genre(Enum):
    happy = 'happy'
    sad = 'sad'
    anger = 'anger'
    fear = 'fear'
    surprise = 'surprise'

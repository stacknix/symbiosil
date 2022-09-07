import abc
from enum import Enum


class Emotion(abc.ABC):

    def __init__(self, genre):
        self.genre = genre


class Genre(Enum):
    happy = 'happy'
    sad = 'sad'
    anger = 'anger'
    fear = 'fear'

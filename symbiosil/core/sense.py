import abc
from enum import Enum


class SenseType(Enum):
    VISION = 'vision'
    HEARING = 'hearing'


class SenseEntity:

    def __init__(self, sense_type: SenseType, confidence_level: float, **kwargs):
        self.sense_type = sense_type
        self.confidence_level = confidence_level


class Sense(abc.ABC):

    def __init__(self, **kwargs):
        self._alive = False

    def begin(self, **kwargs):
        self._alive = True
        self.on_sense(**kwargs)
        self._alive = False

    @abc.abstractmethod
    def on_sense(self, **kwargs):
        pass

    def stop(self):
        self._alive = False

    def alive(self) -> bool:
        return self._alive

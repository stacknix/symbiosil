import abc
from enum import Enum


class SenseType(Enum):
    VISION = 'vision'
    HEARING = 'hearing'
    SPACE = 'space'
    ENERGY = 'energy'
    HEALTH = 'health'


class SenseEntity:

    def __init__(self, confidence_level: float, **kwargs):
        self.confidence_level = confidence_level


class Sense(abc.ABC):

    def __init__(self, sense_type: SenseType, **kwargs):
        self._sense_type = sense_type
        self._alive = False

    def begin(self, **kwargs):
        self._alive = True
        self.on_sense(**kwargs)
        self._alive = False

    @abc.abstractmethod
    def on_sense(self, **kwargs):
        pass

    def emit(self, entity):
        if self._sense_type == SenseType.VISION:
            print(f"I saw: {entity.text} and sure about it {round(entity.confidence_level, 2)}%")
        elif self._sense_type == SenseType.HEARING:
            print(f"I heard '{entity.text}' and sure about it {round(entity.confidence_level, 2)}%")
        else:
            print('unknown sense entity emitted!')

    def stop(self):
        self._alive = False

    def alive(self) -> bool:
        return self._alive

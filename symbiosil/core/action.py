import abc
from enum import Enum


class ActionType(Enum):
    VOICE = 'voice'
    WRITE = 'write'


class Action(abc.ABC):

    def __init__(self, action_type: ActionType, **kwargs):
        self.action_type = action_type

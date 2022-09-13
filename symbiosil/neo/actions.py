from symbiosil.core.action import Action, ActionType


class ActionWrite(Action):

    def __init__(self, **kwargs):
        super(ActionWrite, self).__init__(ActionType.WRITE, **kwargs)


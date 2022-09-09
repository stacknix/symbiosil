import abc


class Sense(abc.ABC):

    def __init__(self, **kwargs):
        self._alive = False

    @abc.abstractmethod
    def on_sense(self, **kwargs):
        pass

    def begin(self, **kwargs):
        self._alive = True
        self.on_sense(**kwargs)
        self._alive = False

    # emit sense when detected
    def emit(self, level, **kwargs):
        pass

    # stop sensing
    def stop(self):
        self._alive = False

    #
    def alive(self):
        return self._alive

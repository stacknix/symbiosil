import abc


class SenseProcessor(abc.ABC):

    @abc.abstractmethod
    def on_process(self, senses: list):
        pass

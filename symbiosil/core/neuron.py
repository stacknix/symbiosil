import abc


class Neuron(abc.ABC):

    # this method return action sense with ratio 0.0-1.0
    @abc.abstractmethod
    def on_match(self, senses: list):
        pass

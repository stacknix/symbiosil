import abc


class Living(abc.ABC):

    def __init__(self, **kwargs):
        self.registries = []
        self.on_registry()

    @abc.abstractmethod
    def on_registry(self):
        pass

    def register(self, registry):
        self.registries.append(registry)

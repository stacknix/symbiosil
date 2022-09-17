import abc


class Living(abc.ABC):

    def __init__(self, processor, **kwargs):
        self.processor = processor
        self.registries = []
        self.on_registry()

    @abc.abstractmethod
    def on_registry(self):
        pass

    def register(self, registry):
        self.registries.append(registry)

    def get_registries(self, registry_class):
        registry_classes = []
        for object_class in self.registries:
            if registry_class in type.mro(object_class):
                registry_classes.append(object_class)
        return registry_classes

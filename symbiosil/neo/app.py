from symbiosil.core.living import Living
from symbiosil.neo.actions import ActionWrite
from symbiosil.neo.senses import SimulatedVision, SimulatedHearing
from symbiosil.neo.processors import NeoSenseProcessor


class App(Living):

    def __init__(self, **kwargs):
        super(App, self).__init__(NeoSenseProcessor, **kwargs)

    def on_registry(self):
        self.register(SimulatedVision)
        self.register(SimulatedHearing)
        self.register(ActionWrite)

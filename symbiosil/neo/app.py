from symbiosil.core.living import Living
from symbiosil.neo.actions import ActionWrite
from symbiosil.neo.senses import SimulatedVision, SimulatedHearing


class App(Living):

    def on_registry(self):
        self.register(SimulatedVision)
        self.register(SimulatedHearing)
        self.register(ActionWrite)

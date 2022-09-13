from fuzzywuzzy import process
from symbiosil.core.neuron import Neuron
from symbiosil.neo.actions import ActionWrite

SAMPLE_CHOICES = ("Hi", "Hello")


class FuzzyNeuron(Neuron):

    def on_match(self, senses: list):
        sample = "hey there"
        choice, ratio = process.extractOne(sample, SAMPLE_CHOICES)
        if ratio != 0.0:
            action = ActionWrite()
            action.text = choice
            action.ratio = ratio
            return action
        return None

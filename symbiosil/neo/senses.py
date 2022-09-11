import random
import time

from symbiosil.core.sense import Sense, SenseType, SenseEntity

SIMPLE_HEARING_DATA = (
    "hi", "i don't like it", "coffee please", "thank you", "what time it is", "it's good", "i am not feeling well",
    "so everything on track", "what do you think", "can we skip today's meeting", "good evening", "I will try my best",
    "we can cancel", "ok got it", "next week", "let's have a quick demo tomorrow", "sounds good", "no issue",
)

SIMPLE_VISION_DATA = (
    'human', 'bird', 'animal', 'plant', 'book'
)


class SimulatedHearing(Sense):

    def __init__(self, **kwargs):
        super(SimulatedHearing, self).__init__(SenseType.HEARING, **kwargs)

    def on_sense(self, **kwargs):
        while self.alive():
            time.sleep(random.randint(2, 4))
            entity = SenseEntity(random.uniform(0.1, 1.0))
            entity.text = random.choice(SIMPLE_HEARING_DATA)
            self.emit(entity)


class SimulatedVision(Sense):

    def __init__(self, **kwargs):
        super(SimulatedVision, self).__init__(SenseType.VISION, **kwargs)

    def on_sense(self, **kwargs):
        while self.alive():
            time.sleep(random.randint(2, 4))
            entity = SenseEntity(random.uniform(0.1, 1.0))
            entity.text = random.choice(SIMPLE_VISION_DATA)
            self.emit(entity)

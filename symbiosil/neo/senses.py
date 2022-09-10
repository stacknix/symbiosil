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

    def on_sense(self, **kwargs):
        while self.alive():
            time.sleep(random.randint(2, 8))
            entity = SenseEntity(SenseType.HEARING, random.uniform(0.1, 1.0))
            entity.text = random.choice(SIMPLE_HEARING_DATA)
            yield entity


class SimulatedVision(Sense):

    def on_sense(self, **kwargs):
        while self.alive():
            time.sleep(random.randint(2, 8))
            entity = SenseEntity(SenseType.VISION, random.uniform(0.1, 1.0))
            entity.text = random.choice(SIMPLE_VISION_DATA)
            yield entity

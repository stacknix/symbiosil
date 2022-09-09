import random
import time

from symbiosil.core.sense import Sense

RAW = (
    "hi", "i don't like it", "coffee please", "thank you", "what time it is", "it's good", "i am not feeling well",
    "so everything on track", "what do you think", "can we skip today's meeting", "good evening", "I will try my best",
    "we can cancel", "ok got it", "next week", "let's have a quick demo tomorrow", "sounds good", "no issue",
)


class HearingSense(Sense):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_sense(self, **kwargs):
        while self.alive():
            text = random.choice(RAW)
            level = random.uniform(0.1, 1.0)
            self.emit(level, text=text)
            time.sleep(random.randint(2, 8))


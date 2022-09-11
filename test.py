import threading
from symbiosil.neo.senses import SimulatedVision, SimulatedHearing


def handle_vision(sense):
    sense.begin()


def handle_hearing(sense):
    sense.begin()


if __name__ == "__main__":
    t1 = threading.Thread(target=handle_vision, args=(SimulatedVision(),))
    t2 = threading.Thread(target=handle_hearing, args=(SimulatedHearing(),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")

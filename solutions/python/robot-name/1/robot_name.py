import random
import string


class Robot:
    active_names = set()
    historical_names = set()

    def __init__(self):
        self._name = ""

    @staticmethod
    def _generate_name():
        letters = "".join(random.choices(string.ascii_uppercase, k=2))
        digits = "".join(random.choices(string.digits, k=3))
        return letters + digits

    @property
    def name(self):
        if not self._name:
            while True:
                candidate = Robot._generate_name()

                if candidate not in Robot.historical_names:
                    Robot.historical_names.add(candidate)
                    Robot.active_names.add(candidate)
                    self._name = candidate
                    break

        return self._name

    def reset(self):
        if self._name:
            Robot.active_names.remove(self._name)
            self._name = ""
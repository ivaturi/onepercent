from string import ascii_uppercase as chars
from string import digits
import random

class Robot(object):
    _names = []
    name = ""

    def __init__(self):
        self.reset()
    
    def reset(self):
        while self.name == "" or self.name in Robot._names:
            self.name = self.generate_name()
        Robot._names.append(self.name)

    def generate_name(self):
        random.seed()
        return "".join(random.choices(chars, k = 2) + random.choices(digits, k = 3))

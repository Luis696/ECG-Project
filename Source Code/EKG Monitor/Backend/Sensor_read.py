from random import randint
import numpy as np
from GUI.updateGUI import TIMER
import time

class Sensor:
    def __init__(self, name_str):
        self.name = name_str

    def print_properties(self):
        print("Name:{name}".format(name=self.name))

    def read(self):
        y = randint(1, 100)
        return y




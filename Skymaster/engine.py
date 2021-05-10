import numpy as np

class Engine:
    def __init__(self, type_name:str, shaft_power = None, eta_prop=None, Cd0 = None):
        self.type_name = type_name
        self.shaft_power = shaft_power
        self.eta_prop = eta_prop
        self.Cd0 = Cd0

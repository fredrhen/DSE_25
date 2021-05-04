import numpy as np

class Engine:
    def __init__(self, type_name:str):
        self.type_name = type_name
        self.shaft_power = None
        self.eta_prop = None
        self.Cd0 = None
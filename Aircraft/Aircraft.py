import numpy as np
import json
import Engine

class Aircraft:
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.forward_engine = None
        self.rear_engine = None

    @classmethod
    def fromjsonfile(cls, json_file="aircraft_data.json"):
        """
        Creates an Aircraft class from a json file
        :param json_file: Json file
        :return: A new class with the json data
        """
        with open(json_file) as f:
            data_dict = json.load(f)
        return cls(data_dict)

    def add_forward_engine(self, engine:Engine):
        self.forward_engine = engine

    def add_rear_engine(self, engine:Engine):
        self.rear_engine = engine

    @staticmethod
    def comp_drag(velocity, Cd, surface_area, density=1.225):
        return .5 * velocity**2 * Cd * density * surface_area

    @staticmethod
    def comp_CD(CL, Cd_0, A, e):
        return Cd_0 + CL**2 / (np.pi * A * e)






if __name__ == '__main__':
    obj = Aircraft.fromjsonfile()
    print(obj.data_dict)
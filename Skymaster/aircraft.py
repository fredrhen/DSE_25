import numpy as np
import json
from Skymaster.engine import Engine

g_const = 9.80665

class Aircraft:

    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.forward_engine = None
        self.rear_engine = None

    @classmethod
    def fromjsonfile(cls, json_file="aircraft_data.json"):
        """
        Creates an Skymaster class from a json file
        :param json_file: Json file
        :return: A new class with the json data
        """
        with open(json_file) as f:
            data_dict = json.load(f)["Aircraft Details"]
        return cls(data_dict)

    def add_forward_engine(self, engine:Engine):
        self.forward_engine = engine

    def add_rear_engine(self, engine:Engine):
        self.rear_engine = engine

    def get_CD0(self, key):
        V = self.MPH_to_MS(float(self.data_dict[key]["speed"]))
        W = self.lbs_to_N(float(self.data_dict[key]["weight"]))
        p_set = float(self.data_dict[key]["power%"])
        rho = float(self.data_dict[key]["rho"])


        T = 0
        T += self.forward_engine.get_thrust(p_set, V, rho)
        T += self.rear_engine.get_thrust(p_set, V, rho)


        S = self.comp_S(float(self.data_dict["wingspan"]), float(self.data_dict['aspect ratio']))
        CL = self.comp_CL_EOM(W, rho, V, S)
        print(f'CL = {CL} ')
        CD = self.comp_CD_EOM(T, rho, V, S)
        print(f'CD = {CD} ')
        return self.comp_CD0(CL, float(self.data_dict["aspect ratio"]), float(self.data_dict['oswald efficiency']), CD)

    @staticmethod
    def comp_CD0(CL, A, e, CD):
        '''
        Computes the parasitic drag
        :param CL: Coefficient of lift
        :param A: Aspect Ratio
        :param e: Oswald Efficiency
        :param CD: Coefficient of Drag
        :return:Parasitic drag
        '''
        return CD - CL**2 / (np.pi*A*e)

    @staticmethod
    def comp_CL_EOM(W, rho, V, S):
        '''
        Computes the CL
        :param W: Weight [N]
        :param rho: Density [kg/m^3]
        :param V: Velocity [m/s]
        :param S: Surface area of wing [m^2]
        :return: Coefficient of Lift []
        '''
        return 2 * (W ) / (rho * V**2 * S)

    @staticmethod
    def comp_S(b, A):
        '''
        Computes the surface area
        :param b: wing span [m]
        :param A: Aspect Ratio []
        :return: [m^2]
        '''
        return b**2 / A

    @staticmethod
    def comp_drag(velocity, Cd, surface_area, rho=1.225):
        return .5 * velocity**2 * Cd * rho * surface_area

    @staticmethod
    def comp_CD_polar(CL, Cd_0, A, e):
        return Cd_0 + CL**2 / (np.pi * A * e)

    @staticmethod
    def comp_CD_EOM(T, rho, V, S):
        '''
        Computes the CD from the simplified equations of motion of steady straight flight with pitch ~ 0 deg
        :param T: Thrust [N]
        :param rho: density [kg/m^3]
        :param V: Velocity [m/s]
        :param S: Surface area of wing [m^2]
        :return: Coefficient of drag
        '''
        return 2*T / (rho * V**2 * S)

    @staticmethod
    def MPH_to_MS(MPH):
        return MPH * 0.44704

    @staticmethod
    def lbs_to_N(lbs):
        return lbs * 4.44822





if __name__ == '__main__':
    obj = Aircraft.fromjsonfile()
    obj.get_CD0('top speed 1')
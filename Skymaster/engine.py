import numpy as np

class Engine:
    def __init__(self, type_name:str, shaft_power = None, eta_prop=None, Cd0 = None):
        '''
        Init the engine class
        :param type_name: Name of the engine
        :param shaft_power: Shaft power of the engine [kW]
        :param eta_prop: Prop efficiency of the engine []
        :param Cd0: zero lift drag contribution of te engine []
        '''
        self.type_name = type_name
        self.shaft_power = shaft_power
        self.eta_prop = eta_prop
        self.Cd0 = Cd0

    def get_thrust(self, power_set, IAS, rho):
        '''
        Return the thrust at a specific velocity
        :param power_set: Power setting [] (0-1)
        :param velocity: TAS of the aircraft
        :return: Thrust of the engine [N]
        '''
        power_req = (self.shaft_power * 1000) * self.eta_prop * power_set
        return power_req / self.IAS_to_TAS(IAS, rho)

    @staticmethod
    def IAS_to_TAS(IAS, density):
        '''
        TAS to IAS conversion
        :param TAS: True airspeed [m/s]
        :param density: Airdensity [kg/m^3]
        :return: The Indicated Airspeed [m/s]
        '''
        return np.sqrt((1.225/density)*IAS**2)

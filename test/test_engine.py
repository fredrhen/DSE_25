import unittest
from Skymaster.aircraft import Engine

class Test_get_thrust(unittest.TestCase):
    def test_get_thrust(self):
        engine = Engine("test", shaft_power= 100, eta_prop=0.7)
        thrust = engine.get_thrust(0.5, 50, 1.1)

        # Hand computation result:
        thrust_hand = 663.32495

        self.assertAlmostEqual(thrust, thrust_hand, places=4)

class Test_IAS_to_TAS(unittest.TestCase):
    def test_get_thrust(self):
        IAS = 50
        rho = 1.1
        TAS = Engine.IAS_to_TAS(IAS, rho)
        # Hand computation result:
        TAS_hand = 52.76448

        self.assertAlmostEqual(TAS, TAS_hand, places=4)


if __name__ == '__main__':
    unittest.main()

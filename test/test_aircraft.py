import unittest
from Skymaster.aircraft import Aircraft
import os

class TestJson(unittest.TestCase):
    def test_readjson(self):
        """
        Test that the loading works
        """
        this_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(this_folder, "aircraft_data_test.json")
        obj = Aircraft.fromjsonfile(file_path)
        self.assertEqual(obj.data_dict, { "aspect ratio": "7.18", "wingspan": "11.63", "dihedral": "3",
    "oswald efficiency": "0.8", "top speed 1": {"weight": "4630","speed" : "199"},
    "top speed 2": {"weight": "4200", "speed" : "200"}})

class Test_comp_CD0(unittest.TestCase):
    def test_comp_CDO(self):
        """
        Testing the computation of CDO in the comp_CDO function
        """
        A = 8
        CL = 1
        e = 0.8
        CD = 0.4
        # Got value from a hand computation
        self.assertAlmostEqual(Aircraft.comp_CD0(CL, A, e, CD), 0.3503, places=4)

class Test_comp_CL_EOM(unittest.TestCase):
    def test_comp_CL_EOM(self):
        """
        Testing the computation of CL in the comp_CL_EOM function
        """
        Weight = 1000 # N
        rho = 1.04
        V = 50
        S = 10

        CL = 0.076923
        # Got value from a hand computation
        self.assertAlmostEqual(Aircraft.comp_CL_EOM(Weight, rho, V, S), CL, places=4)

class Test_comp_CD_polar(unittest.TestCase):
    def test_comp_CD_polar(self):
        """
        Testing the computation of CD in the comp_CD_polar function
        """
        A = 8
        CL = 1
        e = 0.8
        CD_0 = 0.03

        CD = 0.0797359
        # Got value from a hand computation
        self.assertAlmostEqual(Aircraft.comp_CD_polar(CL, CD_0, A, e), CD, places=4)

class Test_comp_CD_EOM(unittest.TestCase):
    def test_comp_CD_EOM(self):
        """
        Testing the computation of CD in the comp_CD_EOM function
        """
        thrust = 100
        rho = 1.04
        V = 50
        S = 10

        CD = 0.0076923
        # Got value from a hand computation
        self.assertAlmostEqual(Aircraft.comp_CD_EOM(thrust, rho, V, S), CD, places=4)



if __name__ == '__main__':
    unittest.main()

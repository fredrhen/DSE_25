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
        self.assertEqual(obj.data_dict, {'Aircarft Details': {'Aspect Ratio': '7.18 []', 'Wingspan': '11.63 [m]', 'Dihedral': '3 [deg]'}})


if __name__ == '__main__':
    unittest.main()

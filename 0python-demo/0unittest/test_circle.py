import unittest
from circle import ca
from math import pi

class TestCa(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(ca(3), pi*3**2)
        self.assertEqual(ca(1), pi)

    def test_values(self):
        self.assertRaises(ValueError, ca, -1)
        self.assertRaises(ValueError, ca, -2)

    # @unittest.skip("demonstrating skipping")
    def test_types(self):
        self.assertRaises(TypeError, ca, True)


        
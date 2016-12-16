import unittest
from romanNumeral import RomanNumeral


class TestRomalNumeralConverter(unittest.TestCase):
    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def tearDown(self):
        self.romanNumeral = None

    def test_convert_1_to_I(self):
        self.assertEqual(self.romanNumeral.convert(1), "I")

    def test_convert_3_to_III(self):
        self.assertEqual(self.romanNumeral.convert(3), "III")

    def test_convert_4_to_IV(self):
        self.assertEqual(self.romanNumeral.convert(4), "IV")

    def test_convert_9_to_IX(self):
        self.assertEqual(self.romanNumeral.convert(9), "IX")

if __name__ == '__main__':
    unittest.main()

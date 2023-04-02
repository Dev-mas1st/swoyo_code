import unittest
from roman_nums import roman_numerals_to_int


class Test(unittest.TestCase):
    def test_roman_numerals_to_int(self):
        self.assertEqual(roman_numerals_to_int("CMXCVIII"), 998)
        self.assertEqual(roman_numerals_to_int("IV"), 4)
        self.assertEqual(roman_numerals_to_int("77"), None)
        self.assertEqual(roman_numerals_to_int("III "), None)
import unittest
from prime import prime_numbers


class Test(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(prime_numbers(1, 20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(prime_numbers(20, 40), [23, 29, 31, 37])
        self.assertEqual(prime_numbers(-20, 40), [])
        self.assertEqual(prime_numbers('20', 40), [])

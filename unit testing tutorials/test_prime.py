import unittest
from prime import is_prime


class PrimeTestCase(unittest.TestCase):
    """TSET FOR PRIME CASES"""

    def test_is_5_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_4_non_prime(self):
        self.assertFalse(is_prime(4), msg='4 is not prime')

    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0), msg='0 is not prime')

    def test_is_negative_non_prime(self):
        self.assertFalse(is_prime(-1),msg='-1 is not prime')
        self.assertFalse(is_prime(-2),msg='-2 is not prime')
        self.assertFalse(is_prime(-3),msg='-3 is not prime')
        self.assertFalse(is_prime(-4),msg='-4 is not prime')
        self.assertFalse(is_prime(-5),msg='-5 is not prime')
        self.assertFalse(is_prime(-6),msg='-6 is not prime')
        self.assertFalse(is_prime(-7),msg='-7 is not prime')


if __name__ == '__main__':
    unittest.main()
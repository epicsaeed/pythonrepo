import unittest, calculator

class TestCalculator(unittest.TestCase):

    def test_add_5_plus_5(self):
        result = calculator.add(5,5)
        self.assertEqual(result,10)

    def test_subtract_10_minus_5(self):
        result = calculator.subtract(10,5)
        self.assertEqual(result,5)

    def test_subtract_5_minus_10(self):
        result = calculator.subtract(5,10)
        self.assertEqual(result,-5)

    def  test_subtract_0_minus_positive(self):
        result = calculator.subtract(0,5)
        self.assertEqual(result,-5)

    def  test_subtract_0_minus_negative(self):
        result = calculator.subtract(0,-5)
        self.assertEqual(result,5)

    def test_multiply_positive_times_positive(self):
        result = calculator.multiply(3,2)
        self.assertEqual(result,6)

    def  test_multiply_positive_times_negative(self):
        result = calculator.multiply(3,-2)
        self.assertEqual(result,-6)

    def  test_multiply_positive_times_0(self):
        result = calculator.multiply(5,0)
        self.assertEqual(result,0)

    def  test_multiply_negative_times_0(self):
        result = calculator.multiply(-5,0)
        self.assertEqual(result,0)

    def test_divide_100_over_10(self):
        result = calculator.divide(100,10)
        self.assertEqual(result,10)

    def test_divide_10_over_100(self):
        result = calculator.divide(10,100)
        self.assertEqual(result,0.1)

    def test_divide_positive_over_zero(self):
        result = calculator.divide(2,0)
        self.assertEqual(result,0)

    def test_divide_negative_over_zero(self):
        result = calculator.divide(-2,0)
        self.assertEqual(result,0)

    def test_valid_input(self):
        self.assertTrue(calculator.validInput(1,6))
        self.assertTrue(calculator.validInput(0,0))
        self.assertTrue(calculator.validInput(3,0))
        self.assertTrue(calculator.validInput(-1,6))
        self.assertTrue(calculator.validInput(-1,-6))

    def test_invalid_input(self):
        self.assertFalse(calculator.validInput('H',0))
        self.assertFalse(calculator.validInput('H',3))
        self.assertFalse(calculator.validInput('4',0))
        self.assertFalse(calculator.validInput('somegf','assoagd'))
        self.assertFalse(calculator.validInput(True,33))
        self.assertFalse(calculator.validInput('H',False))
        self.assertFalse(calculator.validInput(True,False))
        self.assertFalse(calculator.validInput(None,0))


if __name__ == '__main__':
    unittest.main()
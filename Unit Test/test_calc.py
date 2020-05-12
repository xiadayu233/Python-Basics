import unittest
import calc

class TestCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(10,5), 15)
		self.assertEqual(calc.add(10,6), 16)
		self.assertEqual(calc.add(1,5), 6)
		self.assertEqual(calc.add(1,-5), -4)

	def test_subtract(self):
		self.assertEqual(calc.subtract(10,5), 5)
		self.assertEqual(calc.subtract(10,6), 4)
		self.assertEqual(calc.subtract(1,5), -4)
		self.assertEqual(calc.subtract(1,-5), 6)

	def test_multiple(self):
		self.assertEqual(calc.multiply(10,5), 50)
		self.assertEqual(calc.multiply(10,6), 60)
		self.assertEqual(calc.multiply(1,5), 5)
		self.assertEqual(calc.multiply(1,-5), -5)

	def test_divide(self):
		self.assertEqual(calc.divide(10,5), 2)
		self.assertEqual(calc.divide(10,6), 10/6)
		self.assertEqual(calc.divide(1,5), 0.2)
		self.assertEqual(calc.divide(1,-5), -0.2)

		self.assertRaises(ValueError, calc.divide, 1,0)
		#the following will not work
		#self.assertRaises(ValueError, calc.divide(1,0))

if __name__ == "__main__":
	unittest.main()
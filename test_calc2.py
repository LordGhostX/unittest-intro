import unittest
import calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.first_number = 10
        self.second_number = 5

    def tearDown(self):
        print("tearDown Class")

    def test_add(self):
        self.assertEqual(calc.add(self.first_number, self.second_number), 15)

    def test_substract(self):
        self.assertEqual(calc.substract(
            self.first_number, self.second_number), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(
            self.first_number, self.second_number), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(self.first_number, self.second_number), 2)


if __name__ == "__main__":
    unittest.main()

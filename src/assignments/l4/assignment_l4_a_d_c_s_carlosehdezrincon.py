"""
ITESM - MCC
Analysis, Design and Construction of Software
Assignment L4 Exercise 21-24

Author: Carlos Eduardo Hernandez Rincon
Student ID: A01181616
Email: a01181616@itesm.mx

Date: February 12th 2019
"""
import unittest

from assignments.l4.exercise_9 import decimal_2_roman as exercise9_roman
from assignments.l4.exercise_8 import sample_mean as exercise8_sample_mean
from assignments.l4.exercise_8 import sample_standard_deviation as exercise8_sample_std_dev
from assignments.l4.exercise_8 import median as exercise8_median
from assignments.l4.exercise_8 import nquartile as exercise8_nquartile
from assignments.l4.exercise_8 import npercentile as exercise8_npercentile
from assignments.l4.exercise_14 import MyPowerList as exercise14_MyPowerList
from assignments.l4.exercise_15 import UsersDatabase as exercise15_UsersDataBase


class Exercise9RomanTest(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual("I", exercise9_roman(1))
        self.assertEqual("V", exercise9_roman(5))
        self.assertEqual("X", exercise9_roman(10))
        self.assertEqual("L", exercise9_roman(50))
        self.assertEqual("C", exercise9_roman(100))
        self.assertEqual("D", exercise9_roman(500))
        self.assertEqual("M", exercise9_roman(1000))

    def test_compound_numbers(self):
        self.assertEqual("II", exercise9_roman(2))
        self.assertEqual("IV", exercise9_roman(4))
        self.assertEqual("IX", exercise9_roman(9))
        self.assertEqual("VII", exercise9_roman(7))
        self.assertEqual("CLIX", exercise9_roman(159))
        self.assertEqual("CCCXLIII", exercise9_roman(343))
        self.assertEqual("DCXCIX", exercise9_roman(699))
        self.assertEqual("MMXIX", exercise9_roman(2019))
        self.assertEqual("MCMXCI", exercise9_roman(1991))
        self.assertEqual("MMM", exercise9_roman(3000))
        self.assertEqual("\u0305I\u0305V", exercise9_roman(4000))

    def test_invalid_value(self):
        # Rene's method expects a string saying 'Invalid' for invalid values, whereas I expect
        #  Exceptions
        with self.assertRaises(ValueError):
            exercise9_roman("René")

        with self.assertRaises(ValueError):
            exercise9_roman(0)

        with self.assertRaises(ValueError):
            exercise9_roman(-5)

        with self.assertRaises(ValueError):
            exercise9_roman(3.14)

        with self.assertRaises(ValueError):
            exercise9_roman(2000000)

        with self.assertRaises(ValueError):
            exercise9_roman(True)

        with self.assertRaises(TypeError):
            exercise9_roman()

    def test_non_null_str_value(self):
        result = exercise9_roman(10)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()


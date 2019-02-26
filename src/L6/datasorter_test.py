import random
import unittest
import os

from datasorter import DataSorter
from datasorter import NotCSVException


class DataSorterTest(unittest.TestCase):

    def setUp(self):
        self.under_test = DataSorter()
        file = open("test1.txt", "w+")
        file.write("1")
        file.close()
        file = open("test2.csv", "w+")
        file.write("1, 2, 3")
        file.close()

    def test_set_input_data_with_invalid_paths(self):
        with self.assertRaises(TypeError):
            self.under_test.set_input_data(48)
        with self.assertRaises(FileNotFoundError):
            self.under_test.set_input_data("test0.csv")

        with self.assertRaises(NotCSVException):
            self.under_test.set_input_data("test1.txt")

    def test_set_input_data_with_valid_paths(self):
        self.assertTrue(self.under_test.set_input_data("test2.csv"))
        self.assertIsNotNone(self.under_test.data)
        self.assertIsInstance(self.under_test.data, list)
        self.assertEqual(3, len(self.under_test.data))
        self.assertEqual('3', self.under_test.data[2])

    def tearDown(self):
        if os.path.exists("test1.txt"):
            os.remove("test1.txt")
        if os.path.exists("test2.csv"):
            os.remove("test2.csv")

    def test_merge_sort(self):
        # We'll test valid test cases here
        test_cases = [
            [],
            [3],
            [-1, -3, 5, 23, 2, 34, 5, 7],
            [0, 3, 2.3, 12, 5, 2.4, 2.39],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, 2],
            # Random case with 50 int numbers
            [random.randint(1, 100) for _ in range(50)],
            # Random case with 30 float numbers
            [random.uniform(1, 100) for _ in range(30)]
        ]

        for case in test_cases:
            # Inject a simulation of the data
            self.under_test.data = case
            self.under_test.execute_merge_sort()
            result = self.under_test.data

            # All elements in the original list should be in the sorted list
            self.assertTrue(len(case) == len(result),
                            msg=f"The original list and the sorting list are not of the same size! "
                            f"Original: {len(case)} Sorted: {len(result)}")
            self.assertTrue(all([x in result for x in case]),
                            msg="Not all of the elements in the original list are in the sorted list!")

            # All values should be in ASC order
            self.assertTrue(all(result[i] <= result[i + 1] for i in range(len(result) - 1)),
                            msg=f"{case} was not sorted ASC using MergeSort, it showed as: {result}")

    def test_merge_sort_invalid_values(self):
        # We'll test invalid test cases here
        test_cases = [
            None,
            "This is not a list",
            [0, 3, 2, "5", 4],
            [9.3, 8, 7, 6, None, 0, -1, 2]
        ]

        for case in test_cases:
            # Inject a simulation of the data
            self.under_test.data = case

            with self.assertRaises(ValueError,
                                   msg=f"{case} was an invalid case but ValueError was not raised!"):
                self.under_test.execute_merge_sort()

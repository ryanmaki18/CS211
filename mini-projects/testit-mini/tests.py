"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_empty(self):
        self.assertEqual(max_run([]), [])
        # Shows that an empty list cannot be run through buggy.py

    def test_max_run_last_run_largest(self):
        self.assertEqual(max_run([1, 3, 1, 3, 4, 4, 4]), [4, 4, 4])
        # shows that there is a bug if the longest run is the last run of the list

    def test_max_run_backwards(self):
        self.assertEqual(max_run([3, 3, 2, 2, 2, 1]), [2, 2, 2])
        # works correctly

    def test_max_run_tie(self):
        self.assertEqual(max_run([3, 3, 3, 2, 2, 2, 1]), [3, 3, 3])
        # works correctly

    def test_max_run_large(self):
        self.assertEqual(max_run([400, 500, 600, 600, 600, 400, 500]), [600, 600, 600])
        # works correctly

    def test_max_run_negative(self):
        self.assertEqual(max_run([-1, -2, -2, -2, -3]), [-2, -2, -2])
        # works correctly

    def test_max_run_decimal(self):
        self.assertEqual(max_run([.1, .2, .2, .2, .3]), [.2, .2, .2])
        # works correctly

    def test_max_run_string(self):
        self.assertEqual(max_run(["joe", "elliot", "joe", "bob", "bob", "bob", "dylan"]), ["bob", "bob", "bob"])
        # works correctly

if __name__ == "__main__":
    unittest.main()


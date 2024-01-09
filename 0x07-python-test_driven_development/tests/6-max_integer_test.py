#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for max_integer"""
    def test_basic(self):
        """
        Test list of integers
        return the max
        """
        lst = [1, 2, 3, 4, 5]
        got = max_integer(lst)
        self.assertEqual(got, 5)

    def test_not_int(self):
        """
        Test list of non integers
        raise a TypeError
        """
        lst = ["a", 2]
        self.assertRaises(TypeError, max_integer, lst)

    def test_nothing(self):
        """
        Test empty list
        return None
        """
        lst = []
        result = max_integer(lst)
        self.assertEqual(result, None)

    def test_negatives(self):
        """
        Test list of negative integer
        return the max
        """
        lst = [-1, -3, -2]
        result = max_integer(lst)
        self.assertEqual(result, -1)

    def test_float(self):
        """
        Test list of floats and integers
        return the max
        """
        lst = [1, 2, 3.4]
        result = max_integer(lst)
        self.assertEqual(result, 3.4)

    def test_one(self):
        """
        Test list with one integer
        return the integer
        """
        lst = [1]
        result = max_integer(lst)
        self.assertEqual(result, 1)

    def test_sames(self):
        """
        Test list with same integers
        return the integer
        """
        lst = [1, 1, 1, 1]
        result = max_integer(lst)
        self.assertEqual(result, 1)

    def test_not_list(self):
        """
        Test integer (not a list)
        raise a TypeError
        """
        self.assertRaises(TypeError, max_integer, 1)

    def test_string(self):
        """
        Test list of strings
        return the first
        """
        lst = ["Ho", "Hehe"]
        result = max_integer(lst)
        self.assertEqual(result, "Ho")

    def test_nothing(self):
        """
        Test with None
        raise a TypeError
        """
        self.assertRaises(TypeError, max_integer, None)

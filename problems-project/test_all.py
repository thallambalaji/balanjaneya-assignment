#!/usr/bin/env python
"""
Test script for all problem solutions.
"""
import unittest

from caesar_cipher import caesar_encode, caesar_decode
from indian_currency import format_indian_currency
from combine_lists import combine_lists
from minimize_loss import minimize_loss, minimize_loss_optimized

class TestCaesarCipher(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(caesar_encode("abc", 1), "bcd")
        self.assertEqual(caesar_encode("xyz", 1), "yza")
        self.assertEqual(caesar_encode("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_encode("abc", 26), "abc")  # Full rotation
    
    def test_decode(self):
        self.assertEqual(caesar_decode("bcd", 1), "abc")
        self.assertEqual(caesar_decode("yza", 1), "xyz")
        self.assertEqual(caesar_decode("Khoor, Zruog!", 3), "Hello, World!")

class TestIndianCurrency(unittest.TestCase):
    def test_format(self):
        self.assertEqual(format_indian_currency(123456.7891), "1,23,456.7891")
        self.assertEqual(format_indian_currency(1234567.89), "12,34,567.89")
        self.assertEqual(format_indian_currency(12345), "12,345")
        self.assertEqual(format_indian_currency(1234567890.12345), "1,23,45,67,890.12345")
        self.assertEqual(format_indian_currency(999), "999")

class TestCombineLists(unittest.TestCase):
    def test_combine(self):
        list1 = [
            {"positions": [10, 30], "values": ["value1", "value2"]},
            {"positions": [50, 70], "values": ["value5", "value6"]}
        ]
        
        list2 = [
            {"positions": [15, 40], "values": ["value3", "value4"]},
            {"positions": [80, 100], "values": ["value7", "value8"]}
        ]
        
        expected = [
            {"positions": [10, 30], "values": ["value1", "value2", "value3", "value4"]},
            {"positions": [50, 70], "values": ["value5", "value6"]},
            {"positions": [80, 100], "values": ["value7", "value8"]}
        ]
        
        result = combine_lists(list1, list2)
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertEqual(result[i]["positions"], expected[i]["positions"])
            self.assertEqual(result[i]["values"], expected[i]["values"])

class TestMinimizeLoss(unittest.TestCase):
    def test_basic(self):
        prices = [20, 15, 7, 2, 13]
        expected = (2, 5, 2)  # Buy in year 2 (price 15), sell in year 5 (price 13), loss 2
        self.assertEqual(minimize_loss(prices), expected)
        self.assertEqual(minimize_loss_optimized(prices), expected)
    
    def test_no_loss_scenario(self):
        prices = [5, 10, 15, 20]  # Always increasing
        self.assertIsNone(minimize_loss(prices))
        self.assertIsNone(minimize_loss_optimized(prices))

    def test_edge_case(self):
        prices = [10, 5, 15, 7, 6]
        # The correct result according to our function logic:
        # Buy in year 4 (price 7) and sell in year 5 (price 6) for a loss of 1
        # This is the minimum possible loss for this scenario
        expected = (4, 5, 1)
        
        self.assertEqual(minimize_loss(prices), expected)
        self.assertEqual(minimize_loss_optimized(prices), expected)

if __name__ == "__main__":
    unittest.main() 
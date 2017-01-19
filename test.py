#!/usr/bin/env python3

import unittest

from fib.fibonacci import F

class TestCases(unittest.TestCase):
    def test0(self):
        self.assertEqual(8, F(6), "Test failed to return the 6th Fib number")

    def test1(self):
        self.assertEqual(5, F(5), "Test failed to return the 5th Fib number")

    def test2(self):
        self.assertEqual(3, F(4), "Test failed to return the 4th Fib number")

    def test3(self):
        self.assertEqual(2, F(3), "Test failed to return the 3rd Fib number")

    def test4(self):
        self.assertEqual(1, F(2), "Test failed to return the 2nd Fib number")

    def test5(self):
        self.assertEqual(1, F(1), "Test failed to return the 1st Fib number")

    def test6(self):
        self.assertEqual(0, F(0), "Test failed to return the 0th Fib number")

    def test7(self):
        self.assertNotEqual(10, F(9), "Test failed when given unequal arguments")

    def test8(self):
        self.assertEqual(4052739537881, F(62), "Test failed to return the 62nd Fib number")

    def test9(self):
        self.assertEqual(0, F(-1), "Test failed with a negative number")
    #TODO: exception handling for the case below
    def test10(self):
        self.assertEqual(0, F('h'), "Test failed with a character")

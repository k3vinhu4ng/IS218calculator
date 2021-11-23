"""Test addition csv"""
import unittest
from calculator.calculations.addition import Addition
from calculator.csv_reader.reader import CsvReader

def addition_csv_test():
    test_file = CsvReader("tests/tests_data/addition.csv")
    for i in test_file:
        my_tuple = (i[0])
        result = i[1]
        addition = Addition(my_tuple)
        assert addition.get() == result

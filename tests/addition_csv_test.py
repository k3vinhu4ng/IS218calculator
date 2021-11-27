"""Test addition csv"""
from calculator.calculations.addition import Addition
from calculator.csv_reader.reader import CsvReader


def addition_csv_test():

    #Arrange
    test_file = CsvReader("tests/tests_data/addition.csv").data

    for i in test_file:
        my_tuple = (i[0])
        result = i[1]
        #Act
        addition = Addition(my_tuple)

        #Assert
        assert addition.get_result() == result





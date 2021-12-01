"""Test addition csv"""
from calculator.calculations.addition import Addition
from calculator.csv_reader.reader import CsvReader


def test_addition_csv_small():
    """testing small file"""
    #Arrange
    filepath = "tests/tests_data/addition.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:
        my_tuple = i[0]
        result = i[1]

        #Act
        addition = Addition(my_tuple)

        #Assert
        assert addition.get_result() == result


def test_addition_csv_large():
    """testing large file"""
    #Arrange
    filepath = "tests/tests_data/addition_large.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:
        my_tuple = i[0]
        result = i[1]

        #Act
        addition = Addition(my_tuple)

        #Assert
        assert addition.get_result() == result

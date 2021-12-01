"""Test subtraction csv"""
from calculator.calculations.subtraction import Subtraction
from calculator.csv_reader.reader import CsvReader


def test_subtraction_csv_small():
    """testing csv small"""
    #Arrange
    filepath = "tests/tests_data/subtraction.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:
        my_tuple = (-i[0][0], i[0][1])
        result = i[1]

        #Act
        subtraction = Subtraction(my_tuple)

        #Assert
        assert subtraction.get_result() == result


def test_subtraction_csv_large():
    """testing csv large"""
    #Arrange
    filepath = "tests/tests_data/addition_large.csv"
    test_file_large = CsvReader(filepath)

    for i in test_file_large.data:
        my_tuple = (-i[0][0], -i[0][1])
        result = i[1]

        #Act
        subtraction = Subtraction(my_tuple)

        #Assert
        assert subtraction.get_result() == result

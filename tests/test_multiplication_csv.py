"""Test addition csv"""
from calculator.calculations.multiplication import Multiplication
from calculator.csv_reader.reader import CsvReader


def test_multiplication_csv_small():
    """testing csv small"""
    #Arrange
    filepath = "tests/tests_data/multiplication.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:
        my_tuple = i[0]
        result = i[1]

        #Act
        multiplication = Multiplication(my_tuple)

        #Assert
        assert multiplication.get_result() == result


def test_multiplication_csv_large():
    """testing csv large"""
    #Arrange
    filepath = "tests/tests_data/multiplication_large.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:
        my_tuple = i[0]
        result = i[1]

        #Act
        multiplication = Multiplication(my_tuple)

        #Assert
        assert multiplication.get_result() == result

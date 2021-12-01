"""Test addition csv"""
from calculator.calculations.division import Division
from calculator.csv_reader.reader import CsvReader


def test_division_csv_small():
    """testing small csv"""
    # Arrange
    filepath = "tests/tests_data/division.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:

        my_tuple = i[0]
        if i[1] == "#DIV/0!":
            assert Division(my_tuple).get_result() == ZeroDivisionError
        else:
            result = float(i[1])
            new1 = 1 / my_tuple[0]
            new2 = my_tuple[1]
            new_tuple = (new1, new2)

            # Act
            division = Division(new_tuple)

            # Assert
            assert round(division.get_result(), 5) == round(result, 5)


def test_division_csv_large():
    """testing large csv"""
    # Arrange
    filepath = "tests/tests_data/division_large.csv"
    test_file = CsvReader(filepath)

    for i in test_file.data:

        my_tuple = i[0]
        if i[1] == "#DIV/0!" or 0 in my_tuple:
            assert Division(my_tuple).get_result() == ZeroDivisionError
        else:
            result = float(i[1])
            new1 = 1 / my_tuple[0]
            new2 = my_tuple[1]
            new_tuple = (new1, new2)

            # Act
            division = Division(new_tuple)

            # Assert
            assert round(division.get_result(), 5) == round(result, 5)

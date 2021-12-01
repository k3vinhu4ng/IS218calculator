"""Test addition csv"""
from datetime import datetime
import pandas as pd
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


def test_csv_write():
    """testing writing record logs"""
    #
    # filepath = "tests/tests_data/division_large.csv"
    # # test_file = CsvReader(filepath)
    #
    # df = pd.read_csv(filepath)
    # date = datetime.now()
    #
    # df_zero = df[df['result'] == '#DIV/0!']
    # df_zero['Timestamp'] = date
    # df_zero['Filename'] = filepath
    # df_zero.to_csv("results/zerodivision.csv")
    #
    list_csv = ["tests/tests_data/addition.csv",
            "tests/tests_data/addition_large.csv",
            "tests/tests_data/division.csv",
            "tests/tests_data/division_large.csv",
            "tests/tests_data/multiplication.csv",
            "tests/tests_data/multiplication_large.csv",
            "tests/tests_data/subtraction.csv",
            "tests/tests_data/subtraction_large.csv"
            ]
    data = []
    df_result = pd.DataFrame(data, columns = ["Record_Number",
                                              "Value_1", "Value_2",
                                              "Result", "Timestamp",
                                              "FileName"])
    df_zero = pd.DataFrame(data, columns=["Record_Number",
                                          "Value_1",
                                          "Value_2", "Result",
                                          "Timestamp", "FileName"])
    df_zero.to_csv("results/zerodivision.csv")
    df_result.to_csv("results/results.csv")

    for file in list_csv:
        filepath = file
        # test_file = CsvReader(filepath)

        df_test = pd.read_csv(filepath)
        date = datetime.now()

        df_zero = (df_test[df_test['result'] == '#DIV/0!'])
        df_zero['Timestamp'] = date
        df_zero['Filename'] = filepath
        df_zero.to_csv("results/zerodivision.csv", mode='a', header=False)

        df_result = (df_test[df_test['result'] != '#DIV/0!'])
        df_result['Timestamp'] = date
        df_result['Filename'] = filepath
        df_result.to_csv("results/results.csv", mode='a', header=False)

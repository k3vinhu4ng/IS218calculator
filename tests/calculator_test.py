"""testing calculator"""
import pytest
from calculator.history.calculations import Calculations
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division
from calculator.calculator import Calculator

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def test1():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 3)
    Calculator.addition(values)

    values1 = (3, 3)
    Calculator.subtraction(values1)

    values2 = (1, 10)
    Calculator.multiplication(values2)

    values3 = (5, 5)
    Calculator.division(values3)

    values4 = (5, 0)
    Calculator.division(values4)


def test_multiple(clear_history_fixture, test1):
    """testing multiple functions"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.history_length() == 5


    assert Calculator.get_first_result_value() == 4
    assert Calculator.get_num_result_value(0) == 4
    assert isinstance(Calculator.get_calculation_type(0), Addition)

    assert Calculator.get_num_result_value(1) == -6
    assert isinstance(Calculator.get_calculation_type(1), Subtraction)

    assert Calculator.get_num_result_value(2) == 10
    assert isinstance(Calculator.get_calculation_type(2), Multiplication)

    assert Calculator.get_num_result_value(3) == 0.04
    assert isinstance(Calculator.get_calculation_type(3), Division)

    assert Calculator.get_num_result_value(4) == ZeroDivisionError
    assert isinstance(Calculator.get_calculation_type(4), Division)

    assert Calculator.get_last_result_value() == ZeroDivisionError

    Calculator.clear_history()
    assert Calculator.history_length() == 0
    assert Calculator.clear_history() is True

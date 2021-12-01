"""Testing history"""

import pytest
from calculator.history.calculations import Calculations
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

@pytest.fixture
def setup_addition_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 3

def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 3

def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 3

def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    #This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Addition)

#testing subtraction


@pytest.fixture
def setup_subtraction_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    subtraction = Subtraction(values)
    Calculations.add_calculation(subtraction)

def test_subtraction_history(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_subtraction_history(clear_history_fixture, setup_subtraction_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_calculation_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == -3

def test_history_sub_last(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == -3

def test_history_sub_first(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == -3

def test_history_count_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_last_obj_sub(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    #This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Subtraction)

#testing division

@pytest.fixture
def setup_division_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (2, 2)
    division = Division(values)
    Calculations.add_calculation(division)

def test_history_division(clear_history_fixture, setup_division_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_division(clear_history_fixture, setup_division_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_calculation_division(clear_history_fixture, setup_division_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 0.25

def test_last_value_division(clear_history_fixture, setup_division_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 0.25

def test_get_calculation_first_division(clear_history_fixture, setup_division_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 0.25

def test_history_count_division(clear_history_fixture, setup_division_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_last_division_object(clear_history_fixture, setup_division_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    #This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Division)

#testing multiplication

@pytest.fixture
def setup_multiplication_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (2, 2)
    multiplication = Multiplication(values)
    Calculations.add_calculation(multiplication)

def test_add_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 4

def test_last_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 4

def test_first_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 4

def test_count_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_last_object_mult(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    #This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Multiplication)

#testing different functions

@pytest.fixture
def setup_addition_multiplication_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 3)
    addition = Addition(values)
    Calculations.add_calculation(addition)

    values2 = (3, 2)
    multiplication = Multiplication(values2)
    Calculations.add_calculation(multiplication)

def test_add_mult(clear_history_fixture, setup_addition_multiplication_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 2
    assert Calculations.get_calculation(1).get_result() == 6
    assert Calculations.get_last_calculation_result_value() == 6
    assert Calculations.get_first_calculation().get_result() == 4
    assert Calculations.get_calculation(0).get_result() == 4

@pytest.fixture
def setup_create_calculation_fixture():
    """Arrange & Act"""
    # pylint: disable=redefined-outer-name

    # Arrange
    values = (1, 3)
    values1 = (3, 3)
    values2 = (1, 10)
    values3 = (5, 5)
    values4 = (3, 3, 3, 0)

    # Act

    Calculations.add_addition_calculation(values)
    Calculations.add_multiplication_calculation(values1)
    Calculations.add_division_calculation(values2)
    Calculations.add_subtraction_calculation(values3)
    Calculations.add_division_calculation(values4)


def test_create(clear_history_fixture, setup_create_calculation_fixture):
    """ASSERT"""
    # pylint: disable=unused-argument,redefined-outer-name

    # Assert
    assert Calculations.count_history() == 5
    assert Calculations.get_first_calculation().get_result() == 4
    assert Calculations.get_calculation(0).get_result() == 4
    assert Calculations.get_calculation(1).get_result() == 9
    assert Calculations.get_calculation(2).get_result() == 0.1
    assert isinstance(Calculations.get_last_calculation_object(), Division)
    assert Calculations.get_last_calculation_result_value() == ZeroDivisionError

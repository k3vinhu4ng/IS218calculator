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

def test_add_calculation_to_history_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_calculation_history_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
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

def test_get_calc_last_result_value_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == -3

def test_get_calculation_first_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == -3

def test_history_count_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_get_calc_last_result_object_subtraction(clear_history_fixture, setup_subtraction_calculation_fixture):
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

def test_add_calculation_to_history_division(clear_history_fixture, setup_division_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_calculation_history_division(clear_history_fixture, setup_division_calculation_fixture):
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

def test_get_calc_last_result_value_division(clear_history_fixture, setup_division_calculation_fixture):
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

def test_get_calc_last_result_object_division(clear_history_fixture, setup_division_calculation_fixture):
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

def test_add_calculation_to_history_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1

def test_clear_calculation_history_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_calculation_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 4

def test_get_calc_last_result_value_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 4

def test_get_calculation_first_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 4

def test_history_count_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_get_calc_last_result_object_multiplication(clear_history_fixture, setup_multiplication_calculation_fixture):
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

def test_get_calculation_addition_multiplication(clear_history_fixture, setup_addition_multiplication_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 2
    assert Calculations.get_calculation(1).get_result() == 6
    assert Calculations.get_last_calculation_result_value() == 6
    assert Calculations.get_first_calculation().get_result() == 4
    assert Calculations.get_calculation(0).get_result() == 4

@pytest.fixture
def setup_create_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 3)
    Calculations.add_addition_calculation(values)
    values1 = (3, 3)
    Calculations.add_multiplication_calculation(values1)
    values2 = (1, 10)
    Calculations.add_division_calculation(values2)
    values3 = (5, 5)
    Calculations.add_subtraction_calculation(values3)

def test_create(clear_history_fixture, setup_create_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 4
    assert Calculations.get_first_calculation().get_result() == 4
    assert Calculations.get_calculation(0).get_result() == 4
    assert Calculations.get_calculation(1).get_result() == 9
    assert Calculations.get_calculation(2).get_result() == 0.1
    assert Calculations.get_last_calculation_result_value() == -10
    assert isinstance(Calculations.get_last_calculation_object(), Subtraction)

    test = (3, 4, 5, 6)
    Calculations.add_addition_calculation(test)
    test1 = (3, 3, 3, 0)
    Calculations.add_division_calculation(test1)
    assert Calculations.get_last_calculation_result_value() == ZeroDivisionError





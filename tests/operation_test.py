"""Testing Operations"""

from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (10.0, 5.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 15.0

def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    mynumbers = (2.0, 10.0)
    subtraction = Subtraction(mynumbers)
    #Act
    #Assert
    assert subtraction.get_result() == -12.0

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    mynumbers = (5.0, 12.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 60

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (10.0, 10.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.01

def test_calculation_division_zero():
    """testing that our calculator has a static method for division by zero"""
    #Arrange
    mynumbers = (60.0, 0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == ZeroDivisionError

"""Subtraction Class"""
from calculator.operations.calculation import Calculation


class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        result = None
        for value in self.values:
            if result is None:
                result = value
            else:
                result = result - value
        return result

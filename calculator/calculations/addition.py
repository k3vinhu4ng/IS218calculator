"""Addition Class"""
from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """returns the sum of inputs"""
        return sum(self.values)

"""Division Class"""
from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """divison calculation object"""
    def get_result(self):
        """get the division results"""
        try:
            result_division = 1.0
            for value in self.values:
                result_division /= value
            return result_division
        except ZeroDivisionError:
            return ZeroDivisionError

"""Division Class"""
from calculator.operations.calculation import Calculation


class Division(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        try:
            result_division = None
            for value in self.values:
                if result_division is None:
                    result_division = value
                else:
                    result_division /= value
            return result_division
        except ZeroDivisionError:
            return ZeroDivisionError

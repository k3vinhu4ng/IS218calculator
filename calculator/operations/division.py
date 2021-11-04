"""Division Class"""
from calculator.operations.calculation import Calculation


class Division(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        try:
            result = None
            for value in self.values:
                if result is None:
                    result = value
                else:
                    result /= value
            return result
        except ZeroDivisionError:
            return ZeroDivisionError

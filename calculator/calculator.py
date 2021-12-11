"""Calculator Program"""

from calculator.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def addition(tuple_values: tuple):
        """ adds list of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtraction(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def division(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_division_calculation(tuple_values)
        return True

    @staticmethod
    def history_length():
        """returns number of calculations"""
        return Calculations.count_history()

    @staticmethod
    def get_first_result_value():
        """returns first result value"""
        return Calculations.get_first_calculation_result_value()

    @staticmethod
    def get_num_result_value(num):
        """returns value of a specific calculation"""
        return Calculations.get_num_calculation_result_value(num)

    @staticmethod
    def get_calculation_type(num):
        """returns object"""
        return Calculations.get_calculation(num)

    @staticmethod
    def clear_history():
        """clears history"""
        Calculations.clear_history()
        return True

    @staticmethod
    def getHistoryFromCSV():
        Calculations.readHistoryFromCSV()
        return True

    @staticmethod
    def writeHistoryToCSV():
        Calculations.writeHistoryToCSV()
        return True

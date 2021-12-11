from calculator.history.calculations import Calculations
import pandas as pd

def test_csv_read_history():
    Calculations.readHistoryFromCSV()

    assert Calculations.count_history() == 15
    assert Calculations.get_first_calculation_result_value() == 3

def test_csv_write_history():
    Calculations.writeHistoryToCSV()




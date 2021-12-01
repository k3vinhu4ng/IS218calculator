"""Reader for path and converting to pandas"""
from pathlib import Path
import pandas as pd



# def absolute_path(filepath):
#     """absolute path"""
#     relative = Path(filepath)
#     return relative.absolute()
#

class CsvReader:
    """csv reader class"""

    def __init__(self, filepath):
        self.data = []
        self.reader(Path(filepath).absolute())

    def reader(self, filepath):
        """sets up the csv file to be in a testable format"""
        datagram = pd.read_csv(filepath)
        for index, row in datagram.iterrows():
            self.data.append([(row['value_1'], row['value_2']), row['result']])

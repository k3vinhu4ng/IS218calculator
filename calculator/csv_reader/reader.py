import pandas as pd
from pathlib import Path

def absolutepath(filepath):
    """absolute path"""
    relative = Path(filepath)
    return relative.absolute()


class CsvReader:
    """csv reader class"""
    data = []

    def __init__(self):
        self.data = []
        self.reader(absolutepath(filepath))


    def reader(self, filepath):
        df = pd.read_csv(filepath)
        for index, row in df.iterrows():
            """
            info being appended -> [(tuple), result]
            first element is a tuple because that is what *args wants
            i do this here instead of appending [1,2,3], and then having to make a tuple in the tests
            """
            self.data.append([(row['value1'], row['value2']), row['result']])



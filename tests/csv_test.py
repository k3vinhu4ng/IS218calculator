# import unittest
# from pprint import pprint
# from pathlib import Path
# from calculator.csv_reader.csv_reader import CsvReader, class_factory
#
#
# class CsvTestCase(unittest.TestCase):
#
#     def setup(self) -> None:
#         self.csv_reader = CsvReader('tests_data/addition.csv')
#
#
#     #def test_return_data_as_objects(self):
#         test_cases = self.return_data_as_class('test_case')
#         self.assertIsInstance(test_cases, list)
#         test_class = class_factory('test_cases', self.csv_reader.data[0])
#
#         for value in test_cases:
#             self.assertEqual(test_cases.__name__, test_class.__name__)
#             pprint(vars(test_cases))
#
#              # self.assertEqual(test_cases.__name__, test_class.__name__)
#              # pprint(vars(value))
#
#     if __name__ == '__main__':
#         unittest.main()
#
# import pandas as pd
# from pathlib import Path
#
# #filepath = Path("tests_data/addition.csv").absolute()
#
#
# df = pd.read_csv("tests_data/addition.csv")
#
# #print(df.head())
#
# data = []
#
# for index, row in df.iterrows():
#     data.append([(row['value_1'], row['value_2']), row['result']])
#
#
# x = data[0][1]
# print(data)
# print(x)
#
# print(type(x))

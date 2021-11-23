import csv
from calculator.fileutilities.absolutepath import absolutepath


def class_factory(class_name, dictionary):
    """comments"""
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(class_factory(class_name, row))
        return objects

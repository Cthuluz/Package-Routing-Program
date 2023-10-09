import csv


class FileLoader:
    def __init__(self):
        self.my_data = []

    def load_file(self, my_file):
        data = open(my_file, encoding='utf-8-sig')
        csv_data = csv.reader(data)
        self.my_data = list(csv_data)
        return self.my_data

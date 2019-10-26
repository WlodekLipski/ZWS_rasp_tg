import os
import csv


class Sensors_data():
    def __init__(self, file_name='data.csv'):
        self.data = None
        self.tmp_data = None
        self.is_average = False
        self.file_name = file_name

    def average(self, values):
        for i in range(0, len(values)):
            self.data[i] = (self.data[i] + values[i]) // 2

    def save_average(self, values):
        if not self.is_average:
            self.data = values
            self.is_average = True
        else:
            self.average(values)
            """
            Creating a string from values
            and appending it to a file
            """
            data = str(self.data[0])
            for i in self.data[1:]:
                data += ','+str(i)
            data += '\n'
            with open(self.file_name, mode='a') as fd:
                fd.write(data)

            self.is_average = False
        return self.is_average

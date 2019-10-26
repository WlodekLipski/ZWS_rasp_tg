import os
import pandas


class Sensors_data():
    def __init__(self, file_name='data.csv'):
        self.data = None
        self.tmp_data = None
        self.mean = False
        if not os.path.exists(file_name):
            open(file_name, 'a').close()
        try:
            self.data = pandas.read_csv(file_name)
        except pandas.errors.EmptyDataError:
            self.data = None
            pass
            
    def append_data(self, _temp, _light, _humid):
        """
        Zipping values in appropiate format
        """
        keys = ['Temperature', 'Light', 'Humidity']
        values = [[_temp],[_light],[_humid]]
        if isinstance(self.data, pandas.DataFrame):
            _data = pandas.DataFrame(dict(zip(keys,values)))
            if not self.mean:
                self.tmp_data = _data
                self.mean = True
            else:
                """
                Average from 2 frames
                """
                self.tmp_data = self.tmp_data.add(_data).floordiv(2)
                self.data = self.data.append(self.tmp_data, ignore_index=True)
                self.save_to_file()
                self.mean = False

        else:
            self.data = pandas.DataFrame(dict(zip(keys,values)))

    def save_to_file(self, file_name='data.csv'):
        if self.data is not None:
            self.data.to_csv(file_name, index=False)

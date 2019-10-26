import os
import pandas


class Sensors_data():
    def __init__(self, file_name='data.csv'):
        self.data = None
        if not os.path.exists(file_name):
            open(file_name, 'a').close()
        try:
            self.data = pandas.read_csv(file_name)
        except pandas.errors.EmptyDataError:
            pass
            
    def append_data(self, _temp, _light, _humid):
        """
        Zipping values in appropiate format
        """
        keys = ['Temperature', 'Light', 'Humidity']
        values = [[_temp],[_light],[_humid]]
        if isinstance(self.data, pandas.DataFrame):
            _data = pandas.DataFrame(dict(zip(keys,values)))
            self.data = self.data.append(_data, ignore_index=True)
        else:
            self.data = pandas.DataFrame(dict(zip(keys,values)))

    def save_to_file(self, file_name='data.csv'):
        if self.data is not None:
            self.data.to_csv(file_name, index=False)

import time
import smbus
import threading
from . import bh1750
from . import dht11
from . import data

"""
Class launching thread
which is responding for
collecting data from sensors
"""
class Runner():
    def __init__(self, _sleep):
        self.sleep = _sleep
        self.data = data.Sensors_data()
        self.bus = smbus.SMBus(1)
        self.light = bh1750.BH1750(self.bus)
        self.dht = dht11.DHT()

    def set_sleep(self, _sleep=None):
        if _sleep is not None:
            try:
                self.sleep = int(_sleep)
                """
                Sleep timeout might
                be in range 60 to 3600
                """
                if (self.sleep < 60 or
                        self.sleep > 3600):
                    self.sleep = 60

            except ValueError:
                self.sleep = 60
        else:
            self.set_sleep(60)


    def get_sleep(self):
        return self.sleep

    def launch(self, is_running):
        while not is_running.is_set():
            _humid, _temp  = self.dht.read()
            if _humid == -1:
                time.sleep(self.sleep)
            else:
                """
                Collecting data and writing to a file
                """
                _light  = int(self.light.measure_high_res())
                self.data.save_average([_temp, _light, _humid])
                time.sleep(self.sleep)

    def terminate(self, is_running):
        is_running.set()

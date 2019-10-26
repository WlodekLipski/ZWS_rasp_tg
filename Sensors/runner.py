import time
import smbus
import data
import threading
import bh1750
import dht11

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
                be in range 1 to 3600
                """
                if (self.sleep < 1 or
                        self.sleep > 3600):
                    self.sleep = 1

            except ValueError:
                self.sleep = 0xff
        else:
            self.set_sleep(0xff)


    def get_sleep(self):
        return self.sleep

    def launch(self, is_running):
        while not is_running.is_set():
            _dht = self.dht.read()
            if _dht[0] == -1:
                time.sleep(self.sleep)
                pass
            else:
                """
                Collecting data and writing to a file
                """
                _humid = _dht[0]
                _temp = _dht[1]
                _light  = int(self.light.measure_high_res())
                self.data.append_data(_temp, _light, _humid)
                time.sleep(self.sleep)

    def terminate(self, is_running):
        is_running.set()

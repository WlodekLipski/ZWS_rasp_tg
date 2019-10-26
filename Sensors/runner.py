#import Adafruit_DHT
import time
import smbus
import data
import threading
import bh1750

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
                """
                Default value in case of errors
                in config file
                """
                self.sleep = 0xff
        else:
            self.set_sleep(0xff)


    def get_sleep(self):
        return self.sleep

    def launch(self, is_running):
        while not is_running.is_set():
            _light  = int(self.light.measure_high_res())
            """
            Values from dht needed
            Hook to append data to a file
            _temp _light _ humidity
            """
            time.sleep(self.sleep)

    def terminate(self, is_running):
        is_running.set()

#sensor = Adafruit_DHT.DHT11
#pin = 4
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#if humidity is not None or temperature is not None:
#    print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#    print('Failed to get temperature or humidity')

#import Adafruit_DHT
import time
import threading
import configparser

config = configparser.ConfigParser()
config.read('sensors.ini')

"""
Class launching thread
which is responding for
collecting data from sensors
"""
class Runner():
    def __init__(self):
        self._sleep = 10

    def _set_sleep(self):
        try:
            self._sleep = int(config.get('CONFIG','sleep'))
            """
            Sleep timeout might
            be in range 1 to 3600
            """
            if (self._sleep < 1 or
                    self._sleep > 3600):
                self._sleep = 1

        except (configparser.NoSectionError,
                configparser.NoOptionError,
                ValueError):
            """
            Default value in case of errors
            in config file
            """
            self._sleep = 0xff

    def _launch(self, is_running):
        while not is_running.is_set():
            print('Thread hello')
            time.sleep(self._sleep)

    def _terminate(self, is_running):
        is_running.set()

    def _print(self):
        print('Sleep timeout:',self._sleep)

#sensor = Adafruit_DHT.DHT11
#pin = 4
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#if humidity is not None or temperature is not None:
#    print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#    print('Failed to get temperature or humidity')

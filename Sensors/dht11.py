import Adafruit_DHT
class DHT():
    def __init__(self, pin=4):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin
        self.temperature = None
        self.humidity = None

    def read(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if (self.humidity is not None 
                and self.temperature is not None):
            return [int(self.humidity), int(self.temperature)]
        else:
            return [-1, -1]

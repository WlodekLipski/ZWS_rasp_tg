import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None or temperature is not None:
    print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get temperature or humidity')

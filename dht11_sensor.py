# DHT11 Sensor
# Data Pin to D0 - GPIO16

from dht import *
from time import *

d=DHT11(Pin(16))

while True:
  d.measure()
  print("Humidity : %d, Temperature: %d" % (d.humidity(),d.temperature()))
  sleep(2)

# Alcohol Sensor
# DO to D1 (GPIO5)
# LED to D0 (GPIO16)

from machine import *

alcohol_sensor=Pin(5,0)
led=Pin(16,1)

while True:
  if(alcohol_sensor.value()==0):
    print ('Alcohol Detected')
    led.value(0)
  else:
    print ('Alcohol Not Detected')
    led.value(1)
  sleep(100)


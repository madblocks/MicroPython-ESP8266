# IR Sensor Program
# Sensor - D1
# LED - D0

from machine import *
from time import *

ir=Pin(5,0)
led=Pin(16,1)

while True:
  if(ir.value()==0):
    print ('Obstacle Found')
    led.value(0)
  else:
    print ('Obstacle Not Found')
    led.value(1)
  sleep(5)


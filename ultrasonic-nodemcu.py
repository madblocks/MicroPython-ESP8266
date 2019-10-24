# Ultrasonic Sensor Program
# ECHO - D1 - GPIO5
# TRIG - D2 - GPIO4

from machine import *
from utime import *

ECHO=Pin(5,0)
TRIG=Pin(4,1)

def read_distance():
  print ('Reading Data from Ultrasonic Sensor')
  TRIG.value(0)
  sleep_us(2)
  TRIG.value(1)
  sleep_us(10)
  TRIG.value(0)
  while ECHO.value()==0:
    pass
  pulse_start=ticks_us()
  while ECHO.value()==1:
    pass
  pulse_end=ticks_us()
  pulse_duration=pulse_end-pulse_start
  distance=int(0.034*(pulse_duration)/2)
  print ('Distance: %d cm' % distance)
  sleep(1)

while -5:
  read_distance()

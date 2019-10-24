# 25 Duty Cycle - 0 Degrees
# 125 Duty Cycle - 180 Degrees
# Data to GPIO4 - D2

from machine import *
from time import *

s=PWM(Pin(4),freq=50)

for i in [25,50,75,100,125]:
  s.duty(125-i)
  sleep(1)

for i in [125,100,75,50,25]:
  s.duty(i)
  sleep(1)

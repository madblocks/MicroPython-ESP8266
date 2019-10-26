# Controlling Bulb from Cloud
# Relay - D0

from machine import *
from network import *
from urequests import *
from time import *

bulb=Pin(16,1)
ssid="Automad"
password="@ut0M@D0"

def bulbon():
  print ('Your Bulb is On')
  bulb.value(0)
  
def bulboff():
  print ('Your Bulb is Off')
  bulb.value(1)

def connect_wifi():
  print ('Connecting with Wi-Fi')
  station=WLAN(STA_IF)
  if(station.isconnected()==True):
    print(station.ifconfig())
    return ()
  station.active()
  station.connect(ssid,password)
  while(station.isconnected()==False):
    pass
  print('Connection Successful')
  print(station.ifconfig())

def read_data1():
  k=get('http://madblocks.tech/dashboard/device_pull.php?device_api_key=26e0beab9071291f97887b0f53920db5')
  k=k.text
  k=k.split('<br/>')[0]
  k=k.split(' ')[-1]
  print (k)
  return (k)
  
connect_wifi()
while True:
  m=read_data1()
  if(m=='on'):
    bulbon()
  elif(m=='off'):
    bulboff()
  sleep(2)

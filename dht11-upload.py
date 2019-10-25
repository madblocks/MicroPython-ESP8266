# Uploading DHT11 to our madBlocks Dashboard
# DHT11 Sensor
# Data to D0 - GPIO16

from machine import *
from network import *
from socket import *
from dht import *
from time import *

ssid="Automad"
password="@ut0M@D0"

d=DHT11(Pin(5))
cloud_api='dashboard/upload_data.php?channel_api_key=e24844918055f79998056c42e811b405&sensor1_name='
#Wi-Fi Connectivity
def connect_wifi():
    print ('Connecting with Wi-Fi')
    station = WLAN(STA_IF)
    if(station.isconnected()):
      print (station.ifconfig())
      return()
    station.active(True)
    station.connect(ssid,password)
    while (station.isconnected()==False):
      pass
    print('Connection Successful')
    print(station.ifconfig())
    
def upload_data(h,p):
    print ('Uploading Data to Cloud')
    s=socket()
    s.connect(('2.57.89.27',80))
    t='GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n'% (p,h)
    s.send(t.encode('utf-8'))
    while True:
      k=s.recv(1024)
      if k:
        print (k)
        break
    s.close()
connect_wifi()    
while True:
  d.measure()
  h=d.humidity()
  t=d.temperature()
  data_1=cloud_api+str(h)+'&sensor2_name='+str(t)
  upload_data('madblocks.tech',data_1)
  print ("H is %d" % h)
  print ("T is %d" % t)
  
  sleep(2)

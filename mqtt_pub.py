from machine import *
from network import *
from umqtt.simple import *
from time import *

ssid="Madhu P"
password="Madhu23!"
madblocks_broker="YOUR BROKER"
madblocks_broker_port=1883


def connect_wifi():
  print ('Connecting with WiFi')
  station=WLAN(STA_IF)
  if(station.isconnected()==True):
    print ('WiFi Connected')
    print (station.ifconfig())
  station.active(True)
  station.connect(ssid,password)
  while station.isconnected()==False:
    pass
  print ('WiFi Connected')
  print (station.ifconfig())

connect_wifi()
client=MQTTClient("madpiot",madblocks_broker)
client.connect()
client.publish("madblocks","Madhu is a Good Boy1")
client.disconnect()

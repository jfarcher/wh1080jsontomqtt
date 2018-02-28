#!/usr/bin/python
import json
import sys
import datetime
import paho.mqtt.client as mqtt
from time import sleep
mqtthost = ''
format = "%H:%M:%S"
today = datetime.datetime.today()
s = today.strftime(format)
d = datetime.datetime.strptime(s, format)
t = d.strftime(format)
today = datetime.date.today()


WEATHERFILE='/tmp/weather.json'

file = open(WEATHERFILE, "r")
lineList = file.readlines()
WEATHERJSON = lineList[len(lineList)-1]

data = json.loads(WEATHERJSON)
time = data["time"]
temp = data["temperature_C"]
humidity = str(data["humidity"])
avgWindSpeed = str(data["speed"])
rain = str(data["rain"])
#batteryLow = str(data["batteryLow"])
windDirection = str(data["direction_deg"])
gustSpeed = str(data["gust"])
tempf = str(9.0/5.0 * temp + 32)


topic = "weather"
mqttc = mqtt.Client()
mqttc.connect (mqtthost, "1883", 60)
while True:
  mqttc.publish(topic + "/full",str(data), retain=True)
  mqttc.publish(topic + "/humidity",humidity, retain=True)
  mqttc.publish(topic + "/temp",temp, retain=True)
  mqttc.publish(topic + "/avgWindSpeed",avgWindSpeed, retain=True)
  mqttc.publish(topic + "/rain",rain, retain=True)
  mqttc.publish(topic + "/windDirection",windDirection, retain=True)
  mqttc.publish(topic + "/gustSpeed",gustSpeed, retain=True)
  mqttc.publish(topic + "/tempf",tempf, retain=True)
  mqttc.publish("atomictime",time, retain=True)
  sleep(30)



print temp

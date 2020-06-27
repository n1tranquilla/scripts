#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import requests
import sys
from pushbullet import Pushbullet

pb = Pushbullet(sys.argv[1])
channel_name = sys.argv[2]
mqtt_channel = sys.argv[3]

channel = pb.get_channel(channel_name)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(mqtt_channel)

def on_message(client, userdata, msg):
  file = msg.payload.decode()
  result = channel.push_note('Torrent complete', '{} has finished downlaoding'.format(file))
  print('{} has finished downloading'.format(file))

client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

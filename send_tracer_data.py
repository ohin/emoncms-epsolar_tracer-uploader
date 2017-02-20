#!/usr/bin/python

import serial
import json
import sys
from requests import get
from time import sleep
from tracer import Tracer, TracerSerial, QueryCommand

with open(sys.argv[1], 'r') as keyfile:
    EMON_CMS_KEY = keyfile.read().strip()

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
tracer = Tracer(0x16)
tracer_serial = TracerSerial(tracer, port)
query = QueryCommand()

def clean_data(data):
   del(data["data"])
   for key, value in data.iteritems():
      if isinstance(value, bool):
         data[key] = 1 if value else 0
   return data


while True:
   try:
      tracer_serial.send_command(query)
      tracer_data = tracer_serial.receive_result()

      load = clean_data(tracer_data.__dict__)
   
      print get("https://emoncms.org/input/post.json?node=1&apikey=%s&json=%s" % (EMON_CMS_KEY, json.dumps(load))).text
   except Exception as e:
      print >> sys.stderr, e
   
   sleep(10)

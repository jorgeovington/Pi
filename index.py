#!/usr/bin/env python

import json
import screen, tb
#import requests
from sense_hat import SenseHat
from time import sleep



# Constants

#API_KEY          = "<ThingsBoard API Key>"
#THINGSBOARD_HOST = "<Linode Public IP Address>"

#thingsboard_url  = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)

sense = SenseHat()


data = {}

while True:
    temperatura = int(round(sense.get_temperature()))
    humedad = int(round(sense.get_humidity()))
    data['temperatura'] = str(round(sense.get_temperature(),2))
    data['Presion'] = str(round(sense.get_pressure(),2))
    data['Humedad'] = str(round(sense.get_humidity(),2))

    screen.pintar(temperatura, humedad)
    tb.set(data)
  #  r = requests.post(thingsboard_url, data=json.dumps(data))
    print(str(data))
    sleep(20)

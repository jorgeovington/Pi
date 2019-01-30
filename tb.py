#!/usr/bin/env python

import json
import requests

# Constants
def set(data):
    API_KEY          = "KPlSY7837aWkuisw7G3f"
#    THINGSBOARD_HOST = "iot.jorgeovington.com:2080"
    THINGSBOARD_HOST = "192.168.0.23:8080"

    thingsboard_url  = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)

    r = requests.post(thingsboard_url,data = json.dumps(data))

# KPlSY7837aWkuisw7G3f

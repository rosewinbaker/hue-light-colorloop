import json
import requests
import time

action = raw_input("What would you like to do?: ")

# Pick the group of lights or specific lights
if "living room" in action:
    apiURL = my_api_request_link + 'groups/2/action'

elif "bedroom" in action:
    apiURL = my_api_request_link + 'groups/1/action'

elif "5" in action:
    apiURL = my_api_request_link + 'lights/5/state'

elif "6" in action:
    apiURL = my_api_request_link + 'lights/6/state'

else:
    print("Sorry, did not recognize any devices or groups by that name.")


# Turn device on and loop through color values.
if "on" in action:
    hueValue = eval(raw_input("Please choose hue value between 0 and 65535: "))

    while True:
        print hueValue
        hueValue = hueValue+1000
        if hueValue > 65001:
            hueValue = 1

        time.sleep(.25)
        r = requests.put(apiURL,
            json={
                "on": True,
                "sat":254,
                "bri":154,
                "hue": hueValue
                })

    print hueValue

elif "off" in action:

    r = requests.put(apiURL,
        json={
            "on": False,
            })

else:
    print ("Action not recognized.")

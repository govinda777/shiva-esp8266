#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9 
#from modules.umqtt.robust2 import MQTTClient

import time
import sys
from infra.mqtt import Mqtt
from infra.wifi import Wifi

WIFI_SSID = "VIVOFIBRA-6CA1"
WIFI_PW = "Pedro2203"
mqtt = Mqtt()

#start execution
try:
    wifi = Wifi(WIFI_SSID, WIFI_PW)

    print("Connecting WIFI")
    wifi.connect_wifi()
    print("Connecting MQTT")
    mqtt.connect_mqtt()
    mqtt.sub()
    print("Publishing")
    mqtt.pub_msg("{\"AWS-MQTT-8266-01\":" + str(time.time()) + "}")
    
    print("OK")

except Exception as e:
    print(str(e))

while True: 
    try: 
        time.sleep(2)
        #mqtt.wait_msg() #blocking 
        mqtt.check_msg() #non-blocking 
         
    except KeyboardInterrupt: 
        print('Ctrl-C pressed...exiting') 
        mqtt.disconnect() 
        sys.exit()


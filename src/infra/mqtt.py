from umqtt.robust import MQTTClient

class Mqtt:

    #This works for either ESP8266 ESP32 if you rename certs before moving into /flash 
    CERT_FILE = "/teste.cert.der"
    KEY_FILE = "/teste.private.der"

    #if you change the ClientId make sure update AWS policy
    MQTT_CLIENT_ID = "basicPubSub"
    MQTT_PORT = 8883

    #if you change the topic make sure update AWS policy
    MQTT_TOPIC = "sdk/test/Python"

    #Change the following three settings to match your environment
    MQTT_HOST = "a12sdqmvxrmcs4-ats.iot.us-east-1.amazonaws.com"

    mqtt_client = None

    def check_msg(self):
        global mqtt_client
        mqtt_client.check_msg()

    def wait_msg(self):
        global mqtt_client
        mqtt_client.wait_msg()

    def on_message(self, topic, msg):
        print('Message topic: {}, payload: {}'.format(topic, str(msg)))

    def sub(self):
        global mqtt_client
        try:    
            mqtt_client.subscribe(self.MQTT_TOPIC, qos = 1)
            
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

    def pub_msg(self, msg):
        global mqtt_client
        try:    
            mqtt_client.publish(self.MQTT_TOPIC, msg)
            print("Sent: " + msg)
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

    def connect_mqtt(self):    
        global mqtt_client

        try:
            with open(self.KEY_FILE, "r") as f: 
                key = f.read()

            print("Got Key")
                
            with open(self.CERT_FILE, "r") as f: 
                cert = f.read()

            print("Got Cert")	

            mqtt_client = MQTTClient(client_id=self.MQTT_CLIENT_ID, server=self.MQTT_HOST, port=self.MQTT_PORT, keepalive=5000, ssl=True, ssl_params={"cert":cert, "key":key, "server_side":False})
            mqtt_client.set_callback(self.on_message) 
            mqtt_client.connect()
            print('MQTT Connected')

        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise
import network

class Wifi:

    def __init__(self, ssid, pw):
        self.__ssid = ssid
        self.__pw = pw

    def connect_wifi(self):

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        if(wlan.isconnected()):
            wlan.disconnect()  

        nets = wlan.scan()

        if not wlan.isconnected():

            wlan.active(True)
            wlan.connect(self.__ssid, self.__pw)
            while not wlan.isconnected():
                print(".")
                pass

        print("connected:", wlan.ifconfig())

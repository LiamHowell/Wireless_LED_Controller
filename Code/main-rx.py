import network
from esp import espnow
import ubinascii

from liam_funcs import *
#from neopixel import Neopixel
import neopixel

print('----------RUNNING----------')
print('----------RX Board----------')
# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

e = espnow.ESPNow()
e.init()
peer = b'\x11\x22\x33<\x44\x55'  # MAC address of peer's wifi interface

e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        print(unpackBytesColour(msg))
        RGB = unpackBytesColour(msg)
        showColour(RGB)
        



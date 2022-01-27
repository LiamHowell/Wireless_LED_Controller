import network
from esp import espnow
from liam_funcs import *
import utime

print('----------RUNNING----------')
print('----------TX Board----------')

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)

e = espnow.ESPNow()
e.init()
peer = b'\x24\x6f\x28\xc5\x1b\x68'   # MAC address of peer's wifi interface
e.add_peer(peer)

#e.send("Starting...")       # Send to all peers
for i in range(10):
    r_Bright = str(10*i)
    
    LED_COM = 'R' + r_Bright + 'G' + str('0')+ 'B' + str('0')+ 'X'
    sent_str = LED_COM
    
    print(LED_COM)
    e.send(peer, sent_str, True)
    #utime.sleep_ms(500)
 
#e.send('end')

import ubinascii
import network
import neopixel
import machine
from esp import espnow

def getMAC(): #Prints the mac address of the ESP-32, replace ':' with '\x' in peers 
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':')
    print(mac)
    
def unpackBytesColour(packet): #Unpack propietary packet structure into a dict
    proc = packet.decode("utf-8")
    RGB = dict()
    RGB["R"] = int(proc[proc.find("R")+1:proc.find("G")])
    RGB["G"] = int(proc[proc.find("G")+1:proc.find("B")])
    RGB["B"] = int(proc[proc.find("B")+1:proc.find("X")])
    return RGB

def showColour(RGB): #Quick n dirty implementation of an LED strip being updated
    np = neopixel.NeoPixel(machine.Pin(21), 5)
    np.fill((RGB['R'],RGB['G'],RGB['B']))
    np.write()
    
def initComms():
    w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
    w0.active(True)
    e = espnow.ESPNow()
    e.init()
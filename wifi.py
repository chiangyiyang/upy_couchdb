
import network

def connect(ap, pw):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ap, pw)

def disconnect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)

def is_connected():
    sta_if = network.WLAN(network.STA_IF)
    return sta_if.isconnected()

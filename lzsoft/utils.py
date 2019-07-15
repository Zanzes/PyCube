import os
from bluepy.btle import DefaultDelegate
from elevate import elevate

def is_root():
    return os.getuid() == 0

def ensure_root():
    if not is_root():
        elevate()

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

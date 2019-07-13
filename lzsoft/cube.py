import os
from bluepy.btle import DefaultDelegate
from bluepy.btle import Scanner
from elevate import elevate

def is_root():
    return os.getuid() == 0

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

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(60.0)

for dev in devices:
    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value))
    print()
exit()
































#
# import sys
# from bluetooth.ble import GATTRequester
#
#
# service = DiscoveryService()
# devices = service.discover(8)
#
#
# class Reader(object):
#     def __init__(self, address):
#         self.requester = GATTRequester(address, False)
#         self.connect()
#         self.request_data()
#
#     def connect(self):
#         print("Connecting...", end=' ')
#         sys.stdout.flush()
#
#         self.requester.connect(True)
#         print("OK!")
#
#     def request_data(self):
#         print(self.requester.discover_characteristics())
#         data = self.requester.read_by_uuid(
#             "00002a00-0000-1000-8000-00805f9b34fb")[0]
#         try:
#             print("Device name: " + data.decode("utf-8"))
#         except AttributeError:
#             print("Device name: " + data)
#
#
# if __name__ == '__main__':
#     for item in devices.items():
#         try:
#             Reader(item[0])
#         except Exception as e:
#             print(e)
#
#     print("Done.")
#
#
#
#

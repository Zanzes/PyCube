from pprint import pprint

from utils import ScanDelegate, ensure_root
from bluepy.btle import Scanner, Peripheral

ensure_root()


def search_loop():
    while True:
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(5.0)

        for dev in devices:
            data = dev.getScanData()
            for (adtype, desc, value) in data:
                if "Short Local Name" in desc:
                    print("Cube found:")
                    print("  Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
                    for (adtype, desc, value) in data:
                        print("  %s = %s" % (desc, value))
                    p = Peripheral(deviceAddr=dev.addr, addrType=dev.addrType)
                    for serv in p.getServices():
                        print(serv.uuid.getCommonName())
                        for char in serv.getCharacteristics():
                            pprint(char.propertiesToString())
                    return
        #print(f"All data: {data}")
        #print()

search_loop()

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

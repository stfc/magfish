class Machine:

    ip = ""
    mac = ""

    fqdn = ""
    manufact = ""
    model = ""

    serialNo = ""
    coreCount = -1
    coreModel = ""
    totalMemory = -1

    rack = -1
    position = -1
    units = -1

    def __init__ (self,ip):
        self.ip = ip

    def displayIp(self):
        print("\nIP Address: " + self.ip)

    def displayMac(self):
        print("\nMAC Address: " + self.mac)

    def displayFqdn(self):
        print("\nFQDN: " + self.fqdn)

    def displayManufact(self):
        print("\nManufacturer: " + self.manufact)

    def displayModel(self):
        print("\nModel: " + self.model)

    def displaySerialNo(self):
        print("\nSerial Number: " + self.serialNo)

    def displayCoreCount(self):
        print("\nCore Count: " + str(self.coreCount))

    def displayCoreModel(self):
        print("\nSerial Number: " + self.coreModel)

    def displayTotalMemory(self):
        print("\nTotal System Memory: " + str(self.totalMemory) + "GB")

    def displayRack(self):
        print("\nServer Rack ID: " + self.rack)

    def displayPosition(self):
        print("\nPosition of Machine in Rack: " + self.position)

    def displayUnits(self):
        print("\nHeight of Machine in Units: " + self.units)

    def displayAll(self):
        print("\nCurrent Machine:")
        print("===========================")
        self.displayIp()
        self.displayMac()
        self.displayFqdn()
        self.displayManufact()
        self.displayModel()
        self.displaySerialNo()
        print("==========================")
        print("\nCore & Memory Information:")
        print("==========================")
        self.displayCoreModel()
        self.displayCoreCount()
        self.displayTotalMemory()
        print("==========================")
        print("\nPhysical Information:")
        print("==========================")
        self.displayRack()
        self.displayPosition()
        self.displayUnits()

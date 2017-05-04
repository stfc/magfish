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
        print("\nIP Address:" + self.getIp())

    def displayIp(self):
        print("\nMAC Address:" + self.getMac())

    def displayFqdn(self):
        print("\nFQDN:" + self.getFqdn())

    def displayManufact(self):
        print("\nManufacturer:" + self.getManufact(self))

    def displayModel(self):
        print("\nModel:" + self.getModel())

    def displaySerialNo(self):
        print("\nSerial Number:" + self.getSerialNo())

    def displayCoreCount(self):
        print("\nCore Count:" + str(coreCount))

    def displayCoreModel(self):
        print("\nSerial Number:" + self.getCoreModel())

    def displayTotalMemory(self):
        print("\nTotal System Memory" + str(totalMemory) + "GB")

    def displayRack(self):
        print("\nServer Rack ID:" + self.getRack())

    def displayPosition(self):
        print("\nPosition of Machine in Rack:" + self.getPosition())

    def displayUnits(self):
        print("\nHeight of Machine in Units:" + self.getUnits())

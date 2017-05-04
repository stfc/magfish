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
        print("\nIP Address:" + ip)

    def displayIp(self):
        print("\nMAC Address:" + mac)

    def displayFqdn(self):
        print("\nFQDN:" + fqdn)

    def displayManufact(self):
        print("\nManufacturer:" + manufact)

    def displayModel(self):
        print("\nModel:" + model)

    def displaySerialNo(self):
        print("\nSerial Number:" + serialNo)

    def displayCoreCount(self):
        print("\nCore Count:" + str(coreCount))

    def displayCoreModel(self):
        print("\nSerial Number:" + coreModel)

    def displayTotalMemory(self):
        print("\nTotal System Memory" + str(totalMemory) + "GB")

    def displayRack(self):
        print("\nServer Rack ID:" + rack)

    def displayPosition(self):
        print("\nPosition of Machine in Rack:" + position)

    def displayUnits(self):
        print("\nHeight of Machine in Units:" + units)

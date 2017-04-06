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

    def getIp(self):
        return self.ip
    def setIp(self,ip):
        self.ip = ip
    def displayIp(self):
        print("\nIP Address:" + self.getIp())

    def getMac(self):
        return self.mac
    def setMac(self,mac):
        self.mac = mac
    def displayIp(self):
        print("\nMAC Address:" + self.getMac())

    def getFqdn(self):
        return self.fqdn
    def setFqdn(self,fqdn):
        self.fqdn = fqdn
    def displayFqdn(self):
        print("\nFQDN:" + self.getFqdn())

    def getManufact(self):
        return self.manufact
    def setManufact(self,manufact):
        self.manufact = manufact
    def displayManufact(self):
        print("\nManufacturer:" + self.getManufact())

    def getModel(self):
        return self.model
    def setModel(self,model):
        self.model = model
    def displayModel(self):
        print("\nmodel:" + self.getmodel())

    def getSerialNo(self):
        return self.serialNo
    def setSerialNo(self,serialNo):
        self.serialNo = serialNo
    def displaySerialNo(self):
        print("\nCore Model:" + self.getSerialNo())

    def getCoreCount(self):
        return self.coreCount
    def setCoreCount(self,coreCount):
        self.coreCount = coreCount
    def displayCoreCount(self):
        print("\nCore Count:" + str(coreCount))

    def getCoreModel(self):
        return self.coreModel
    def setCoreModel(self,coreModel):
        self.coreModel = coreModel
    def displayCoreModel(self):
        print("\nSerial Number:" + self.getCoreModel())

    def getTotalMemory(self):
        return self.totalMemory
    def setTotalMemory(self,totalMemory):
        self.totalMemory = totalMemory
    def displayTotalMemory(self):
        print("\nTotal System Memory" + str(totalMemory) + "GB")

    def getRack(self):
        return self.rack
    def setRack(self,rack):
        self.rack = rack
    def displayRack(self):
        print("\nServer Rack ID:" + self.getRack())

    def getPosition(self):
        return self.position
    def setPosition(self,position):
        self.position = position
    def displayPosition(self):
        print("\nPosition of Machine in Rack:" + self.getPosition())

    def getUnits(self):
        return self.Units
    def setUnits(self,Units):
        self.Units = Units
    def displayUnits(self):
        print("\nHeight of Machine in Units:" + self.getUnits())

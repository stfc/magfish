class Machine:

    ip = ""
    mac = ""

    fqdn = ""
    vendor = ""
    manufact = ""

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

    def getVendor(self):
        return self.vendor
    def setVendor(self,vendor):
        self.vendor = vendor
    def displayVendor(self):
        print("\nVendor:" + self.getVendor())

    def getManufact(self):
        return self.manufact
    def setManufact(self,manufact):
        self.manufact = manufact
    def displayManufact(self):
        print("\nManufacturer:" + self.getManufact())

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
<<<<<<< Updated upstream
    def displayPosition(self):
        print("\nPosition of Machine in Rack:" + self.getPosition())

    def getUnits(self):
        return self.Units
    def setUnits(self,Units):
        self.Units = Units
    def displayUnits(self):
        print("\nHeight of Machine in Units:" + self.getUnits())
=======
    def displayPosition():
        print("\nPosition of Machine in Rack:" + self.getPosition)

    def getUnits():
        return self.units
    def setUnits(units):
        self.units = units
    def displayUnits():
        print("\nHeight of Machine in Units:" + self.getUnits)
>>>>>>> Stashed changes

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

    def getIp():
        return self.ip
    def setIp(ip):
        self.ip = ip
    def displayIp():
        print("\nIP Address:" + self.getIp)

    def getMac():
        return self.mac
    def setMac(mac):
        self.mac = mac
    def displayIp():
        print("\nMAC Address:" + self.getMac)

    def getFqdn():
        return self.fqdn
    def setFqdn(fqdn):
        self.fqdn = fqdn
    def displayFqdn():
        print("\nFQDN:" + self.getFqdn)

    def getVendor():
        return self.vendor
    def setVendor(vendor):
        self.vendor = vendor
    def displayVendor():
        print("\nVendor:" + self.getVendor)

    def getManufact():
        return self.manufact
    def setManufact(manufact):
        self.manufact = manufact
    def displayManufact():
        print("\nManufacturer:" + self.getManufact)

    def getRack():
        return self.rack
    def setRack(rack):
        self.rack = rack
    def displayRack():
        print("\nServer Rack ID:" + self.getRack)

    def getPosition():
        return self.position
    def setPosition(position):
        self.position = position
    def displayPosition():
        print("\nPosition of Machine in Rack:" + self.getPosition)

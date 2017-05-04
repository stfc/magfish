class Machine:

    ip = ""
    mac = ""

    fqdn = ""
    manufact = ""
    model = ""

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

    def displayRack(self):
        print("\nServer Rack ID:" + rack)

    def displayPosition(self):
        print("\nPosition of Machine in Rack:" + position)

    def displayUnits(self):
        print("\nHeight of Machine in Units:" + units)

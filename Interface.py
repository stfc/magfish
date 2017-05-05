class Interface:

    id = -1
    mac = ""
    active = False;
    status = ""

    def __init__ (self,id,mac,active,status):
        self.id = id
        self.mac = mac;
        self.active = active;
        self.status = status;

    def displayId(self):
        print("\nID: " + str(self.id))

    def displayMac(self):
        print("\nMAC Address: " + self.mac)

    def displayStatus(self):
        print("\Status: " + str(self.status))

    def displayAll(self):
        print("\nInterface:")
        print("================")
        self.displayId()
        self.displayMac()
        self.displayStatus()
        print("================")

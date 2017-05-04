class Interface:

    id = -1
    mac = ""
    active = False;

    def __init__ (self,id,mac,active):
        self.id = id
        self.mac = mac;
        self.active = active;

    def displayId(self):
        print("\nID: " + str(self.id))

    def displayMac(self):
        print("\nMAC Address: " + self.mac)

    def displayActive(self):
        print("\nActive: " + str(self.active))

    def displayAll(self):
        print("\nInterface:")
        print("================")
        self.displayId()
        self.displayMac()
        self.displayActive()
        print("================")

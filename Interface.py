class Interface:

    id = -1
    mac = ""
    active = False;

    def __init__ (self,id,mac,active):
        self.id = id
        self.mac = mac;
        self.active = active;

    def displayId(self):
        print("\nID: " + str(id))

    def displayMac(self):
        print("\nMAC Address: " + mac)

    def displayActive(self):
        print("\nActive: " + str(active))

    def displayAll(self):
        print("\nInterface:")
        print("================")
        self.displayId()
        self.displayMac()
        self.displayActive()

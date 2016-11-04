class Machine:

    ip = ""

    manu = ""
    model = ""
    partNo = ""

    def __init__(self,ip):
        self.ip = ip

    def setManu(self,manu): self.manu = manu
    def getManu(self): return manu
    def displayManu(self): print("Manufacturer: " + self.manu)

    def setModel(self,model): self.model = model
    def getModel(self): return model
    def displayModel(self): print("Model: " + self.model)

    def setPartNo(self,partNo): self.partNo = partNo
    def getPartNo(self): return partNo
    def displayPartNo(self): print("Part Number: " + self.partNo)

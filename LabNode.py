class LabNode:
    def __init__(self, name, mac_addr, ip_addr):
        self.name = name
        self.mac_addr = mac_addr
        self.ip_addr = ip_addr
        self.labPosX = None
        self.labPosY = None

    def ipmiStatus(self):
        print('polling ipmi from machine', self.name)
        # Do IPMI magic and return
        return 'being real cool'

    def setDesc(self, desc):
        self.desc = desc

    def setLabPosition(self, y, x):
        self.labPosX = x
        self.labPosY = y


class Lab:
    def __init__(self, name, height, width):
        self.name = name
        self.nodeList = []
        self.height = height
        self.width = width
        self.racks = []
        
        # Initialize rack list
        for i in range(0, (int(height)*int(width))):
            print(i)
            self.racks.append(Rack(10))
            
    def addNode(self, labNode):
        self.nodeList.append(labNode)
        self.racks[((int(labNode.labPosY) - 1) * (int(self.width))) + (int(labNode.labPosX) - 1)].addNode(labNode)

    def getNode(self, i):
        return self.nodeList[i]

    def getNodes(self):
        return self.nodeList

    def getRack(self, y, x):
        print(y - 1, x - 1)
        return self.racks[((y-1) * int(self.width)) + (x-1)]


class Rack:
    def __init__(self, units):
        self.units = units
        self.nodeList = []

    def addNode(self, node):
        self.nodeList.append(node)

    def getNode(self, i):
        if (i < len(self.nodeList)) and (len(self.nodeList) != 0) :
            return self.nodeList[i];
        else :
            return None
    

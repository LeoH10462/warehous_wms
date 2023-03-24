class Item:

    def __init__(self, name, count=0, pallet=0, note='',
                 cost=0, sale=0, vendor='', vendorInv=''):
            self.ItemName = name
            self.ItemCount = count
            self.ItemPallet = pallet
            self.ItemNote = note
            self.ItemCost = cost
            self.ItemSale = sale
            self.ItemVendor = vendor
            self.ItemVendorInvoice = vendorInv

    # 物品名称
    def setName(self, name):
        self.ItemName = name

    # 物品数量
    def setCount(self, count):
        self.ItemCount = count

    # 物品总托盘数
    def setPallet(self, pallet):
        self.ItemName = pallet

    # 物品备注
    def setNote(self, note=""):
        self.ItemName = note

    # 物品成本
    def setCost(self, cost=0):
        self.ItemName = cost

    # 物品售价
    def setSale(self, sale):
        self.ItemName = sale

    # 物品供应商（派送公司）
    def setVendor(self, vendor=""):
        self.ItemVendor = vendor

    # 物品供应商账单号（派送公司账单）
    def setVendorInvoice(self, vendorInv):
        self.ItemVendorInvoice = vendorInv

    def getName(self):
        return self.ItemName

    def getCount(self):
        return self.ItemCount

    def getPallet(self):
        return self.ItemPallet

    def getNote(self):
        return self.ItemNote

    def getCost(self):
        return self.ItemCost

    def getSale(self):
        return self.ItemSale

    def getVendor(self):
        return self.getVendor

    def getVendorInv(self):
        return self.getVendorInv
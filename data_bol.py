CUSTOMER_LIST= []

# 此Item
class Item:
    #每个item的名称，数量，板数，备注，成本，售价，供应商，供应商账单
    def __init__(self, name='', count=0, pallet=0, note='',
                 cost=0, sale=0, vendor='', vendorInv='', status=''):
            self.ItemName = name
            self.ItemCount = count
            self.ItemPallet = pallet
            self.ItemNote = note
            self.ItemCost = cost
            self.ItemSale = sale
            self.ItemVendor = vendor
            self.ItemVendorInvoice = vendorInv
            self.ItemStatus = status

    # 物品名称
    def setName(self, name):
        self.ItemName = name

    def getName(self):
        return self.ItemName
    
    # 物品数量
    def setCount(self, count):
        self.ItemCount = count

    def getCount(self):
        return self.ItemCount
    
    # 物品总托盘数
    def setPallet(self, pallet):
        self.ItemPallet = pallet

    def getPallet(self):
        return self.ItemPallet
    
    # 物品备注
    def setNote(self, note=""):
        self.ItemNote = note

    def getNote(self):
        return self.ItemNote
    
    # 物品成本
    def setCost(self, cost=0):
        self.ItemCost = cost

    def getCost(self):
        return self.ItemCost
    
    # 物品售价
    def setSale(self, sale):
        self.ItemSale = sale

    def getSale(self):
        return self.ItemSale
    
    # 物品供应商（派送公司）
    def setVendor(self, vendor=""):
        self.ItemVendor = vendor

    def getVendor(self):
        return self.ItemVendor
    
    # 物品供应商账单号（派送公司账单）
    def setVendorInvoice(self, vendorInv):
        self.ItemVendorInvoice = vendorInv

    def getVendorInvoice(self):
        return self.ItemVendorInvoice
    
    # 物品状态设置（存仓（一件代发），暂扣，自提，改UPS，改Ama，客户发送，已发送）
    def setStatus(self, status):
        self.ItemStatus = status

    def getStatus(self):
        return self.ItemStatus
    
    def __repr__(self):
        return f"{self.ItemName} {self.ItemCount}pc {self.ItemPallet}P \
${self.ItemCost} ${self.ItemSale} {self.ItemVendor}"


class Bol():
    #一条货柜的后端处理基本信息，货柜号，提单号，ETA，拖柜卡车公司，备注，客户，货物列表
    def __init__(self, container='', mbl='', eta='', dateTime="", truck='', 
                note='', customer=''):
        
        self.Container = container
        self.MBL = mbl
        self.ETA = eta # 预计到达日
        self.DateTime = dateTime #柜子到仓日 or 卸柜日
        self.Truck = truck
        self.Note = note
        self.Customer = customer
        self.Items = []
        self.Ama_num =0
        self.Ups_num =0
        self.Oth_num =0
        self.total_num = 0

    # 添加item到当前货柜的总货物列表
    def addItem(self, item):
        self.Items.append(item)
    
    def getItems(self):
        return self.Items
    
    # 柜号
    def setContainer(self, contain):
        self.Container = contain

    def getContainer(self):
        return self.Container
    
    # mbl 提单号
    def setMbl(self, mbl):
        self.MBL = mbl
    
    def getMbl(self):
        return self.MBL
    
    # eta 预计到达日期
    def setEta(self, eta):
        self.ETA = eta

    def getEta(self):
        return self.ETA
    
    # dateTime 柜子到仓日 or 卸柜日
    def setDateTime(self, dateTime):
        self.DateTime = dateTime
    
    def getDateTime(self):
        return self.DateTime
    
    # truck 拖柜卡车公司
    def setTruck(self, truck):
        self.Truck = truck

    def getTruck(self):
        return self.Truck
    
    # customer 客户名称，货柜所属客户
    def setCustomer(self, custom):
        self.Customer = custom
    
    def getCustomer(self):
        return self.Customer
    
    # note 备注
    def setNote(self, note):
        self.Note = note

    def getNote(self):
        return self.Note
    
    # ama_num ama数量
    def setAma_num(self, ama_num):
        self.Ama_num = ama_num
        self.update_total_num()

    def getAma_num(self):
        return self.Ama_num
    
    # ups_num ups数量
    def setUps_num(self, ups_num):
        self.Ups_num = ups_num
        self.update_total_num()
    
    def getUps_num(self):
        return self.Ups_num
    
    # oth_num 其他数量（自提，改UPS，改Ama，客户发送，已发送）
    def setOth_num(self, oth_num):
        self.Oth_num = oth_num
        self.update_total_num()
    
    def getOth_num(self):
        return self.Oth_num
    
    # total_num 货物总数量
    def update_total_num(self):
        self.total_num = self.Ama_num + self.Ups_num + self.Oth_num

    def getTotal_num(self):
        return self.total_num
    
    # 单个提单信息列表
    def printInfo(self):
        print(f"Customer: [{self.Customer}] [{self.ETA}] [{self.MBL}] \
[{self.Container}] [{self.Truck}] [{self.Note}] {list(self.Items)}")

    def __repr__(self):
        return f"Customer: [{self.Customer}] [{self.ETA}] [{self.MBL}] \
[{self.Container}] [{self.Truck}] [{self.Note}] {list(self.Items)}"

    def pre_print(self):
        print(f"Customer: [{self.Customer}] [{self.ETA}] [{self.MBL}] \
[{self.Container}] [{self.Truck}] Ama:[{self.Ama_num}] UPS:[{self.Ups_num}] Oth:[{self.Oth_num}]")

    def pos_print(self):
        print(f"Customer: [{self.Customer}] [{self.ETA}] [{self.MBL}] \
[{self.Container}] [{self.Note}] Item:[{list(self.Ama_num)}]")




testBol = Bol()
testBol.setTruck("FAE")
testBol.setContainer("CMDUS123")
testBol.setCustomer("wd")
testBol.setMbl("123123")
testBol.setAma_num(111)
testBol.setUps_num(222)
testBol.setOth_num(333)
#testBol.pre_print()





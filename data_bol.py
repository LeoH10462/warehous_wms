CUSTOMER_LIST= []
class Item:
    #每个item的名称，数量，板数，备注，成本，售价，供应商，供应商账单
    def __init__(self, name='', count=0, pallet=0, note='',
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

    def __repr__(self):
        return f"{self.ItemName} {self.ItemCount}pc {self.ItemPallet}P \
${self.ItemCost} ${self.ItemSale} {self.ItemVendor}"


class Bol():
    #一条货柜的后端处理基本信息，货柜号，提单号，ETA，拖柜卡车公司，备注，客户，货物列表
    def __init__(self, container='', mbl='', eta='', truck='', note='', customer=''):
        self.Container = container
        self.MBL = mbl
        self.ETA = eta
        self.Truck = truck
        self.Note = note
        self.Customer = customer
        self.Items = []
        self.Ama_num =0
        self.Ups_num =0
        self.Oth_num =0
        self.total_num = self.Ama_num + self.Ups_num + self.Oth_num

    # 添加item到当前货柜的总货物列表
    def addItem(self, item):
        self.Items.append(item)

    def setContainer(self, contain):
        self.Container = contain

    def setmbl(self, mbl):
        self.MBL = mbl

    def setEta(self, eta):
        self.ETA = eta
    
    def setTruck(self, truck):
        self.Truck = truck

    def setCustomer(self, custom):
        self.Customer = custom

    def setNote(self, note):
        self.Note = note

    def setAma_num(self, ama_num):
        self.Ama_num = ama_num

    def setUps_num(self, ups_num):
        self.Ups_num = ups_num

    def setOth_num(self, oth_num):
        self.Oth_num = oth_num
    

    def printInfo(self):
        print(f"Customer: [{self.Customer}] [{self.ETA}] [{self.MBL}] \
[{self.Container}] [{self.Truck}] [{self.Note}] {list(self.Items)}")

    def __repr__(self):
        return f"Customer: [{self.Customer}] [{self.ETA}] [{self.MBL}] \
[{self.Container}] [{self.Truck}] [{self.Note}] {list(self.Items)}"

#from item import item
from data_class.item import Item

class Bol:

    def __init__(self, container, mbl, eta, truck, note, customer):
        self.Container = container
        self.MBL = mbl
        self.ETA = eta
        self.Truck = truck
        self.Note = note
        self.Customer = customer

    def setAmazon(self, number):
        amazon = Item()

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

    def printInfo(self):
        print("Customer: ["+ self.Customer + "]"
                "\nETA: ["+ self.ETA +"]"
                "\nMBL: ["+ self.MBL +"]"
                "\nContainer: ["+ self.Container + "]"
                "\nTruck: [" + self.Truck + "]"
                "\nNote: [" + self.Note + "]")

    def printTest(self):
        print("here!")
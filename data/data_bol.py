from item import item

class Bol:


    def __init__(self, container, mbl, eta, truck, note):
        self.Container = container
        self.MBL = mbl
        self.ETA = eta
        self.Truck = truck
        self.Note = note

    def setAmazon(self, number):
        amazon = item()
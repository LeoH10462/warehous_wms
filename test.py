
from data_bol import Bol
from data_bol import Item

bol_list = []
eahBol = Bol("CMAU7518336","CMDUCNXD214700", "2021-11-16",
            "FAE", "", "委达")
eahBol.printInfo()

amazom_item = Item()
amazom_item.setName('ONT8')
amazom_item.setCount(100)
amazom_item.setPallet(10)
eahBol.addItem(amazom_item)
eahBol.printInfo()

am_item2 = Item()
am_item2.setName('GYR3')
am_item2.setCount(200)
am_item2.setPallet(20)
eahBol.addItem(am_item2)
eahBol.printInfo()



















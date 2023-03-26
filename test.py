import numpy as np
from data_bol import Bol

x = np.arange(10)
myBol = Bol("CMAU7518336","CMDUCNXD214700", "2021-11-16",
            "FAE", "", "委达")
myBol.printInfo()

print(x)


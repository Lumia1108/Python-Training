import os, usecsv
import numpy as np
path = os.getcwd()
os.chdir(path + '\\numpy')

data = np.array(usecsv.switchtonum(usecsv.opencsv('data.csv')))
print(data)
print(data > 5)
data[data > 5] = 5
usecsv.writecsv('data.csv', list(data))
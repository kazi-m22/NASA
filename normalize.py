from pandas import read_csv
import os
import matplotlib.pyplot as plt
import numpy as np
from pandas import set_option
from sklearn.preprocessing import Normalizer



os.chdir(".//Data")
data = read_csv('THU_U_day.csv')

array = data.values

x = array[:,:]


scaler = Normalizer().fit(x)
normalizedx = scaler.transform(x)

print(normalizedx[0:5,:])
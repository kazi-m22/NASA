import tifffile
import os
import matplotlib.pyplot as plt

os.chdir('E:\\Projects\\NASA\\Data\\Image data')
a = tifffile.imread('E:\\Projects\\NASA\\Data\\Image data\\Hansen_GFC2015_lossyear_30N_090E.tif')
b = a[:10000, :10000]
tifffile.imshow(b)
plt.show()
from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = '1.txt'
names = ['Year', 'MonthOfYear', 'DayOfMonth', 'DayOfYear', 'DayOfCentury' ,'AirPressure(hPa)' ,'AirTemperature(C)', 'AirTemperatureHygroClip(C)', 'RelativeHumiditywrtWater(%)' ,'RelativeHumidity(%)', 'WindSpeed(m/s)' ,'WindDirection(d)', 'ShortwaveRadiationDown(W/m2)', 'ShortwaveRadiationDownCor(W/m2)' ,'ShortwaveRadiationUp(W/m2)', 'ShortwaveRadiationUp_Cor(W/m2)' ,'Albedo_theta<70d LongwaveRadiationDown(W/m2)', 'LongwaveRadiationUp(W/m2)', 'CloudCover' ,'SurfaceTemperature(C)', 'HeightSensorBoom(m)', 'HeightStakes(m)' ,'DepthPressureTransducer(m)', 'DepthPressureTransducer_Cor(m)', 'AblationPressureTransducer(mm)', 'IceTemperature1(C)' ,'IceTemperature2(C)' ,'IceTemperature3(C)', 'IceTemperature4(C)', 'IceTemperature5(C)', 'IceTemperature6(C)', 'IceTemperature7(C)' ,'IceTemperature8(C)', 'TiltToEast(d)', 'TiltToNorth(d)' ,'LatitudeGPS_HDOP<1(ddmm)', 'LongitudeGPS_HDOP<1(ddmm)', 'ElevationGPS_HDOP<1(m)' ,'HorDilOfPrecGPS_HDOP<1 LoggerTemperature(C)', 'FanCurrent(mA) BatteryVoltage(V)']
data = pd.read_table(files, names = names)
correlation = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlation, vmin = -.01, vmax = .1000)
fig.colorbar(cax)
ticks = np.arange(0,9,len(names))
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()
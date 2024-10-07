from datetime import datetime
import pandas as pd 
import numpy as np 
from statsmodels.tsa.stattools import  adfuller
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/AileenNielsen/TimeSeriesAnalysisWithPython/master/data/AirPassengers.csv")

#string to date format
df['Month'] = pd.to_datetime(df['Month'])
df = df.set_index(['Month'])
df.head(5)

plt.figure(figsize=(15,7))
plt.xlabel("Date")
plt.ylabel("passengers")
plt.plot(df)
plt.show()

df["mean"] = df["#Passengers"].rolling(window=12).mean()
df["variance"] = df["#Passengers"].rolling(window=12).std()

plt.plot(figsize=(15 , 7))
plt.plot(df["mean"] , c = 'r')
plt.plot(df["variance"] , c = 'g')
plt.legend(loc = 'best')
plt.show()

dftest = adfuller(df["#Passengers"] , autolag = 'AIC')
print('ADF Statistic: %f' % dftest[0])
print('p-value: %f' % dftest[1])
print('Critical Values:')
for key, value in dftest[4].items():
    print('\t%s: %.3f' % (key, value))

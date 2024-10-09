from datetime import datetime
import pandas as pd 
import numpy as np 
from sqlalchemy import false
from statsmodels.tsa.stattools import  adfuller
import matplotlib.pyplot as plt
#download our data
df = pd.read_csv("https://raw.githubusercontent.com/AileenNielsen/TimeSeriesAnalysisWithPython/master/data/AirPassengers.csv")
#string to date format
df['Month'] = pd.to_datetime(df['Month'])
df = df.set_index(['Month'])
df.head(5)
#plot the series
plt.figure(figsize=(15,7))
plt.xlabel("Date")
plt.ylabel("passengers")
plt.plot(df)
plt.show()
#calculate the mean and the variance  of the series
df["mean"] = df["#Passengers"].rolling(window=12).mean()
df["variance"] = df["#Passengers"].rolling(window=12).std()
#plot the result
plt.plot(figsize=(15 , 7))
plt.plot(df["mean"] , c = 'r')
plt.plot(df["variance"] , c = 'g')
plt.legend(loc = 'best')
plt.show()
# we test if the series is stationary  or not
dftest = adfuller(df["#Passengers"] , autolag = 'AIC')
print('ADF Statistic: %f' % dftest[0])
print('p-value: %f' % dftest[1])
print('Critical Values:')
for key, value in dftest[4].items():
    print('\t%s: %.3f' % (key, value))

# so in this code we use SARIMA model to forecast  the series


from  statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX


#plot the acf and pacf of the series
plt.figure(figsize =(10,5))

plot_acf(df["#Passengers"], lags=20)
plt.show()
plt.figure(figsize =(10,5))
plot_pacf(df["#Passengers"], lags=20)
plt.show()

# as  we can see from the acf and pacf plot , we can see that p=1 and d= 1(data is not stationary)and q=0
p , q , d = 1 , 0 , 1
P , Q , D , S = 1, 1, 0, 12
# we use the SARIMA model to forecast the series
model = SARIMAX(df["#Passengers"] ,order=(p ,q , d) , seasonal_order=(P,Q,D,S))
result = model.fit()

print(result.summary())

n_forecast = 24  

# Obtain the forecasts
forecast = result.get_forecast(steps=n_forecast)

# Create a time index for future dates
forecast_index = pd.date_range(df.index[-1] + pd.offsets.MonthEnd(), periods=n_forecast, freq='M')

# Extract the forecast values and convert them into a Pandas series
forecast_series = pd.Series(forecast.predicted_mean, index=forecast_index)

# Visualize the forecasts and confidence intervals
plt.figure(figsize=(10, 6))
plt.plot(df['#Passengers'], label='Observed')
plt.plot(forecast_series, label='Forecast', color='red')
plt.fill_between(forecast_index, 
                 forecast.conf_int().iloc[:, 0], 
                 forecast.conf_int().iloc[:, 1], 
                 color='pink', alpha=0.3)  # Confidence interval
plt.title('SARIMA Model Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()









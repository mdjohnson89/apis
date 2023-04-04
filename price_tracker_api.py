import json
import requests
import matplotlib.pyplot as plt
from datetime import date


symbol = input('Which stock would you like to follow? (Enter stock symbol): ')
num_days = int(input('How many days back? : '))
API_KEY = 'WQT4AM73F83AQIO6'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
table = response.json()

time_series_daily = dict(table['Time Series (Daily)'])
dates = list(time_series_daily.keys())


# Here, we separate out all the close values and then select the range we want from num_days
# This could be accomplished with a list comprehension to be more efficient. 
# Showing here in two steps for clarity
close_values = []
values = []

for key in time_series_daily:
    close_values.append(float(time_series_daily[key]['4. close']))
for i in range(num_days):
    values.append(close_values[i])

# The x_data isn't numeric, so the ticks will be based off of num_days
if num_days < 10:
    x_ticks = list(range(0, num_days))
else:
    x_ticks = list(range(0, num_days, 2))
# We read in the dates in a string, and want them to display that way

x_data = dates[0:num_days]

# Labeling and setting the ticks
plt.figure(figsize=(10,8))
plt.tight_layout()
plt.title(f'{symbol} price from past {num_days} days ending {dates[0]}')
plt.xlabel('Dates')
plt.ylabel(f'Price of {symbol} in USD')
plt.yticks= range(round(close_values[0]), round(close_values[-1]), 5)
plt.xticks(x_ticks, rotation=45)

#plt.gca()(get current axis)
plt.gca().invert_xaxis()
plt.grid()
plt.plot(x_data, values)
plt.show()
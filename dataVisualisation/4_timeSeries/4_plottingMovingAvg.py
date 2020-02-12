import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/stocks.csv', index_col = 'Date')

aapl = stocks['AAPL']
# convert aapl index to datatime64
aapl.index = pd.to_datetime(aapl.index)
# print(aapl.index)
mean_30 = aapl.resample('30D').mean()
# print(mean_30)
mean_75 = aapl.resample('75D').mean()
mean_125 = aapl.resample('125D').mean()
mean_250 = aapl.resample('250D').mean()



# Plot the 30-day moving average in the top left subplot in green
plt.subplot(2,2,1)
plt.plot(mean_30, color='green')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')

# Plot the 75-day moving average in the top right subplot in red
plt.subplot(2,2,2)
plt.plot(mean_75, 'red')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

# Plot the 125-day moving average in the bottom left subplot in magenta
plt.subplot(2, 2, 3)
plt.plot(mean_125, color='magenta')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

# Plot the 250-day moving average in the bottom right subplot in cyan
plt.subplot(2,2,4)
plt.plot(mean_250, color='cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

# Display the plot
plt.show()

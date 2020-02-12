import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/stocks.csv', index_col = 'Date')

aapl = stocks['AAPL']
# convert aapl index to datatime64
aapl.index = pd.to_datetime(aapl.index)
# print(aapl.index)
std_30 = aapl.resample('30D').std()
# print(mean_30)
std_75 = aapl.resample('75D').std()
std_125 = aapl.resample('125D').std()
std_250 = aapl.resample('250D').std()

# Plot std_30 in red
plt.plot(std_30, color='red', label='30d')

# Plot std_75 in cyan
plt.plot(std_75, color='cyan', label='75d')

# Plot std_125 in green
plt.plot(std_125, color='green', label='125d')

# Plot std_250 in magenta
plt.plot(std_250, color='magenta', label='250d')

# Add a legend to the upper left
plt.legend(loc='upper left')

# Add a title
plt.title('Moving standard deviations')

# Display the plot
plt.show()
plt.savefig('/Users/apple/desktop/dataVisualisation/4_timeSeries/5_movingStd.png')

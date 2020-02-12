import pandas as pd

stock = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/stocks.csv')
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot the aapl time series in blue
plt.plot(stock['AAPL'], color='blue', label='AAPL')

# Plot the ibm time series in green
plt.plot(stock['IBM'], color='green', label='IBM')

# Plot the csco time series in red
plt.plot(stock['CSCO'], color='red', label='CSCO')

# Plot the msft time series in magenta
plt.plot(stock['MSFT'], color='magenta', label='MSFT')


# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')

# Specify the orientation of the xticks
plt.xticks(rotation=60)

# Display the plot
plt.show()

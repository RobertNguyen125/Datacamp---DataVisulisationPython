import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/stocks.csv', index_col = 'Date')

aapl = stocks['AAPL']
view_1 = aapl['2007-11':'2008-05']
view_2 = aapl['2008-01':'2008-02']

# plot the entire aapl series and view_1 to compare between these 2
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL:2001-2011')

# Specify the axes
plt.axes((.25,.5,.35,.35))

#plot view_1 series
plt.plot(view_1, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()

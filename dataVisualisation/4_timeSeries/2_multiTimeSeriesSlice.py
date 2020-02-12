import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/stocks.csv', index_col = 'Date')
print(stocks.head())

# extract Series 'aapl' from dataframe:
aapl = stocks['AAPL']
print(aapl.shape)

# extract price from Nov 2007 - Apr 2008: view_1
view_1 = aapl['2007-11':'2008-05']
# print(view_1)
# Create subplot in the top subplot
plt.subplot(2,1,1)
plt.plot(view_1, color='red')
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.xticks(rotation=45)

view_2 = aapl['2008-01':'2008-02']
# print(view_2)
# Create subplot in the bottom in green
plt.subplot(2,1,2)
plt.plot(view_2, color='green')
plt.title('AAPL: Jan. 2008')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/auto-mpg.csv')

sns.lmplot(x='weight', y='hp', data=auto)
plt.show()


# --------------------------------------------------------------------------------
# plotting residuals of regression
sns.residplot(x='hp', y='mpg', data=auto, color='green')
plt.show()

# --------------------------------------------------------------------------------
# higher order regression
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, color='blue', scatter=None, label='First Order',order=1)

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, color='green',scatter=None, label='Second Order',order=2)


# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()

# --------------------------------------------------------------------------------
# Grouping linear regressions by hue
# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(data=auto, x='weight', y='hp', hue = 'origin', palette='Set1')

# Display the plot
plt.show()

# --------------------------------------------------------------------------------
# Grouping linear regressions by row or column
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(data=auto, x='weight', y='hp', hue='origin', row='origin')

# Display the plot
plt.show()

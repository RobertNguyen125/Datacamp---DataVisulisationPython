import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/auto-mpg.csv')

# plotting joint distribution
# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot(x='hp', y='mpg',data=auto)
# Display the plot
plt.show()

# ------------------------------------------------------------------------------
# hex box
# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
sns.jointplot(x='hp', y='mpg',data=auto, kind ='hex')
# Display the plot
plt.show()

# ------------------------------------------------------------------------------
# Plotting distributions pairwise (1)
# will automatically plot categorical data, non-categorical will be plotted in square grid of subplots
# Plot the pairwise joint distributions from the DataFrame
sns.pairplot(auto)
# Display the plot
plt.show()

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto, kind='reg', hue='origin')
# Display the plot
plt.show()

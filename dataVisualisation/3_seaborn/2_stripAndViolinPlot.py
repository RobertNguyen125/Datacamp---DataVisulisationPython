import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('/Users/apple/desktop/dataVisualisation/dataset/auto-mpg.csv')

# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=3)

# Display the plot
plt.show()


# --------------------------------------------------------------------------------
# swarmplot()
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(y='cyl', x='hp', data=auto, hue='origin', orient='h')

# Display the plot
plt.show()

# --------------------------------------------------------------------------------
# violinplot()
# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto, inner=None, color='lightgray')


# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', data=auto,color='lightgray', jitter=True, size=1.5)

# Display the plot
plt.show()

import matplotlib.pyplot as plt
img = plt.imread('/Users/apple/desktop/dataVisualisation/dataset/Astronaut.jpg')
print(img.shape)

plt.imshow(img)
plt.axis('off')
plt.show()

# --------------------------------------------------------------------------------

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()

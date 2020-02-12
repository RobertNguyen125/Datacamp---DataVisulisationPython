import matplotlib.pyplot as plt
import numpy as np
image = plt.imread('/Users/apple/desktop/dataVisualisation/dataset/hs-2004-32-b-small_web.jpg')

# display image in top subplot
plt.subplot(2,1,1)
plt.title('Original')
plt.axis('off')
plt.imshow(image)

# extract 2-D array of RGB:
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]

red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()

#overlay hists of the pixels of each color in the bottom plot
plt.subplot(2,1,2)
plt.title('Histogram from color image')
plt.xlim((0,256))
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha =0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha =0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha =0.2)
# plt.show()

# --------------------------------------------------------------------------------
# Generate a 2-D histogram of the red and green pixels
plt.subplot(2,2,1)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('red')
plt.ylabel('green')
plt.hist2d(red_pixels, green_pixels, bins=(32,32))

# Generate a 2-D histogram of the green and blue pixels
plt.subplot(2,2,2)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('green')
plt.ylabel('blue')
plt.hist2d(green_pixels, blue_pixels, bins=(32,32))

# Generate a 2-D histogram of the blue and red pixels
plt.subplot(2,2,3)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('blue')
plt.ylabel('red')
plt.hist2d(blue_pixels,red_pixels,bins=(32,32))

# Display the plot
plt.show()

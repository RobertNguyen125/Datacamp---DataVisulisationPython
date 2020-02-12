# extract histogram from a grayscale imange
import matplotlib.pyplot as plt

image = plt.imread('/Users/apple/desktop/dataVisualisation/dataset/640px-Unequalized_Hawkes_Bay_NZ.jpg')

# display image on top of subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original Image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# flattening image into 1 dimention: pixels
pixels = image.flatten()

# display a hist in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0,256),normed=True, color='red', alpha =0.4)

plt.show()

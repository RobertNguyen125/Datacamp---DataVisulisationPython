# CDF: Cumulative Distribution Function
# PDF: Probability Density Function
import matplotlib.pyplot as plt
image = plt.imread('/Users/apple/desktop/dataVisualisation/dataset/640px-Unequalized_Hawkes_Bay_NZ.jpg')

# display image on top of subplot using color map 'gray'
plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# flattening image into 1 dimention: pixels
pixels = image.flatten()

# display a hist of pixels  in the bottom plot
plt.subplot(2,1,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), alpha=0.4, color='red', normed=False)
plt.grid('off')
# call plt.twinx() to overlay PDF in the
plt.twinx()
#plot CDF
cdf = plt.hist(pixels, bins=64, range=(0,256), alpha=0.4, color='blue', cumulative=True, normed=True)

plt.xlim((0,256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()



# # Display image in top subplot using color map 'gray'
# plt.subplot(2,1,1)
# plt.imshow(image, cmap='gray')
# plt.title('Original image')
# plt.axis('off')
#
# # Flatten the image into 1 dimension: pixels
# pixels = image.flatten()
#
# # Display a histogram of the pixels in the bottom subplot
# plt.subplot(2,1,2)
# pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False,
#                color='red', alpha=0.4)
# plt.grid('off')
#
# # Use plt.twinx() to overlay the CDF in the bottom subplot
# plt.twinx()
#
# # Display a cumulative histogram of the pixels
# cdf = plt.hist(pixels, bins=64, range=(0,256),
#                cumulative=True, normed=True,
#                color='blue', alpha=0.4)
#
# # Specify x-axis range, hide axes, add title and display plot
# plt.xlim((0,256))
# plt.grid('off')
# plt.title('PDF & CDF (original image)')
# plt.show()

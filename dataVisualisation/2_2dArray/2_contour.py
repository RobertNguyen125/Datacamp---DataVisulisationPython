import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]])
plt.pcolor(A, cmap='Blues')
plt.colorbar()
plt.show()

# ------------------------------------------------------------------------------------
the X,Y,Z arrays from datacamp were too large to extract so below is the code only
# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(X,Y,Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X,Y,Z,20)

# Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contour(X,Y,Z)

# Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contour(X,Y,Z,20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

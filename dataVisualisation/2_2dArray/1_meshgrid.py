import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2,2,3)
v = np.linspace(-1,1,5)
X,Y = np.meshgrid(u,v)
Z = X**2/25 + Y**2/4

print('Z:\n', Z)
plt.set_cmap('gist_gray')
plt.pcolor(Z)
plt.show()

# --------------------------------------------------------------------------------

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u,v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2))

# Display the resulting image with pcolor()
plt.pcolor(Z)
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('/Users/apple/desktop/dataVisualisation/2_2dArray/1_meshgrid.jpeg')

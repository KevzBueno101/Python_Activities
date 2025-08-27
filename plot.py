import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cone surface
z = np.linspace(0, 60, 100)
theta = np.linspace(0, 2 * np.pi, 100)
Z, Theta = np.meshgrid(z, theta)
R = 0.5 * Z
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

ax.plot_surface(X, Y, Z, color='green', alpha=0.6, edgecolor='none')

# Draw height line (z-axis)
ax.plot([0, 0], [0, 0], [0, 60], color='red', linewidth=2)
ax.text(0, 0, 30, 'Height = 60 cm', color='red')

# Draw radius line at top of cone
ax.plot([0, 30], [0, 0], [60, 60], color='blue', linewidth=2)
ax.text(15, 0, 62, 'Radius = 30 cm', color='blue')

# Labels for tip and top
ax.text(0, 0, 0, 'Tip (0,0,0)', color='black')
ax.text(0, 0, 60, 'Top (z=60 cm)', color='black')

# Axis labels and title
ax.set_title('Labeled 3D View of Conical Tree Hole')
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Depth (cm)')

plt.show()
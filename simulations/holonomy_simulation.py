"""
Holonomy Evolution via Parallel Transport

Simulates the rotation of a tangent vector transported around a loop
on a curved surface using discrete parallel transport.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define loop: circle in parameter space
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Initial vector
v0 = np.array([1.0, 0.0])
vectors = [v0]

# Simulate parallel transport (naive discrete version)
for i in range(1, len(theta)):
    # Tangent to path
    dx = x[i] - x[i-1]
    dy = y[i] - y[i-1]
    tangent = np.array([dx, dy])
    tangent /= np.linalg.norm(tangent)

    # Rotate vector to stay parallel (project onto tangent plane)
    v_prev = vectors[-1]
    v_new = v_prev - np.dot(v_prev, tangent) * tangent
    v_new /= np.linalg.norm(v_new)
    vectors.append(v_new)

vectors = np.array(vectors)

# Plot loop and transported vectors
plt.figure(figsize=(6,6))
plt.plot(x, y, 'k--', label='Loop')
for i in range(0, len(x), 10):
    plt.quiver(x[i], y[i], vectors[i,0], vectors[i,1], color='blue', scale=10)

plt.title("Parallel Transport Around a Loop")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.savefig("figures/holonomy_loop.png", dpi=300)
plt.show()


"""
Connection Evolution Simulation

This script models the time evolution of geometric and internal connections,
represented by A(α) and A(β), using complex-valued functions. Outputs include
real and imaginary components plotted over time.
"""

import numpy as np
import matplotlib.pyplot as plt

   
t_max = 10
resolution = 1000
t = np.linspace(0, t_max, resolution)

A_alpha = np.sin(t) + 1j * np.cos(t)         # Geometric connection
A_beta = np.exp(1j * t)                      # Internal connection

if __name__ == "__main__":
plt.plot(t, A_alpha.real, label='Re[A(α)]')
plt.plot(t, A_alpha.imag, label='Im[A(α)]')
plt.plot(t, A_beta.real, label='Re[A(β)]', linestyle='--')
plt.plot(t, A_beta.imag, label='Im[A(β)]', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Evolution of A(α) and A(β) Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/connection_evolution.png", dpi=300)
plt.show()


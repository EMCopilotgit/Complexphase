# Complexphase
# Complexphase

This directory contains simulation code and visualizations related to the time evolution of geometric and internal phase connections, denoted as \( A(\alpha) \) and \( A(\beta) \), respectively. These simulations support the theoretical framework presented in the manuscript and illustrate dynamic behaviors such as holonomy, phase accumulation, and spike-based encoding.

## Contents

- `connection_evolution.py`  
  Simulates the time-dependent behavior of \( A(\alpha) \) and \( A(\beta) \) using complex-valued functions. Outputs include real and imaginary components plotted over time.

- `spike_trains.py`  
  Generates raster plots of spike trains across neurons using the Brian2 simulator. Demonstrates how phase information can be encoded in spike timing.

- `figures/`  
  Contains representative output plots from the simulations, suitable for embedding in the manuscript.

## Requirements

- Python 3.8+
- `matplotlib`
- `numpy`
- `brian2` (for spike train simulation)

Install dependencies with:

```bash
pip install matplotlib numpy brian2

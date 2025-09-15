"""
Spike Train Simulation using Brian2

This script generates a raster plot of spike trains across neurons,
illustrating how phase information can be encoded in spike timing.
"""

# Define neuron model and parameters

from brian2 import *

# Neuron model
tau = 10*ms
eqs = '''
dv/dt = (I - v)/tau : volt
I : volt
'''

# Create neurons
G = NeuronGroup(5, eqs, threshold='v > -50*mV', reset='v = -70*mV', method='exact')
G.I = [-55, -54, -53, -52, -51]*mV
G.v = -70*mV

# Monitor spikes
M = SpikeMonitor(G)

if __name__ == "__main__":
    run(100*ms)
    plt.plot(M.t/ms, M.i, '.k')
    plt.xlabel('Time (ms)')
    plt.ylabel('Neuron index')
    plt.title('Spike Train Raster Plot')
    plt.grid(True)

    # Save figure to figures/ folder
    plt.savefig("figures/spike_train_raster.png", dpi=300)
    plt.show()


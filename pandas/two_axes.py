import numpy as np
import matplotlib.pyplot as plt
# Create a figure with 1 row, 2 columns of subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5)) # 'axes' is now an array of Axes objects

# Plot on the first Axes (left subplot)
axes[0].plot(np.random.rand(10), color='red')
axes[0].set_title('Random Data 1')
axes[0].set_xlabel('Index')
axes[0].set_ylabel('Value')

# Plot on the second Axes (right subplot)
axes[1].hist(np.random.randn(100), bins=10, color='green', alpha=0.7)
axes[1].set_title('Histogram of Random Normal Data')
axes[1].set_xlabel('Value')
axes[1].set_ylabel('Frequency')

fig.suptitle('Two Subplots in One Figure', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent suptitle overlap

plt.show()
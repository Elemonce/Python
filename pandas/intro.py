import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # Just to show it's used with pandas

# Create some sample data
data = {'x': np.linspace(0, 10, 100), 'y': np.sin(np.linspace(0, 10, 100))}
df = pd.DataFrame(data)

# Create a figure and a single set of axes
fig, ax = plt.subplots(figsize=(8, 5)) # Set figure size to 8x5 inches

# --- Operations on the Axes object (ax) ---
df.plot(x='x', y='y', ax=ax, label='Sine Wave', color='blue') # Plot data onto 'ax'
ax.set_title('My First Matplotlib Plot (on ax)')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()
ax.set_ylim(-1.5, 1.5) # Set y-axis limits

# --- Operations on the Figure object (fig) ---
fig.suptitle('Overall Figure Title', fontsize=16, color='darkred') # Title for the entire figure
fig.patch.set_facecolor('lightyellow') # Set background color of the figure

# Display the plot
plt.show()
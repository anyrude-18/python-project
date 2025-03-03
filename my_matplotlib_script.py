import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Sample Data
x = np.linspace(0, 10, 100)
y = np.sin(x)
bar_labels = ['A', 'B', 'C', 'D']
bar_values = [10, 20, 15, 30]
hist_data = np.random.randn(1000)
scatter_x = np.random.rand(50)
scatter_y = np.random.rand(50)
pie_sizes = [25, 35, 20, 20]

# Create a 2-row, 5-column grid of subplots
fig, axes = plt.subplots(2, 5, figsize=(18, 8))

# ---------- ANIMATED PLOT (Line Plot) ----------
line, = axes[0, 0].plot(x, np.sin(x), color='b')
axes[0, 0].set_title("Animated Line Plot")

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Update y-data
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# ---------- STATIC PLOTS ----------
# Scatter Plot
axes[0, 1].scatter(scatter_x, scatter_y, color='r', alpha=0.6)
axes[0, 1].set_title("Scatter Plot")

# Bar Chart
axes[0, 2].bar(bar_labels, bar_values, color=['blue', 'green', 'orange', 'purple'])
axes[0, 2].set_title("Bar Chart")

# Histogram
axes[0, 3].hist(hist_data, bins=20, color='gray', edgecolor='black')
axes[0, 3].set_title("Histogram")

# Pie Chart
axes[0, 4].pie(pie_sizes, labels=bar_labels, autopct='%1.1f%%', startangle=140)
axes[0, 4].set_title("Pie Chart")

# Area Plot
axes[1, 0].fill_between(x, y, color="skyblue", alpha=0.4)
axes[1, 0].set_title("Area Plot")

# Step Plot
axes[1, 1].step(x, y, where='mid', color='magenta')
axes[1, 1].set_title("Step Plot")

# Box Plot
axes[1, 2].boxplot(hist_data)
axes[1, 2].set_title("Box Plot")

# Violin Plot
axes[1, 3].violinplot(hist_data)
axes[1, 3].set_title("Violin Plot")

# 3D Surface Plot
ax3d = fig.add_subplot(2, 5, 10, projection='3d')
X, Y = np.meshgrid(np.linspace(-5, 5, 30), np.linspace(-5, 5, 30))
Z = np.sin(np.sqrt(X**2 + Y**2))
ax3d.plot_surface(X, Y, Z, cmap='viridis')
ax3d.set_title("3D Surface Plot")

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
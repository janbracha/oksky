import numpy as np
import matplotlib.pyplot as plt

# Create data
temp_range = [5, 15, 25, 35, 45, 55, 65]
payload_range = [3500, 4500, 5500, 6500, 7500, 7800, 8000]
colors = (0,0,0)


# Plot
plt.subplot(2, 1, 1)
plt.scatter(temp_range, payload_range, alpha=0.5)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('temp')
plt.ylabel('payload')
plt.subplot(2, 1, 2)
temp_range1 = [5, 15, 25, 35, 45]
plt.hist(temp_range)
plt.show()

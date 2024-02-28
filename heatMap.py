import numpy as np
import matplotlib.pyplot as plt

dataset = np.random.rand(10,10)

#Plotting Heatmap

plt.figure(figsize=(8,6))
plt.imshow(dataset,cmap='viridis',interpolation='nearest')
plt.colorbar(label='Values')
plt.title('Heatmap')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

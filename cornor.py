import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
num_points = 1000
num_feautes = 2
Dataset =np.random.rand(num_points,num_feautes)

corner_date = Dataset[:100]
plt.scatter(corner_date[:, 0], corner_date[:,1],color='b',alpha=0.5)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.title('Corner of the Datasets')
plt.grid(True)
plt.show()

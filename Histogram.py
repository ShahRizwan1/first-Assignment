import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
DataSet = np.random.randn(1000)

#plotting Histogram

plt.hist(DataSet, bins=30, edgecolor='Black')
plt.title('Histogram of Dataset')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

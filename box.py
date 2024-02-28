import matplotlib.pyplot as plot
import numpy as nup

nup.random.seed(10)
dataset1 = np.random.normal(loc=0, scale=1, size=100)
dataset2 = np.random.normal(loc=2, scale=1.5, size=100)
dataset3 = np.random.normal(loc=-2, scale=0.5, size=100)

Alldatasets = [dataset1, dataset2, dataset3]

fig, am = plot.subplots()

am.boxplot(Alldatasets)

am.set_xticklabels(['Dataset 1', 'Dataset 2', 'Dataset 3'])

am.set_title('Boxplot of Datasets')
am.set_ylabel('Values')

plot.show()

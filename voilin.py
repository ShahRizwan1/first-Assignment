import matplotlib.pyplot as plot
import seaborn as sb
import numpy as nup

dataset1 = nup.random.normal(loc=0, scale=1, size=100)
dataset2 = nup.random.normal(loc=2, scale=1.5, size=100)
dataset3 = nup.random.normal(loc=-2, scale=0.5, size=100)

data = [dataset1, dataset2, dataset3]

plot.figure(figsize=(10, 6))
sb.violinplot(data=data, inner="points")
plot.title('Violin Plot of Sample Datasets')
plot.xlabel('Groups')
plot.ylabel('Values')
plot.show()

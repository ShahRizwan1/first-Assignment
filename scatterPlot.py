import matplotlib.pyplot as plt

data1 = [1,2,3,4,5]
data2 = [2,3,5,7,11]

data3 = [2,3,4,5,6]
data4 = [1,4,6,8,10]

plt.scatter(data1,data2,color='red', label = 'DataSet No 1')
plt.scatter(data3,data4,color='blue', label = 'DataSet No 2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot of DataSets')
plt.legend()

plt.grid(True)
plt.show()

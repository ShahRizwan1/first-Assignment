import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5]
data2 = [2, 3, 5, 7, 11]
data3 = [1, 4, 9, 16, 25]

plt.plot(data1, data2, label='Dataset No 1', color='blue', linestyle='-')
plt.plot(data1, data3, label='Dataset No 2', color='red', linestyle='--')

plt.title('Line Chart of Datasets')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.legend()
plt.show()

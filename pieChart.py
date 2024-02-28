import matplotlib.pyplot as plt

label = ['A','B','C','D']
Size = [15,30,47,10]

#Plotting Pie Chart
plt.figure(figsize=(8,8))
plt.pie(Size, labels=label, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Pie Chart')
plt.show()

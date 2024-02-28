import pandas
import matplotlib.pyplot as plt
import pandas as pd

DataSet = {'Categories': ['A', 'B', 'C', 'D'],'Values': [23, 45, 56, 78]}

#Creating DataFrame 
df = pd.DataFrame(DataSet)

#Plotting
plt.figure(figsize = (8,6))
plt.bar(df['Categories'], df['Values'], color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

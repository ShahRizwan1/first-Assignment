import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion Matrix', cmap=plt.cm.Blues):
  if normalize:
    cm=cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
    print('Normalized Confusion Matrix')
  else:
    print('Without Normalization Confusion Matrix')  

  plt.figure(figsize=(8,6))
  plt.imshow(cm,interpolation='nearest',cmap=cmap)
  plt.title(title)
  plt.colorbar()
  tick_marks = np.arange(len(classes))
  plt.xticks(tick_marks,classes,rotation=45)
  plt.yticks(tick_marks,classes)

  fmt = '.2f' if normalize else 'd'
  thresh = cm.max()/2
  for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
    plt.text(j,i,format(cm[i,j],fmt), horizontalalignment="center",color="white" if cm[i,j] > thresh else "black")
    plt.tight_layout
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')

y_trueV = [0, 1, 2, 0, 1, 2, 0, 1, 2]
y_predi = [0, 1, 2, 1, 0, 1, 2, 2, 2]

classes_name = ['Class 0', 'Class 1', 'Class 2']
cnf_matrix = confusion_matrix(y_trueV, y_predi)

plt.figure()
plot_confusion_matrix(cnf_matrix,classes=classes_name,normalize=True,title='Normalized COnfusion Matrix')

plt.show()

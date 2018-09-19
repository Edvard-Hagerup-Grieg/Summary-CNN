import numpy
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
#from keras.wrappers.scikit_learn.KerasClassifier import

(x_train, y_train), (x_test, y_test) = mnist.load_data()

##To show data (matrix)
#print(x_train[0])

##To show data (image)
# plotData = x_train[0]
# plotData = plotData.reshape(28, 28)
# plt.gray()
# plt.imshow(plotData)
# plt.show()

model = Sequential()

model.add()
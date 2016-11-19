from sknn.mlp import Classifier, Layer
import numpy as np
import pickle

train_file = 'data/trainingset.csv'

train = np.loadtxt( train_file, delimiter = ',' )

x_train = train[:,0:-1]
y_train = train[:,-1]
y_train = y_train.reshape( -1, 1 )

nn = Classifier(
    layers=[
        Layer("Sigmoid", units=100),
        Layer("Softmax")],
    learning_rate=0.001,
    n_iter=600)

nn.fit(x_train, y_train)

pickle.dump(nn, open('nn.pkl', 'wb'))

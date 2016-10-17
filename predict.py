import numpy as np
import cPickle as pickle

from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE

model_file = 'model.pkl'
net = pickle.load( open( model_file, 'rb' ))

def predict_player(inputs):
    x = np.array([inputs])

    input_size = x.shape[1]
    target_size = 1

    y_dummy = np.zeros( (1, 1) )

    ds = SDS( input_size, target_size )
    ds.setField( 'input', x )
    ds.setField( 'target', y_dummy )

    p = net.activateOnDataset( ds )
    return p[0][0]

def player_for_score(score):
    rounded = int(score)
    players = ['Jaap', 'Joel', 'Tobias']
    if rounded > len(players) or rounded < 1:
        return '[UNKNOWN]'
    else:
        return players[rounded - 1]

import pickle
import numpy as np

nn = pickle.load(open('scikit-neuralnetwork/nn.pkl', 'rb'))

def predict_player(inputs, index):
    X = np.array([inputs])
    index = nn.predict(X)[0][0]
    players = ['Jaap', 'Joel', 'Tobias']
    return players[int(index) - 1]

import numpy as np
from matplotlib import pyplot as plt

from data import load_data
from model import forward_prop, get_predictions
from train import gradient_descent

X_train, y_train, X_dev, y_dev = load_data()

def make_predictions(X, W1, b1, W2, b2, W3, b3):
    _, _, _, _, _, A3 = forward_prop(W1, b1, W2, b2, W3, b3, X)
    predictions = get_predictions(A3)
    return predictions

def test_prediction(index, W1, b1, W2, b2, W3, b3):
    current_image = X_train[:, index, None]
    prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2, W3, b3)
    label = y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()

W1, b1, W2, b2, W3, b3 = gradient_descent(X_train, y_train, 0.1, 150)
test_prediction(0, W1, b1, W2, b2, W3, b3)
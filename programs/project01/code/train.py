from matplotlib import pyplot as plt

from model import init_params, update_params, forward_prop, backward_prop, get_predictions, get_accuracy

def gradient_descent(X, y, alpha, iterations):
    W1, b1, W2, b2, W3, b3 = init_params()
    accs = []
    plt.ion()
    for i in range(iterations): 
        Z1, A1, Z2, A2, Z3, A3 = forward_prop(W1, b1, W2, b2, W3, b3, X)
        predictions = get_predictions(A3) 
        accs.append(get_accuracy(predictions, y))
        dW1, db1, dW2, db2, dW3, db3 = backward_prop(Z1, A1, Z2, A2, Z3, A3, W2, W3, X, y) 
        W1, b1, W2, b2, W3, b3 = update_params(W1, b1, W2, b2, W3, b3, dW1, db1, dW2, db2, dW3, db3, alpha) 
        if i % 10 == 0:
            print("Iteration: ", i)
            plt.clf()
            plt.plot(accs, color="blue")
            plt.xlabel("Iteration")
            plt.ylabel("Accuracy")
            plt.title("Accuracy over iterations")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return W1, b1, W2, b2, W3, b3
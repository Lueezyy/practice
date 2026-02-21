import pandas as pd
import numpy as np

def load_data():
    data = pd.read_csv('data/train.csv')

    #numpy arrays are better than pandas dataframe for math operations
    data = np.array(data)

    #m rows and n columns are better than numbers since variables can change
    m, n = data.shape

    #shuffle so the model learns from patterns in data not order
    np.random.shuffle(data)

    #initialize our development (or validation) dataset to first 1000 images
    #transpose so the columns become each image, better for features
    data_dev = data[0:1000].T

    #set y to the "true" values of each image, this is what we're comparing to
    #since the data is transposed, the 0th row is now all the true values of each image
    y_dev = data_dev[0]

    #the original n is the pixels for each image with the label being the 0th entry
    #for the transposed validation data, n becomes the pixels for each image
    X_dev = data_dev[1:n]

    #256 values from 0(black) to 255(white), divide by 255 so each pixel color is 0 to 1
    #this is better for gradients since the magnitude of input plays a huge role
    X_dev = X_dev / 255.

    #now that the validation data is created, set the training data to the rest of the dataset
    data_train = data[1000:m].T

    #the training values follow the same logic as the validation since the test data is also transposed
    y_train = data_train[0]
    X_train = data_train[1:n]
    X_train = X_train / 255.
    
    #the data is now able to be used as training and development data
    return X_train, y_train, X_dev, y_dev
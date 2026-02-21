from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

from data import load_data

def makeModel(estimators):
    data = load_data()
    y = data.rating
    features = ["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "vitamins"]
    X = data[features]
    trainX, valX, trainy, valy = train_test_split(X, y, random_state=1)
    forestModel = RandomForestRegressor(n_estimators = estimators, random_state=1)
    forestModel.fit(trainX, trainy)
    predictions = forestModel.predict(valX)
    return mean_absolute_error(valy, predictions)
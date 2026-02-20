import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("data/cereal.csv")
y = data.rating
features = ["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "vitamins"]
X = data[features]

def makeModel(estimators):
    trainX, valX, trainy, valy = train_test_split(X, y, random_state=1)
    forestModel = RandomForestRegressor(n_estimators = estimators, random_state=1)
    forestModel.fit(trainX, trainy)
    predictions = forestModel.predict(valX)
    print(mean_absolute_error(valy, predictions))

estimators = int(input("Number of decision trees: "))
makeModel(estimators)
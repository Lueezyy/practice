import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("data/customdata.csv")
features = ["gdp", "lifeExpectancy", "internetPct"]

le = LabelEncoder()
y = le.fit_transform(data.income)
X = data[features]
trainX, valX, trainy, valy = train_test_split(X, y, random_state=1)

def makeModel(estimators=100):
    forestModel = RandomForestClassifier(n_estimators = estimators, random_state=1)
    forestModel.fit(trainX, trainy)
    return forestModel

def makePredictions(forestModel):
    predictions = forestModel.predict(valX)
    print(f"{accuracy_score(valy, predictions) * 100}% accuracy")

def makePrediction(forestModel, userData):
    return forestModel.predict(userData)

forestModel = makeModel()

gdp = float(input("Enter GDP per Capita: "))
lifeExp = float(input("Enter life expectancy: "))
internetPct = float(input("Enter internet percentage: "))

userData = pd.DataFrame([[gdp, lifeExp, internetPct]], columns=features)
predNum = makePrediction(forestModel, userData)
pred_label = le.inverse_transform(predNum)

print(f"Predicted income level: {pred_label[0]}")
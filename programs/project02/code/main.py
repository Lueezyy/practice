from model import makeModel

estimators = int(input("Number of decision trees: "))
print(f"The MAE is: {makeModel(estimators):.3f}")
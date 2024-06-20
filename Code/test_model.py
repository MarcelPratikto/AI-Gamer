#from sklearn.tree import DecisionTreeRegressor
import pickle

model = pickle.load(open("Code/model.pkl", "rb"))

print(model.predict([[41,False,-1,-1,-1]]))
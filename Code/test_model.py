#from sklearn.tree import DecisionTreeRegressor
import pickle

model = pickle.load(open("Code/model.pkl", "rb"))

print(model.predict([[10,False,-1,-1,-1]]))
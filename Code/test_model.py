#from sklearn.tree import DecisionTreeRegressor
import pickle

model = pickle.load(open("Code/Old-Samples-Models/model.pkl", "rb"))

# print("10s: ")
# print(model.predict([[10,False,-1,-1,-1]]))
# print()

# print("100s:")
# print(model.predict([[100,False,-1,-1,-1]]))
# print(model.predict([[110,False,-1,-1,-1]]))
# print(model.predict([[120,False,-1,-1,-1]]))
# print(model.predict([[130,False,-1,-1,-1]]))
# print(model.predict([[140,False,-1,-1,-1]]))
# print(model.predict([[150,False,-1,-1,-1]]))
# print()

# print("200s: ")
# print(model.predict([[200,False,-1,-1,-1]]))

reset = False
seconds = 0
while seconds < 200:
    prediction = model.predict([[seconds,False,-1,-1,-1]])
    seconds += 1
    reset = prediction[0][7]
    if reset:
        print(f"seconds: {seconds}")
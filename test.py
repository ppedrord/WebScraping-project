import pickle

with open('urls_rejected.p', 'rb') as file:
    object = pickle.load(file)

print(len(object))

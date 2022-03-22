import pickle

with open('list_urls_thriller.p', 'rb') as file:
    list = pickle.load(file)

print(len(list))
print(list[2002])



import pickle

with open('list_urls_superhero.p', 'rb') as file:
    list = pickle.load(file)

print(len(list))
print(list[25])



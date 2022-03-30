import pickle

with open('movie_data_limited_all.p', 'rb') as movies_file:
    object = pickle.load(movies_file)

print(object[1])
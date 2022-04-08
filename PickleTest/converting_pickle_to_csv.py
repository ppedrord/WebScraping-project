import pickle
import pandas as pd

with open('movie_data_limited_all_updated.p', 'rb') as movies_file:
    object = pickle.load(movies_file)

list_of_certificate_categories = list()
for i in object:
    if i['certificate'] is not None:
        if i['certificate'] != "Isn't Available":
            if i['imdb_rating'] is not None:
                list_of_certificate_categories.append(i)

for i in list_of_certificate_categories:
    if i['certificate'] == "PG":
        i['certificate'] = '10'

    elif i['certificate'] == "PG-13":
        i['certificate'] = '14'

    elif i['certificate'] == "R":
        i['certificate'] = '16'

    elif i['certificate'] == "NC-17":
        i['certificate'] = '18'

    elif i['certificate'] == "L":
        i['certificate'] = 'Livre'

    elif i['certificate'] == "16+":
        i['certificate'] = '16'

    elif i['certificate'] == "M/PG":
        i['certificate'] = '16'

    elif i['certificate'] == "M":
        i['certificate'] = '16'

    elif i['certificate'] == "X":
        i['certificate'] = '18'

    elif i['certificate'] == "GP":
        i['certificate'] = '10'

    elif i['certificate'] == "G":
        i['certificate'] = 'Livre'

list_movies_above_18 = list()
for i in list_of_certificate_categories:
    if i['certificate'] == "18":
        list_movies_above_18.append(i)


imdb_rating_action = list()
imdb_rating_adventure = list()
imdb_rating_animation = list()
imdb_rating_biography = list()
imdb_rating_comedy = list()
imdb_rating_crime = list()
imdb_rating_drama = list()
imdb_rating_family = list()
imdb_rating_fantasy = list()
imdb_rating_film_noir = list()
imdb_rating_history = list()
imdb_rating_horror = list()
imdb_rating_music = list()
imdb_rating_musical = list()
imdb_rating_mystery = list()
imdb_rating_romance = list()
imdb_rating_sci_fi = list()
imdb_rating_sport = list()
imdb_rating_thriller = list()
imdb_rating_war = list()
imdb_rating_western = list()


for i in list_movies_above_18:
    for j in i['genre']:
        if j == "ACTION":
            imdb_rating_action.append(i['imdb_rating'])

        elif j == "ADVENTURE":
            imdb_rating_adventure.append(i['imdb_rating'])

        elif j == "ANIMATION":
            imdb_rating_animation.append(i['imdb_rating'])

        elif j == "BIOGRAPHY":
            imdb_rating_biography.append(i['imdb_rating'])

        elif j == "COMEDY":
            imdb_rating_comedy.append(i['imdb_rating'])

        elif j == "CRIME":
            imdb_rating_crime.append(i['imdb_rating'])

        elif j == "DRAMA":
            imdb_rating_drama.append(i['imdb_rating'])

        elif j == "FAMILY":
            imdb_rating_family.append(i['imdb_rating'])

        elif j == "FANTASY":
            imdb_rating_fantasy.append(i['imdb_rating'])

        elif j == "FILM-NOIR":
            imdb_rating_film_noir.append(i['imdb_rating'])

        elif j == "HISTORY":
            imdb_rating_history.append(i['imdb_rating'])

        elif j == "HORROR":
            imdb_rating_horror.append(i['imdb_rating'])

        elif j == "MUSIC":
            imdb_rating_music.append(i['imdb_rating'])

        elif j == "MUSICAL":
            imdb_rating_musical.append(i['imdb_rating'])

        elif j == "MYSTERY":
            imdb_rating_mystery.append(i['imdb_rating'])

        elif j == "ROMANCE":
            imdb_rating_romance.append(i['imdb_rating'])

        elif j == "SCI-FI":
            imdb_rating_sci_fi.append(i['imdb_rating'])

        elif j == "SPORT":
            imdb_rating_sport.append(i['imdb_rating'])

        elif j == "THRILLER":
            imdb_rating_thriller.append(i['imdb_rating'])

        elif j == "WAR":
            imdb_rating_war.append(i['imdb_rating'])

        elif j == "WESTERN":
            imdb_rating_western.append(i['imdb_rating'])
print("soma de action:", sum(imdb_rating_action))

average_rating_per_genre = [
    {
        'genre': 'Action',
        'average_rating': round(sum(imdb_rating_action)/len(imdb_rating_action), 1) if len(imdb_rating_action) is not None else None
        },
    {
        'genre': 'Adventure',
        'average_rating': round(sum(imdb_rating_adventure) / len(imdb_rating_adventure), 1) if len(imdb_rating_adventure) is not None else None
        },
    {
        'genre': 'Animation',
        'average_rating': round(sum(imdb_rating_animation) / len(imdb_rating_animation), 1) if len(imdb_rating_animation) is not None else None
        },
    {
        'genre': 'Biography',
        'average_rating': round(sum(imdb_rating_biography) / len(imdb_rating_biography), 1) if len(imdb_rating_biography) is not None else None
        },
    {
        'genre': 'Comedy',
        'average_rating': round(sum(imdb_rating_comedy) / len(imdb_rating_comedy), 1) if len(imdb_rating_comedy) is not None else None
        },
    {
        'genre': 'Crime',
        'average_rating': round(sum(imdb_rating_crime) / len(imdb_rating_crime), 1) if len(imdb_rating_crime) is not None else None
        },
    {
        'genre': 'Drama',
        'average_rating': round(sum(imdb_rating_drama) / len(imdb_rating_drama), 1) if len(imdb_rating_drama) is not None else None
        },
    {
        'genre': 'Family',
        'average_rating': round(sum(imdb_rating_family) / len(imdb_rating_family), 1) if len(imdb_rating_family) is not None else None
        },
    {
        'genre': 'Fantasy',
        'average_rating': round(sum(imdb_rating_fantasy) / len(imdb_rating_fantasy), 1) if len(imdb_rating_fantasy) is not None else None
        },
    {
        'genre': 'Film-Noir',
        'average_rating': round(sum(imdb_rating_film_noir) / len(imdb_rating_film_noir), 1) if len(imdb_rating_film_noir) is not None else None
        },
    {
        'genre': 'History',
        'average_rating': round(sum(imdb_rating_history) / len(imdb_rating_history), 1) if len(imdb_rating_history) is not None else None
        },
    {
        'genre': 'Horror',
        'average_rating': round(sum(imdb_rating_horror) / len(imdb_rating_horror), 1) if len(imdb_rating_horror) is not None else None
        },
    {
        'genre': 'Music',
        'average_rating': round(sum(imdb_rating_music) / len(imdb_rating_music), 1) if len(imdb_rating_music) is not None else None
        },
    {
        'genre': 'Musical',
        'average_rating': round(sum(imdb_rating_musical) / len(imdb_rating_musical), 1) if len(imdb_rating_musical) is not None else None
        },
    {
        'genre': 'Mystery',
        'average_rating': round(sum(imdb_rating_mystery) / len(imdb_rating_mystery), 1) if len(imdb_rating_mystery) is not None else None
        },
    {
        'genre': 'Romance',
        'average_rating': round(sum(imdb_rating_romance) / len(imdb_rating_romance), 1) if len(imdb_rating_romance) is not None else None
        },
    {
        'genre': 'Sci-Fi',
        'average_rating': round(sum(imdb_rating_sci_fi) / len(imdb_rating_sci_fi), 1) if len(imdb_rating_sci_fi) is not None else None
        },
    {
        'genre': 'Sport',
        'average_rating': round(sum(imdb_rating_sport) / len(imdb_rating_sport), 1) if len(imdb_rating_sport) is not None else None
        },
    {
        'genre': 'Thriller',
        'average_rating': round(sum(imdb_rating_thriller) / len(imdb_rating_thriller), 1) if len(imdb_rating_thriller) is not None else None
        },
    {
        'genre': 'War',
        'average_rating': round(sum(imdb_rating_war) / len(imdb_rating_war), 1) if len(imdb_rating_war) is not None else None
        },
    {
        'genre': 'Western',
        'average_rating': round(sum(imdb_rating_western) / len(imdb_rating_western), 1) if len(imdb_rating_western) is not None else None
        }
    ]


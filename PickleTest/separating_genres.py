import pickle


def separate_genres():
    with open('movie_data_limited_all_updated.p', 'rb') as movies_file:
        object = pickle.load(movies_file)

    list_action = list()
    list_adventure = list()
    list_animation = list()
    list_biography = list()
    list_comedy = list()
    list_crime = list()
    list_drama = list()
    list_family = list()
    list_fantasy = list()
    list_film_noir = list()
    list_history = list()
    list_horror = list()
    list_music = list()
    list_musical = list()
    list_mystery = list()
    list_romance = list()
    list_sci_fi = list()
    list_sport = list()
    list_superhero = list()
    list_thriller = list()
    list_war = list()
    list_western = list()

    for i in object:

        for j in i['genre']:
            if j == "ACTION":
                list_action.append(i)
            elif j == "ADVENTURE":
                list_adventure.append(i)
            elif j == "ANIMATION":
                list_animation.append(i)
            elif j == "BIOGRAPHY":
                list_biography.append(i)
            elif j == 'COMEDY':
                list_comedy.append(i)
            elif j == "CRIME":
                list_crime.append(i)
            elif j == "DRAMA":
                list_drama.append(i)
            elif j == "FAMILY":
                list_family.append(i)
            elif j == "FANTASY":
                list_fantasy.append(i)
            elif j == "FILM-NOIR":
                list_film_noir.append(i)
            elif j == "HISTORY":
                list_history.append(i)
            elif j == "HORROR":
                list_horror.append(i)
            elif j == "MUSIC":
                list_music.append(i)
            elif j == "MUSICAL":
                list_musical.append(i)
            elif j == "MYSTERY":
                list_mystery.append(i)
            elif j == "ROMANCE":
                list_romance.append(i)
            elif j == "SCI-FI":
                list_sci_fi.append(i)
            elif j == "SPORT":
                list_sport.append(i)
            elif j == "SUPERHERO":
                list_superhero.append(i)
            elif j == "THRILLER":
                list_thriller.append(i)
            elif j == "WAR":
                list_war.append(i)
            elif j == "WESTERN":
                list_western.append(i)

    with open('movies_action.p', 'wb') as action:
        pickle.dump(list_action, action)

    with open('movies_adventure.p', 'wb') as adventure:
        pickle.dump(list_adventure, adventure)

    with open('movies_animation.p', 'wb') as animation:
        pickle.dump(list_animation, animation)

    with open('movies_biography.p', 'wb') as biography:
        pickle.dump(list_biography, biography)

    with open('movies_comedy.p', 'wb') as comedy:
        pickle.dump(list_comedy, comedy)

    with open('movies_crime.p', 'wb') as crime:
        pickle.dump(list_crime, crime)

    with open('movies_drama.p', 'wb') as drama:
        pickle.dump(list_drama, drama)

    with open('movies_family.p', 'wb') as family:
        pickle.dump(list_family, family)

    with open('movies_fantasy.p', 'wb') as fantasy:
        pickle.dump(list_fantasy, fantasy)

    with open('movies_film_noir.p', 'wb') as film_noir:
        pickle.dump(list_film_noir, film_noir)

    with open('movies_history.p', 'wb') as history:
        pickle.dump(list_history, history)

    with open('movies_horror.p', 'wb') as horror:
        pickle.dump(list_horror, horror)

    with open('movies_music.p', 'wb') as music:
        pickle.dump(list_music, music)

    with open('movies_musical.p', 'wb') as musical:
        pickle.dump(list_musical, musical)

    with open('movies_mystery.p', 'wb') as mystery:
        pickle.dump(list_mystery, mystery)

    with open('movies_romance.p', 'wb') as romance:
        pickle.dump(list_romance, romance)

    with open('movies_sci_fi.p', 'wb') as sci_fi:
        pickle.dump(list_sci_fi, sci_fi)

    with open('movies_sport.p', 'wb') as sport:
        pickle.dump(list_sport, sport)

    with open('movies_superhero.p', 'wb') as superhero:
        pickle.dump(list_superhero, superhero)

    with open('movies_thriller.p', 'wb') as thriller:
        pickle.dump(list_thriller, thriller)

    with open('movies_war.p', 'wb') as war:
        pickle.dump(list_war, war)

    with open('movies_western.p', 'wb') as western:
        pickle.dump(list_western, western)


def rating_per_runtime():
    with open('movie_data_limited_all_updated.p', 'rb') as movies_file:
        object = pickle.load(movies_file)
    rating_per_runtime_dict = list()
    imdb_rating_list = list()
    for i in range(45, 181):
        data = {
            'runtime': i
            }
        imdb_rating_list.clear()
        for j in object:
            if j['runtime'] == i:
                if j['imdb_rating'] is not None:
                    imdb_rating_list.append(j['imdb_rating'])

        if len(imdb_rating_list) != 0:
            data.update({'imdb_rating': round((sum(imdb_rating_list) / len(imdb_rating_list)), 1)})
        else:
            data.update({'imdb_rating': None})

        if data['imdb_rating'] is not None:
            rating_per_runtime_dict.append(data)


rating_per_runtime()

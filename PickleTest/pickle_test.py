import pickle
import json

with open('movies.p', 'rb') as file:
    object = pickle.load(file)

dictionary = {
    'movies_limited_all': object
    }
print(type(object))
print(type(dictionary))

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)



"""list_individual_links = list()
individual_links_file = open("individual_links_file.p", "wb")
for i, v in enumerate(object):
    list_individual_links.append(object[i]['link'])

print(len(list_individual_links))
list_individual_links = list(set(list_individual_links))
print(len(list_individual_links))
individual_links_file = open("individual_links_file.p", "wb")
pickle.dump(list_individual_links, individual_links_file)
individual_links_file.close()
"""
# for i in list_urls:
#     print(i)

"""
    list_urls_genre_action = create_list_urls("action", get_urls_genre_action())
    list_urls_genre_adventure = create_list_urls("adventure", get_urls_genre_adventure())
    list_urls_genre_animation = create_list_urls("animation", get_urls_genre_animation())
    list_urls_genre_biography = create_list_urls("biography", get_urls_genre_biography())
    list_urls_genre_comedy = create_list_urls("comedy", get_urls_genre_comedy())
    list_urls_genre_crime = create_list_urls("crime", get_urls_genre_crime())
    # list_urls_genre_documentary = create_list_urls("documentary", get_urls_genre_documentary())
    list_urls_genre_drama = create_list_urls("drama", get_urls_genre_drama())
    list_urls_genre_family = create_list_urls("family", get_urls_genre_family())
    list_urls_genre_fantasy = create_list_urls("fantasy", get_urls_genre_fantasy())
    list_urls_genre_film_noir = create_list_urls("film_noir", get_urls_genre_film_noir())
    list_urls_genre_history = create_list_urls("history", get_urls_genre_history())
    list_urls_genre_horror = create_list_urls("horror", get_urls_genre_horror())
    list_urls_genre_music = create_list_urls("music", get_urls_genre_music())
    list_urls_genre_musical = create_list_urls("musical", get_urls_genre_musical())
    list_urls_genre_mystery = create_list_urls("mystery", get_urls_genre_mystery())
    list_urls_genre_romance = create_list_urls("romance", get_urls_genre_romance())
    list_urls_genre_sci_fi = create_list_urls("sci_fi", get_urls_genre_sci_fi())
    # list_urls_genre_short_film = create_list_urls("short_film", get_urls_genre_short_film())
    list_urls_genre_sport = create_list_urls("sport", get_urls_genre_sport())
    list_urls_genre_superhero = create_list_urls("superhero", get_urls_genre_superhero())
    list_urls_genre_thriller = create_list_urls("thriller", get_urls_genre_thriller())
    list_urls_genre_war = create_list_urls("war", get_urls_genre_war())
    list_urls_genre_western = create_list_urls("western", get_urls_genre_western())

    list_urls_action = get_urls_genre_action()
    list_urls_adventure = get_urls_genre_adventure()
    list_urls_animation = get_urls_genre_animation()
    list_urls_biography = get_urls_genre_biography()
    list_urls_comedy = get_urls_genre_comedy()
    list_urls_crime = get_urls_genre_crime()
    # list_urls_documentary = get_urls_genre_documentary()
    list_urls_drama = get_urls_genre_drama()
    list_urls_family = get_urls_genre_family()
    list_urls_fantasy = get_urls_genre_fantasy()
    list_urls_film_noir = get_urls_genre_film_noir()
    list_urls_history = get_urls_genre_history()
    list_urls_horror = get_urls_genre_horror()
    list_urls_music = get_urls_genre_music()
    list_urls_musical = get_urls_genre_musical()
    list_urls_mystery = get_urls_genre_mystery()
    list_urls_romance = get_urls_genre_romance()
    list_urls_sci_fi = get_urls_genre_sci_fi()
    # list_urls_short_film = get_urls_genre_short_film()
    list_urls_sport = get_urls_genre_sport()
    list_urls_superhero = get_urls_genre_superhero()
    list_urls_thriller = get_urls_genre_thriller()
    list_urls_war = get_urls_genre_war()
    list_urls_western = get_urls_genre_western()

    list_urls = list_urls_action
    list_urls.extend(list_urls_adventure)
    list_urls.extend(list_urls_animation)
    list_urls.extend(list_urls_biography)
    list_urls.extend(list_urls_comedy)
    list_urls.extend(list_urls_crime)
    list_urls.extend(list_urls_documentary)
    list_urls.extend(list_urls_drama)
    list_urls.extend(list_urls_family)
    list_urls.extend(list_urls_fantasy)
    list_urls.extend(list_urls_film_noir)
    list_urls.extend(list_urls_history)
    list_urls.extend(list_urls_horror)
    list_urls.extend(list_urls_music)
    list_urls.extend(list_urls_musical)
    list_urls.extend(list_urls_mystery)
    list_urls.extend(list_urls_romance)
    list_urls.extend(list_urls_sci_fi)
    # list_urls.extend(list_urls_short_film)
    list_urls.extend(list_urls_sport)
    list_urls.extend(list_urls_superhero)
    list_urls.extend(list_urls_thriller)
    list_urls.extend(list_urls_war)
    list_urls.extend(list_urls_western)
    print(len(list_urls))"""

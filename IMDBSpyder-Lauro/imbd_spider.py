# -*- coding: utf-8 -*-
"""
author:
- Lauro de Lacerda [ laurodelacerda@gmail.com ]
"""
import sys, getopt
import time
import requests
import pickle
import re
from bs4 import BeautifulSoup as bs
from threading import Thread

################################################################
# Threading
################################################################

def divide_work(list_urls, thread_id: int, thread_number: int) :

    size = len(list_urls)

    part = size / thread_number
    start = int(thread_id * part)
    end = int((thread_id * part) + part) if thread_id != thread_number - 1 else size

    print('Starting Thread {}/{} - items {} - {}'.format(thread_id, thread_number, start, end))

    if thread_id > thread_number :
        return None
    else :
        return list_urls[start : end]


class IMDbThread(Thread):

    def __init__(self, urls):
        super().__init__()
        self.urls   = urls
        self.movies = None

    def run(self):
        self.movies = list(execute(self.urls))

################################################################
# General Methods
################################################################

def get_urls_genre_sport():

    list_urls = list()

    for i in range(0, 99):
        title_number = i * 50 + 1
        target = f"https://www.imdb.com/search/title/?title_type=feature&genres=sport&start={title_number}&explore=genres&ref_=adv_nxt"
        list_urls.append(target)

    return list_urls

def make_request(url):

    try:
        response = requests.get(url)
        movies   = parse_data(response.text)
        return movies
    except:
        return None

def parse_data(html_page :str):

    parser = bs(html_page, "html.parser")

    data = parser.find_all("div", {"class" : "lister-item mode-advanced"})

    h3_selector = parser.find_all('h3', {'class' : 'lister-item-header'})
    p_selector = parser.find_all('p', {'class' : 'text-muted'})

    num_p = 0
    num_p_synopsis = 1

    movies_list = list()
    for i, card in enumerate(data) :

        movie_title = h3_selector[i].find('a').text

        movie_url = h3_selector[i].find('a').get("href")

        title = movie_title

        if h3_selector[i].find('span', {'class' : 'lister-item-year text-muted unbold'}) is None :
            movie_year = "Isn't Available"
        else :
            movie_year = h3_selector[i].find('span', {'class' : 'lister-item-year text-muted unbold'}).text

        year = movie_year[1 :-1]

        if p_selector[num_p].find('span', {'class' : 'certificate'}) is None :
            movie_certificate = "Isn't Available"
        else :
            movie_certificate = p_selector[num_p].find('span', {'class' : 'certificate'}).text

        certificate = movie_certificate

        if p_selector[num_p].find('span', {'class' : 'runtime'}) is None :
            movie_runtime = "Isn't Available"
        else :
            movie_runtime = p_selector[num_p].find('span', {'class' : 'runtime'}).text

        runtime = movie_runtime

        if p_selector[num_p].find('span', {'class' : 'genre'}) is None :
            movie_genre = "Isn't Available"
        else :
            movie_genre = p_selector[num_p].find('span', {'class' : 'genre'}).text

        genre = movie_genre

        if p_selector[num_p_synopsis] is None :
            movie_synopsis = "Isn't Available"
        else :
            movie_synopsis = p_selector[num_p_synopsis].text

        synopsis = movie_synopsis

        movie_data = {
            'title' : clean_data(title),
            'year' : year,
            'certificate' : clean_data(certificate),
            'runtime' : clean_data(runtime),
            'genre' : clean_data(genre),
            'synopsis' : clean_data(synopsis),
            'link' : f"https://www.imdb.com{movie_url}"
        }

        movies_list.append(movie_data)

        num_p += 2
        num_p_synopsis += 2

    return movies_list

def clean_data(value :str):

    new_value = re.sub("/(\r\n|\n|\r)/gm", "", value)
    new_value = re.sub("\s+", " ", new_value)
    new_value = re.sub('\"', "", new_value)

    return new_value

def execute(list_urls :list):

    list_movies = list()
    for i in list_urls:
        movies = make_request(i)
        list_movies.extend(movies)

    return list_movies

################################################################
# Main
################################################################

def main():
    start = time.time()

    number_threads = int(sys.argv[1])

    list_urls = get_urls_genre_sport()
    list_threads = list()

    for i in range(number_threads):
        sub_list_urls = divide_work(list_urls, i, number_threads)
        thread = IMDbThread(sub_list_urls)
        list_threads.append(thread)

    for t in list_threads:
        t.start()

    for t in list_threads:
        t.join()

    # Merging lists
    list_movies = list()
    for i in list_threads:
        list_movies.extend(i.movies)

    file = open("movies.p", "wb")
    pickle.dump(list_movies, file)
    file.close()

    print(time.time() - start)

if __name__ == "__main__":
    main()


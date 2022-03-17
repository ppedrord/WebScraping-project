from bs4 import BeautifulSoup as bs
import re
import SeleniumRequests
from SeleniumRequests import browser
# import main
import requests
import numpy as np
import random
import time
import threading

start = time.time()


class Counter:

    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self):
        with self.lock:
            self.count += 1
            if self.count % 1000 == 0:
                print('{} - {}'.format(self.count, time.time() - start))


global base_url
base_url = 'https://www.imdb.com'


# Creating a list of url of all the pages in this genre section
def creating_targets():
    global sport_genre
    global number_of_titles
    global advance_pages

    title_number = 1
    page_url    = f'{base_url}/search/title/?title_type=feature&genres=sport&start={title_number}&explore=genres&ref_=adv_nxt'
    browser_url = browser.get(page_url)
    html = browser.page_source
    sport_genre = bs(html, "html.parser")

    number_of_titles = sport_genre.find('tbody').find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)

    advance_pages = list()

    while title_number < number_of_titles:
        if title_number > number_of_titles:
            break
        page_url = f'{base_url}/search/title/?title_type=feature&genres=sport&start={title_number}&explore=genres&ref_=adv_nxt'
        # page_url = page_url[20:]
        advance_pages.append(page_url)
        title_number += 50
    print(advance_pages)

    return advance_pages


pages = creating_targets()

<<<<<<< HEAD
"""def divide_work(advance_pages, thread_id: int, thread_number: int):
=======
print(pages)

def divide_work(advance_pages, thread_id: int, thread_number: int):
>>>>>>> 8ac419b595d072d8e854ac4f4f532826c27ce9c8
    size = len(advance_pages)

    part = size / thread_number
    start = int(thread_id * part)
    end = int((thread_id * part) + part) if thread_id != thread_number - 1 else size

    print('Starting Thread {}/{} - items {} - {}'.format(thread_id, thread_number - 1, start, end))

    if thread_id > thread_number:
        return None
    else:
        return advance_pages[start: end]"""


def sending_requests(advance_pages):
    global movies_list
    global cards
    from requests import get
    cards = sport_genre.find_all('div', {'class': 'lister-item mode-advanced'})
    movies_list = list()
    h3_selector = sport_genre.find_all('h3', {'class': 'lister-item-header'})
    p_selector = sport_genre.find_all('p', {'class': 'text-muted'})
    for i in advance_pages:
        print(i)
        request = get(i)
        print(request.status_code)
        num_p = 0
        num_p_synopsis = 1
        for j, card in enumerate(cards):
            movie_title = h3_selector[j].find('a').text
            title = movie_title

            if h3_selector[j].find('span', {'class': 'lister-item-year text-muted unbold'}) is None:
                movie_year = "Isn't Available"
            else:
                movie_year = h3_selector[j].find('span', {'class': 'lister-item-year text-muted unbold'}).text

            year = movie_year

            if p_selector[num_p].find('span', {'class': 'certificate'}) is None:
                movie_certificate = "Isn't Available"
            else:
                movie_certificate = p_selector[num_p].find('span', {'class': 'certificate'}).text

            certificate = movie_certificate

            if p_selector[num_p].find('span', {'class': 'runtime'}) is None:
                movie_runtime = "Isn't Available"
            else:
                movie_runtime = p_selector[num_p].find('span', {'class': 'runtime'}).text

            runtime = movie_runtime

            if p_selector[num_p].find('span', {'class': 'genre'}) is None:
                movie_genre = "Isn't Available"
            else:
                movie_genre = p_selector[num_p].find('span', {'class': 'genre'}).text

            genre = movie_genre

            if p_selector[num_p_synopsis] is None:
                movie_synopsis = "Isn't Available"
            else:
                movie_synopsis = p_selector[num_p_synopsis].text

            synopsis = movie_synopsis

            movie_data = {
                'title': title,
                'year': year,
                'certificate': certificate,
                'runtime': runtime,
                'genre': genre,
                'synopsis': synopsis
                }
            movies_list.append(movie_data)
            print(j, movie_data)
            num_p += 2
            num_p_synopsis += 2
    return movies_list


print(sending_requests(advance_pages))

"""def finding_movie_data():
    global movies_list
    global cards

    cards       = sport_genre.find_all('div', {'class': 'lister-item mode-advanced'})

    movies_list = list()
    h3_selector = sport_genre.find_all('h3', {'class': 'lister-item-header'})
    p_selector  = sport_genre.find_all('p', {'class': 'text-muted'})

    num_p = 0
    num_p_synopsis = 1

    for i, card in enumerate(cards):
        movie_title = h3_selector[i].find('a').text
        title = movie_title

        if h3_selector[i].find('span', {'class': 'lister-item-year text-muted unbold'}) is None:
            movie_year = "Isn't Available"
        else:
            movie_year = h3_selector[i].find('span', {'class': 'lister-item-year text-muted unbold'}).text

        year = movie_year

        if p_selector[num_p].find('span', {'class': 'certificate'}) is None:
            movie_certificate = "Isn't Available"
        else:
            movie_certificate = p_selector[num_p].find('span', {'class': 'certificate'}).text

        certificate = movie_certificate

        if p_selector[num_p].find('span', {'class': 'runtime'}) is None:
            movie_runtime = "Isn't Available"
        else:
            movie_runtime = p_selector[num_p].find('span', {'class': 'runtime'}).text

        runtime = movie_runtime

        if p_selector[num_p].find('span', {'class': 'genre'}) is None:
            movie_genre = "Isn't Available"
        else:
            movie_genre = p_selector[num_p].find('span', {'class': 'genre'}).text

        genre = movie_genre

        if p_selector[num_p_synopsis] is None:
            movie_synopsis = "Isn't Available"
        else:
            movie_synopsis = p_selector[num_p_synopsis].text

        synopsis = movie_synopsis

        movie_data = {
            'title': title,
            'year': year,
            'certificate': certificate,
            'runtime': runtime,
            'genre': genre,
            'synopsis': synopsis
            }

        movies_list.append(movie_data)

        num_p += 2
        num_p_synopsis += 2

    return movies_list


print(finding_movie_data())"""

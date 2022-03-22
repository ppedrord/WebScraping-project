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
import os


################################################################
# Threading
################################################################

def divide_work(list_urls, thread_id: int, thread_number: int):
    size = len(list_urls)

    part = size / thread_number
    start = int(thread_id * part)
    end = int((thread_id * part) + part) if thread_id != thread_number - 1 else size

    print('Starting Thread {}/{} - items {} - {}'.format(thread_id, thread_number, start, end))

    if thread_id > thread_number:
        return None
    else:
        return list_urls[start: end]


class IMDbThread(Thread):

    def __init__(self, urls):
        super().__init__()
        self.urls = urls
        self.movies = None

    def run(self):
        self.movies = list(execute(self.urls))


################################################################
# General Methods
################################################################

def get_urls_all_genres():
    list_urls_all_genres = list()
    response = requests.get('https://www.imdb.com/feature/genre/')
    html_page = bs(response.text, 'html.parser')
    whole_table = html_page.find('div', {'class': 'ab_links'})
    primary_tables = whole_table.find_all('div', {'class': 'table-cell primary'})

    for i in primary_tables:
        find_genre = i.find('a').text
        find_href = i.find('a').get('href')
        genre_url = f'https://www.imdb.com{find_href}'
        genre = {
            'genre': find_genre[1:-1],
            'url': genre_url
            }
        list_urls_all_genres.append(genre)

    return list_urls_all_genres


def get_urls_genre_sport():
    start = time.time()
    sport_url = get_urls_all_genres()[19].get('url')
    list_urls_sport = [sport_url]
    response = requests.get(sport_url)
    sport_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = sport_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=sport&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_sport.append(page_url)
            title_number += 50
        else:
            target = sport_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                sport_genre_pages = bs(next_response.text, "html.parser")
                next_href = sport_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_sport.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=sport&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_sport.append(page_url)
            title_number += 50

    print("get_urls_genre_sport method:", time.time() - start)

    return list_urls_sport


def get_urls_genre_western():
    start = time.time()
    western_url = get_urls_all_genres()[23].get('url')
    list_urls_western = [western_url]
    response = requests.get(western_url)
    western_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = western_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=western&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_western.append(page_url)
            title_number += 50
        else:
            target = western_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                western_genre_pages = bs(next_response.text, "html.parser")
                next_href = western_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_western.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=western&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_western.append(page_url)
            title_number += 50

    print("get_urls_genre_western method:", time.time() - start)

    return list_urls_western


def get_urls_genre_action():
    start = time.time()
    action_url = get_urls_all_genres()[0].get('url')
    list_urls_action = [action_url]
    response = requests.get(action_url)
    action_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = action_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=action&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_action.append(page_url)
            title_number += 50
        else:
            target = action_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                action_genre_pages = bs(next_response.text, "html.parser")
                next_href = action_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_action.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=action&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_action.append(page_url)
            title_number += 50

    print("get_urls_genre_action method:", time.time() - start)
    return list_urls_action


def get_urls_genre_adventure():
    start = time.time()
    adventure_url = get_urls_all_genres()[1].get('url')
    list_urls_adventure = [adventure_url]
    response = requests.get(adventure_url)
    adventure_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = adventure_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=adventure&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_adventure.append(page_url)
            title_number += 50
        else:
            target = adventure_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                adventure_genre_pages = bs(next_response.text, "html.parser")
                next_href = adventure_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_adventure.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=adventure&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_adventure.append(page_url)
            title_number += 50

    print("get_urls_genre_adventure method:", time.time() - start)

    return list_urls_adventure


def get_urls_genre_animation():
    start = time.time()
    animation_url = get_urls_all_genres()[2].get('url')
    list_urls_animation = [animation_url]
    response = requests.get(animation_url)
    animation_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = animation_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=animation&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_animation.append(page_url)
            title_number += 50
        else:
            target = animation_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                animation_genre_pages = bs(next_response.text, "html.parser")
                next_href = animation_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_animation.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=animation&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_animation.append(page_url)
            title_number += 50

    print("get_urls_genre_animation method:", time.time() - start)

    return list_urls_animation


def get_urls_genre_comedy():
    start = time.time()
    comedy_url = get_urls_all_genres()[4].get('url')
    list_urls_comedy = [comedy_url]
    response = requests.get(comedy_url)
    comedy_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = comedy_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_comedy.append(page_url)
            title_number += 50
        else:
            target = comedy_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                comedy_genre_pages = bs(next_response.text, "html.parser")
                next_href = comedy_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_comedy.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_comedy.append(page_url)
            title_number += 50

    print("get_urls_genre_comedy method:", time.time() - start)

    return list_urls_comedy


def get_urls_genre_biography():
    start = time.time()
    biography_url = get_urls_all_genres()[3].get('url')
    list_urls_biography = [biography_url]
    response = requests.get(biography_url)
    biography_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = biography_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=biography&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_biography.append(page_url)
            title_number += 50
        else:
            target = biography_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                biography_genre_pages = bs(next_response.text, "html.parser")
                next_href = biography_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_biography.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=biography&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_biography.append(page_url)
            title_number += 50

    print("get_urls_genre_biography method:", time.time() - start)

    return list_urls_biography


def get_urls_genre_crime():
    start = time.time()
    crime_url = get_urls_all_genres()[5].get('url')
    list_urls_crime = [crime_url]
    response = requests.get(crime_url)
    crime_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = crime_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=crime&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_crime.append(page_url)
            title_number += 50
        else:
            target = crime_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                crime_genre_pages = bs(next_response.text, "html.parser")
                next_href = crime_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_crime.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=crime&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_crime.append(page_url)
            title_number += 50

    print("get_urls_genre_crime method:", time.time() - start)

    return list_urls_crime


def get_urls_genre_documentary():
    start = time.time()
    documentary_url = get_urls_all_genres()[6].get('url')
    list_urls_documentary = [documentary_url]
    response = requests.get(documentary_url)
    documentary_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = documentary_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=documentary&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_documentary.append(page_url)
            title_number += 50
        else:
            target = documentary_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                documentary_genre_pages = bs(next_response.text, "html.parser")
                next_href = documentary_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_documentary.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=documentary&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_documentary.append(page_url)
            title_number += 50

    print("get_urls_genre_documentary method:", time.time() - start)

    return list_urls_documentary


def get_urls_genre_drama():
    start = time.time()
    drama_url = get_urls_all_genres()[7].get('url')
    list_urls_drama = [drama_url]
    response = requests.get(drama_url)
    drama_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = drama_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=drama&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_drama.append(page_url)
            title_number += 50
        else:
            target = drama_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                drama_genre_pages = bs(next_response.text, "html.parser")
                next_href = drama_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_drama.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=drama&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_drama.append(page_url)
            title_number += 50

    print("get_urls_genre_drama method:", time.time() - start)

    return list_urls_drama


def get_urls_genre_family():
    start = time.time()
    family_url = get_urls_all_genres()[8].get('url')
    list_urls_family = [family_url]
    response = requests.get(family_url)
    family_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = family_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=family&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_family.append(page_url)
            title_number += 50
        else:
            target = family_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                family_genre_pages = bs(next_response.text, "html.parser")
                next_href = family_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_family.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=family&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_family.append(page_url)
            title_number += 50

    print("get_urls_genre_family method:", time.time() - start)

    return list_urls_family


def get_urls_genre_fantasy():
    start = time.time()
    fantasy_url = get_urls_all_genres()[9].get('url')
    list_urls_fantasy = [fantasy_url]
    response = requests.get(fantasy_url)
    fantasy_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = fantasy_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_fantasy.append(page_url)
            title_number += 50
        else:
            target = fantasy_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                fantasy_genre_pages = bs(next_response.text, "html.parser")
                next_href = fantasy_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_fantasy.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_fantasy.append(page_url)
            title_number += 50

    print("get_urls_genre_fantasy method:", time.time() - start)

    return list_urls_fantasy


def get_urls_genre_film_noir():
    start = time.time()
    film_noir_url = get_urls_all_genres()[10].get('url')
    list_urls_film_noir = [film_noir_url]
    response = requests.get(film_noir_url)
    film_noir_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = film_noir_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=film-noir&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_film_noir.append(page_url)
            title_number += 50
        else:
            target = film_noir_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                film_noir_genre_pages = bs(next_response.text, "html.parser")
                next_href = film_noir_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_film_noir.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=film-noir&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_film_noir.append(page_url)
            title_number += 50

    print("get_urls_genre_film_noir method:", time.time() - start)

    return list_urls_film_noir


def get_urls_genre_history():
    start = time.time()
    history_url = get_urls_all_genres()[11].get('url')
    list_urls_history = [history_url]
    response = requests.get(history_url)
    history_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = history_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=history&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_history.append(page_url)
            title_number += 50
        else:
            target = history_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                history_genre_pages = bs(next_response.text, "html.parser")
                next_href = history_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_history.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=history&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_history.append(page_url)
            title_number += 50

    print("get_urls_genre_history method:", time.time() - start)

    return list_urls_history


def get_urls_genre_horror():
    start = time.time()
    horror_url = get_urls_all_genres()[12].get('url')
    list_urls_horror = [horror_url]
    response = requests.get(horror_url)
    horror_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = horror_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=horror&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_horror.append(page_url)
            title_number += 50
        else:
            target = horror_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                horror_genre_pages = bs(next_response.text, "html.parser")
                next_href = horror_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_horror.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=horror&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_horror.append(page_url)
            title_number += 50

    print("get_urls_genre_horror method:", time.time() - start)

    return list_urls_horror


def get_urls_genre_music():
    start = time.time()
    music_url = get_urls_all_genres()[13].get('url')
    list_urls_music = [music_url]
    response = requests.get(music_url)
    music_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = music_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=music&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_music.append(page_url)
            title_number += 50
        else:
            target = music_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                music_genre_pages = bs(next_response.text, "html.parser")
                next_href = music_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_music.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=music&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_music.append(page_url)
            title_number += 50

    print("get_urls_genre_music method:", time.time() - start)

    return list_urls_music


def get_urls_genre_musical():
    start = time.time()
    musical_url = get_urls_all_genres()[14].get('url')
    list_urls_musical = [musical_url]
    response = requests.get(musical_url)
    musical_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = musical_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=musical&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_musical.append(page_url)
            title_number += 50
        else:
            target = musical_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                musical_genre_pages = bs(next_response.text, "html.parser")
                next_href = musical_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_musical.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=musical&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_musical.append(page_url)
            title_number += 50

    print("get_urls_genre_musical method:", time.time() - start)

    return list_urls_musical


def get_urls_genre_mystery():
    start = time.time()
    mystery_url = get_urls_all_genres()[15].get('url')
    list_urls_mystery = [mystery_url]
    response = requests.get(mystery_url)
    mystery_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = mystery_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=mystery&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_mystery.append(page_url)
            title_number += 50
        else:
            target = mystery_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                mystery_genre_pages = bs(next_response.text, "html.parser")
                next_href = mystery_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_mystery.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=mystery&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_mystery.append(page_url)
            title_number += 50

    print("get_urls_genre_mystery method:", time.time() - start)

    return list_urls_mystery


def get_urls_genre_romance():
    start = time.time()
    romance_url = get_urls_all_genres()[16].get('url')
    list_urls_romance = [romance_url]
    response = requests.get(romance_url)
    romance_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = romance_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=romance&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_romance.append(page_url)
            title_number += 50
        else:
            target = romance_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                romance_genre_pages = bs(next_response.text, "html.parser")
                next_href = romance_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_romance.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=romance&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_romance.append(page_url)
            title_number += 50

    print("get_urls_genre_romance method:", time.time() - start)

    return list_urls_romance


def get_urls_genre_sci_fi():
    start = time.time()
    sci_fi_url = get_urls_all_genres()[17].get('url')
    list_urls_sci_fi = [sci_fi_url]
    response = requests.get(sci_fi_url)
    sci_fi_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = sci_fi_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=sci-fi&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_sci_fi.append(page_url)
            title_number += 50
        else:
            target = sci_fi_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                sci_fi_genre_pages = bs(next_response.text, "html.parser")
                next_href = sci_fi_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_sci_fi.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=sci-fi&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_sci_fi.append(page_url)
            title_number += 50

    print("get_urls_genre_sci_fi method:", time.time() - start)

    return list_urls_sci_fi


def get_urls_genre_short_film():
    start = time.time()
    short_film_url = get_urls_all_genres()[18].get('url')
    list_urls_short_film = [short_film_url]
    response = requests.get(short_film_url)
    short_film_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = short_film_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=short&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_short_film.append(page_url)
            title_number += 50
        else:
            target = short_film_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                short_film_genre_pages = bs(next_response.text, "html.parser")
                next_href = short_film_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_short_film.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=short&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_short_film.append(page_url)
            title_number += 50

    print("get_urls_genre_short_film method:", time.time() - start)

    return list_urls_short_film


def get_urls_genre_superhero():
    start = time.time()
    superhero_url = get_urls_all_genres()[20].get('url')
    list_urls_superhero = list()
    response = requests.get(superhero_url)
    superhero_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = superhero_genre.find('div', {'class': 'desc'}).text
    number_of_titles = re.findall("\d", number_of_titles)[3:]
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        for i in range(number_of_pages):
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=T1Q8CSME92J5EA9KD18E&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page={i + 1}'
            list_urls_superhero.append(page_url)
            title_number += 50
            if i == number_of_pages - 1:
                last_page = f'https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=T1Q8CSME92J5EA9KD18E&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page={number_of_pages}'
                list_urls_superhero.append(last_page)
        else:
            target = superhero_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                superhero_genre_pages = bs(next_response.text, "html.parser")
                next_href = superhero_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_superhero.append(target)

    else:
        for i in range(number_of_pages):
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=T1Q8CSME92J5EA9KD18E&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page={i + 1}'
            list_urls_superhero.append(page_url)
            title_number += 50
        last_page = f'https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=T1Q8CSME92J5EA9KD18E&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page={number_of_pages}'
        list_urls_superhero.append(last_page)

    print("get_urls_genre_superhero method:", time.time() - start)

    return list_urls_superhero


def get_urls_genre_thriller():
    start = time.time()
    thriller_url = get_urls_all_genres()[21].get('url')
    list_urls_thriller = [thriller_url]
    response = requests.get(thriller_url)
    thriller_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = thriller_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_thriller.append(page_url)
            title_number += 50
        else:
            target = thriller_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                thriller_genre_pages = bs(next_response.text, "html.parser")
                next_href = thriller_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_thriller.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=thriller&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_thriller.append(page_url)
            title_number += 50

    print("get_urls_genre_thriller method:", time.time() - start)

    return list_urls_thriller


def get_urls_genre_war():
    start = time.time()
    genre_war_url = get_urls_all_genres()[22].get('url')
    list_urls_genre_war = [genre_war_url]
    response = requests.get(genre_war_url)
    genre_war_genre = bs(response.text, "html.parser")

    # Finding how many pages this genre section has
    number_of_titles = genre_war_genre.find('tr').find('td').text
    number_of_titles = re.findall("\d", number_of_titles)
    number_of_titles = ''.join(number_of_titles)
    number_of_titles = int(number_of_titles)
    number_of_pages = round(number_of_titles / 50)

    title_number = 51
    if number_of_titles > 10000:
        while title_number < number_of_titles:
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=genre-war&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_genre_war.append(page_url)
            title_number += 50
        else:
            target = genre_war_url
            for i in range((number_of_pages - 1)):
                next_response = requests.get(target)
                genre_war_genre_pages = bs(next_response.text, "html.parser")
                next_href = genre_war_genre_pages.find('a', {'class': 'lister-page-next next-page'}).get('href')
                target = f"https://www.imdb.com{next_href}"
                list_urls_genre_war.append(target)

    else:
        while title_number < number_of_titles:
            if title_number > number_of_titles:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=genre-war&start={title_number}&explore=genres&ref_=adv_nxt'
            list_urls_genre_war.append(page_url)
            title_number += 50

    print("get_urls_genre_genre_war method:", time.time() - start)

    return list_urls_genre_war


def create_list_urls(name_genre: str, list_urls: list):
    file = open(f"list_urls_{name_genre}.p", "wb")
    pickle.dump(list_urls, file)
    file.close()
    return file


def make_request(url):
    try:
        response = requests.get(url)
        movies = parse_data(response.text)
        return movies
    except:
        return None


def parse_data(html_page: str):
    parser = bs(html_page, "html.parser")

    data = parser.find_all("div", {"class": "lister-item mode-advanced"})

    h3_selector = parser.find_all('h3', {'class': 'lister-item-header'})
    p_selector = parser.find_all('p', {'class': 'text-muted'})
    # list_content_selector = parser.find_all('div', {'class': 'lister-item-content'})

    num_p = 0
    num_p_synopsis = 1

    movies_list = list()
    for i, card in enumerate(data):

        movie_title = h3_selector[i].find('a').text

        movie_url = h3_selector[i].find('a').get("href")

        title = movie_title

        if h3_selector[i].find('span', {'class': 'lister-item-year text-muted unbold'}) is None or '':
            movie_year = "Isn't Available"
        else:
            movie_year = h3_selector[i].find('span', {'class': 'lister-item-year text-muted unbold'}).text

        year = movie_year[1:-1]

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

        """span_selector = list_content_selector[i].find('p', {'class': 'sort-num_votes-visible'})
        if span_selector[0] is None:
            movie_num_votes = "Isn't Available"
        else:
            movie_num_votes = span_selector.find_all('span', {'name': 'nv'})[0].text

        num_votes = movie_num_votes

        if span_selector[1] is False:
            movie_collection = "Isn't Available"
        else:
            movie_collection = span_selector.find_all('span', {'name': 'nv'})[1].text

        collection = movie_collection

        if list_content_selector[i].find('div', {'class': 'ratings-bar'}) is None:
            movie_imdb_rating = "Isn't Available"
        else:
            rating_bars_selector = list_content_selector[i].find('div', {'class': 'ratings-bar'})
            movie_imdb_rating = rating_bars_selector.find('div', {'class': 'inline-block ratings-imdb-rating'}).get('data-value')

        imdb_rating = movie_imdb_rating"""

        movie_data = {
            'title': clean_data(title),
            'year': year,
            'certificate': clean_data(certificate),
            'runtime': clean_data(runtime),
            'genre': clean_data(genre),
            'synopsis': clean_data(synopsis),
            # 'imdb_rating': imdb_rating,
            # 'num_votes': num_votes,
            # 'collection': collection,
            'link': f"https://www.imdb.com{movie_url}"
            }

        movies_list.append(movie_data)

        num_p += 2
        num_p_synopsis += 2
    return movies_list


def clean_data(value: str):
    new_value = re.sub("/(\r\n|\n|\r)/gm", "", value)
    new_value = re.sub("\s+", " ", new_value)
    new_value = re.sub('\"', "", new_value)

    return new_value


def execute(list_urls: list):
    list_movies = list()
    try:
        for i in list_urls:
            movies = make_request(i)
            list_movies.extend(movies)
            print(movies)
        return list_movies
    except:
        return list_movies


def load_files():
    list_urls = list()
    file_urls = "C:/Users/Pedro Paulo/WebScraping-project/IMDBSpyder-Lauro/list_urls_pages_all_genres/"
    for file in os.listdir(file_urls):
        if file.endswith(".p"):
            pickle_file = open(os.path.join(file_urls, file), 'rb')
            data = pickle.load(pickle_file)
            list_urls.extend(data)

    print(len(list_urls), list_urls[0])
    return list_urls


################################################################
# Main
################################################################

def main():
    start = time.time()
    number_threads = int(sys.argv[1])
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
    list_urls = load_files()
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
    print(list_movies)
    print("main method:", time.time() - start)


if __name__ == "__main__":
    main()

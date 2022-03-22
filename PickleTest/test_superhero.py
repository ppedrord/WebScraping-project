from bs4 import BeautifulSoup as bs
import requests
import pickle
import time
import re

"""def get_urls_genre_superhero():
    start = time.time()
    superhero_url = "https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=T1Q8CSME92J5EA9KD18E&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_21"
    list_urls_superhero = [superhero_url]
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

    return list_urls_superhero"""

action_url = "https://www.imdb.com/search/title/?title_type=feature&genres=action&start=51&explore=genres&ref_=adv_nxt"
response = requests.get(action_url)
html_page = response.text


def clean_data(value: str):
    new_value = re.sub("/(\r\n|\n|\r)/gm", "", value)
    new_value = re.sub("\s+", " ", new_value)
    new_value = re.sub('\"', "", new_value)

    return new_value


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


print(parse_data(html_page))

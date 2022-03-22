from bs4 import BeautifulSoup as bs
import requests
import pickle
import time
import re


def get_urls_genre_superhero():
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

    return list_urls_superhero


get_urls_genre_superhero()

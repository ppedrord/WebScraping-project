from collections import namedtuple
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By


class IMDb:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://imdb.com'
        self.menu = 'imdbHeader-navDrawerOpen--desktop'  # ID
        self.search_by_genre = '//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[5]/span'  # XPATH
        self.sport_genre = '//*[@id="main"]/div[6]/span/div/div/div/div/div[4]/div/div[2]/div/a'  # XPATH
        self.movie_card = '.mode-advanced'  # CSS_SELECTOR
        self.movie_title = '.lister-item-header a'  # CSS_SELECTOR
        self.movie_year = 'lister-item-year text-muted unbold'  # CLASS
        self.movie_certificated = 'certificate'  # CLASS
        self.movie_runtime = 'runtime'  # CLASS
        self.movie_genre = 'genre'  # CLASS
        self.movie_imdb_rating = 'inline-block ratings-imdb-rating'  # CLASS
        self.movie_sinopse = '.ratings-bar+ .text-muted'  # CSS_SELECTOR
        self.event = namedtuple('Event',
                                'Title Year Certificated Runtime Genre Rating Sinopse')

    def navigate(self):
        self.driver.get(self.url)

    def click_menu(self):
        self.driver.find_element(By.ID, self.menu).click()

    def click_search_by_genre(self):
        self.driver.find_element(By.XPATH, self.search_by_genre).click()

    def click_genre_sport(self):
        self.driver.find_element(By.XPATH, self.sport_genre).click()

    def _get_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.movie_card)

    def _get_movie_title(self, movie_card):
        return movie_card.find_element(By.CLASS_NAME, self.movie_title)

    def _get_movie_year(self, movie_card):
        return movie_card.find_element(By.CLASS_NAME, self.movie_year)

    def _get_movie_certificated(self, movie_card):
        return movie_card.find_element(By.CLASS_NAME, self.movie_certificated)

    def _get_movie_runtime(self, movie_card):
        return movie_card.find_element(By.CLASS_NAME, self.movie_runtime)

    def _get_movie_imdb_rating(self, movie_card):
        return movie_card.find_element(By.CLASS_NAME, self.movie_imdb_rating)

    def _get_movie_sinopse(self, movie_card):
        return movie_card.find_element(By.CLASS_NAME, self.movie_sinopse)

    def get_all_data(self):
        cards = self._get_cards()
        for card in cards:
            yield self.event(self._get_movie_title(card).text,
                             self._get_movie_year(card).text,
                             self._get_movie_certificated(card).text,
                             self._get_movie_runtime(card).text,
                             self._get_movie_imdb_rating(card).text,
                             self._get_movie_sinopse(card).text)

    def event(self, text, text1, text2, text3, text4, text5):
        pass


browser = webdriver.Chrome()
imdb = IMDb(browser)
imdb.navigate()
imdb.click_menu()
imdb.click_search_by_genre()
imdb.click_genre_sport()

for event in imdb.get_all_data():
    pprint(event)

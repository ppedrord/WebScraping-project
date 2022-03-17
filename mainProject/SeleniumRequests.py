from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import re


class IMDb:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://imdb.com'
        self.menu = 'imdbHeader-navDrawerOpen--desktop'  # ID
        self.search_by_genre = '//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[5]/span'  # XPATH
        self.sport_genre = '//*[@id="main"]/div[6]/span/div/div/div/div/div[4]/div/div[2]/div/a'  # XPATH

    def navigate(self):
        self.driver.get(self.url)

    def click_menu(self):
        self.driver.find_element(By.ID, self.menu).click()

    def click_search_by_genre(self):
        self.driver.find_element(By.XPATH, self.search_by_genre).click()

    def click_genre_sport(self):
        self.driver.find_element(By.XPATH, self.sport_genre).click()


browser = webdriver.Chrome()
imdb = IMDb(browser)
imdb.navigate()
imdb.click_menu()
imdb.click_search_by_genre()
imdb.click_genre_sport()

base_url = 'https://www.imdb.com'
title_number = 1
url_pages = f'{base_url}/search/title/?title_type=feature&genres=sport&start=1&explore=genres&ref_=adv_nxt'
browser.get(url_pages)
html = browser.page_source
sport_genre = bs(html, "html.parser")


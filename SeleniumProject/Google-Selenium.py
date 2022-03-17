from selenium import webdriver
from selenium.webdriver.common.by import By


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://google.com.br'
        self.search_bar = 'q'       # name
        self.btn_search = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"    # xpath
        self.btn_lucky = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]"     # xpath

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element(By.NAME, 'q').send_keys(word)
        self.driver.find_element(By.XPATH, self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element(By.NAME, 'q').send_keys(word)
        self.driver.find_element(By.XPATH, self.btn_lucky).click()


browser = webdriver.Chrome()
google = Google(browser)
google.navigate()
google.search("Gol do deyvinho")
browser.quit()
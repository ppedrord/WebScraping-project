import requests
import random
import numpy as np
import time
from bs4 import BeautifulSoup as bs

url = 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&after=WzEzNDA4MCwidHQwOTk2OTYyIiwyMjY1MV0%3D&explore=genres'


def select_user_agent(url: str, delays=[1, 2, 3]):
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        ]
    delay = np.random.choice(delays)
    time.sleep(delay)

    # Pick a random user agent
    user_agent = random.choice(user_agent_list)
    # Set the headers
    headers = {'User-Agent': user_agent}
    # Make the request
    try:
        print('try:')
        response = requests.get(url, headers=headers)
        print("response:", response)
        html_page = bs(response.text, 'html.parser')
        print(html_page)
        # movies = parse_data(response.text)
    except:
        print("except:")
        big_delays = [5, 10, 15]
        response = select_user_agent(url, big_delays)
        print(response)

    if response.status_code == 200:
        return response
    else:
        return None


print(select_user_agent(url))

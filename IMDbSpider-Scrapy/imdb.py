import threading
import re
import scrapy


class MyThreads(threading.Thread):
    def __init__(self, target, name='MyThreads'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


number_of_threads = 5
list_threads = list()
for i in range(number_of_threads):
    list_words = IMDbSpider.divide_work(list, i, number_of_threads)
    thread = threading.Thread(name=str(i), target=dicio.execute, args=(list_words, i, counter))
    list_threads.append(thread)


class IMDbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ['https://www.imdb.com/']

    def parse(self, response):
        """
            A method to collect the link to the genres page

        :param response: A scrapy method to do a request
        :return: A quest on the link retrieved
        """

        links = response.xpath('//nav//div//div//ul/a[re:test(@href, "nv_ch_gr")]/@href').get()
        home_link = ["https://www.imdb.com", links]
        links = ''.join(home_link)
        yield scrapy.Request(
            response.urljoin(links),
            callback=self.parse_category
            )

    def parse_category(self, response):
        """
            A method to entering on the categories available

        :param response: A Scrapy method to do a request
        :return:
        """

        genre_sport = response.css('.article:nth-child(13) .table-cell:nth-child(4) .table-row:nth-child(2) a::attr('
                                   'href)').get()
        genre_link = ["https://www.imdb.com", genre_sport]
        sport = ''.join(genre_link)
        yield scrapy.Request(
            response.urljoin(sport),
            callback=self.divide_work
            )

    def divide_work(self, response):
        """
            A method to find all the url pages and divide work

        :param response: A Scrapy method to do a request
        :return:
        """

        advance_pages = []
        title_num = 1

        # Retrieving the number of movies in the genre
        number_of_movies = response.xpath('//div//table//td').get()
        number_of_movies = re.findall("\d", number_of_movies)
        number_of_movies = ''.join(number_of_movies)
        number_of_movies = int(number_of_movies)

        # Creating a list of url of all the pages in this genre section
        while title_num < number_of_movies:
            if title_num > number_of_movies:
                break
            page_url = f'https://www.imdb.com/search/title/?title_type=feature&genres=sport&start={title_num}&explore=genres&ref_=adv_nxt'
            advance_pages.append(page_url)
            title_num += 50

        return scrapy.Request(response.urljoin(advance_pages)), advance_pages

    def execute_scraping(self, response):
        """
            The method where the web scraping is executed

        :param response:
        :return:
        """
        movies = response.css('.lister-item-header a::attr(href)').getall()
        home_link = "https://www.imdb.com"
        movies_list = list()

        # Just a for statement to create a list with all the movies urls
        for split_url in movies:
            title_link = home_link + split_url
            movies_list.append(title_link)
        titles_list = response.css('.lister-item-header a::text').getall()
        years_list = response.css('.text-muted.unbold::text').getall()
        sinopse_list = response.css('.text-muted+ .text-muted::text, .ratings-bar+ .text-muted').getall()
        genres_list = response.css('.genre::text').getall()
        directors_list = response.css('.text-muted+ p a:nth-child(1)::text').getall()

        # movie_card = response.css('.mode-advanced').getall()
        # for card in movie_card:
        #     title = card.css('').get()

        for i, v in enumerate(movies_list):
            title = titles_list[i]
            # year = years_list[i][1:-1]
            sinopse = sinopse_list[i].replace('<p class="text-muted">', '').replace('</p>', '')
            genre = genres_list[i]
            # director = directors_list[i]
            # if not response.css('.certificate::text').getall():
            #     certificate =
            title_url = movies_list[i]
            yield {
                "title": title,
                # "year": year,
                # "imdb_rating": '',
                "sinopse": sinopse,
                # "director": director,
                # "stars": '',
                "genres": genre,
                # "length": '',
                # "certificate": '',
                "title_url": title_url
                }

        next_page_url = response.css('.next-page::attr(href)').get()
        next_page_url = home_link + next_page_url
        yield scrapy.Request(
            response.urljoin(next_page_url),
            callback=self.parse_movies_list
            )

    pass


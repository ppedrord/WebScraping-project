import scrapy


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

        genre_action = response.css('.article:nth-child(13) .table-cell:nth-child(1) .table-row:nth-child(1) a::attr('
                                    'href)').get()
        genre_link = ["https://www.imdb.com", genre_action]
        action = ''.join(genre_link)
        yield scrapy.Request(
            response.urljoin(action),
            callback=self.parse_movies_list
            )

    def parse_movies_list(self, response):
        """
            A method to collect the url to the movie pages

        :param response: A Scrapy method to do a request
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
            yield {
                "title": title,
                # "year": year,
                # "imdb_rating": '',
                "sinopse": sinopse,
                # "director": director,
                # "stars": '',
                "genres": genre,
                # "length": '',
                # "certificate": ''
                }

        next_page_url = response.css('.next-page::attr(href)').get()
        next_page_url = home_link + next_page_url
        yield scrapy.Request(
            response.urljoin(next_page_url),
            callback=self.parse_movies_list
            )

    pass

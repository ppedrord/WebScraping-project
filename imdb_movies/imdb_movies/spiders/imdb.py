import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    # allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for movies in response.css(".titleColumn"):
            yield {
                "title": movies.css(".titleColumn a ::text").get(),
                "year": movies.css(".secondaryInfo ::text").get()[1:-1],
                "imdbRating": response.css("strong ::text").get()
                }
        pass

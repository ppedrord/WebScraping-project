import scrapy


class AosFatosSpider(scrapy.Spider):
    name = "aos_fatos"

    start_urls = ['https://aosfatos.org']

    def parse(self, response, **kwargs):
        links = response.xpath(
            '//div//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_category
                )

    def parse_category(self, response):
        news = response.xpath('//section/div/a/@href').getall()
        for new_url in news:
            yield scrapy.Request(
                response.urljoin(new_url),
                callback=self.parse_new
                )
        pass

    def parse_new(self, response):
        title = response.css("article h1::text").get()
        date = " ".join(response.css(".publish-date::text").get().split())
        quotes = response.css("blockquote")
        for quote in quotes:
            quote_text = quote.css("::text").get()
        status_quotes = ""
        url = ""
        yield {
            "title": title,
            "date": date,
            "url": response.url
            }
        pass

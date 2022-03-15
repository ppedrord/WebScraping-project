import scrapy
import time


def timer_method(func):
    """ Calculates how long it takes for a function to run
    """

    def wrapper(*args, **kwargs):
        before = time.time()
        a = func(*args, **kwargs)
        print(f"Timer function {func.__name__} : {time.time() - before} seconds")
        return a

    return wrapper


class AosFatosSpider(scrapy.Spider):
    name = "aos_fatos"
    start_urls = ['https://aosfatos.org']

    def parse(self, response):
        links = response.xpath('//div//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
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
                callback=self.parse_news
                )
        pages_url = response.css(".current-page+ a::attr(href) ").getall()
        for page in pages_url:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_category
                )

    def parse_news(self, response):
        title = response.css("article h1::text").get()
        date = " ".join(response.css(".publish-date::text").get().split())

        list_status = []

        if not response.css("figcaption figcaption::text").getall():
            status = response.xpath('//p/img[re:test(@data-image-id, "png")]/@data-image-id').getall()
            for i in status:

                if i == "falso.png":
                    list_status.append("FALSO")

                elif i == "contraditorio.png":
                    list_status.append("CONTRADITÓRIO")

                elif i == "insustentavel.png":
                    list_status.append("INSUSTENTÁVEL")

                elif i == "exagerado.png":
                    list_status.append("EXAGERADO")

                elif i == "impreciso.png":
                    list_status.append("IMPRECISO")

                elif i == "verdadeiro.png":
                    list_status.append("VERDADEIRO")
        else:
            if not response.css("figcaption figcaption::text").getall():
                list_status = response.css("figcaption").getall()

            else:
                status = response.css("figcaption figcaption::text").getall()
                for i in status:

                    if i == "FALSO":
                        list_status.append(i)

                    elif i == "CONTRADITÓRIO":
                        list_status.append(i)

                    elif i == "INSUSTENTÁVEL":
                        list_status.append(i)

                    elif i == "EXAGERADO":
                        list_status.append(i)

                    elif i == "IMPRECISO":
                        list_status.append(i)

                    elif i == "VERDADEIRO":
                        list_status.append(i)
        quotes = response.css("blockquote")
        for j, quote in enumerate(quotes):
            quote_text = quote.css("::text").get()
            quote_status = list_status[j]
            if not list_status:
                continue
            if not quote_status:
                continue

            yield {
                "title": title,
                "date": date,
                "quote_text": quote_text,
                "status": quote_status,
                "url": response.url
                }

        pass



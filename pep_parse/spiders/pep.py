import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """
    Паук для парсинга документов PEP.
    Собирает информацию о статусах PEP.
    """
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """Собирает ссылки на документы PEP из общей таблицы."""
        num_index = response.xpath("//*[@id='numerical-index']").css("tbody")
        all_peps_links = num_index.css("a::attr(href)").getall()
        for link in all_peps_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items."""
        title_pep = response.css("h1.page-title::text").get()
        status = response.css("dt:contains('Status') + dd abbr::text").get()
        data = {
            "number": int(title_pep.split(" ")[1]),
            "name": title_pep,
            "status": status
        }
        yield PepParseItem(data)

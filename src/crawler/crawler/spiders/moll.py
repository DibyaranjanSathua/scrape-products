import colorama
import scrapy


class ScreenalSpider(scrapy.Spider):
    name = "moll"
    allowed_domains = ["moll-textil.com"]
    not_found = "__NOT_FOUND__"

    def __init__(self, *args, **kwargs):
        super(ScreenalSpider, self).__init__(*args, **kwargs)
        self.start_url = "http://moll-textil.com/"
        self.start_parse = self.parse_products
        # List of dict where each dict has key as product category and value as list of products
        self.products = []

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.start_parse)

    def parse_products(self, response):

        """ Parse products """
        print(f"\t{colorama.Fore.CYAN}Crawling: {response.url}")

        products = response.xpath('//div/a/p/text()').getall()

        self.products = [
            {'products': products}]

        self.logger.info(f"Products: {self.products}")
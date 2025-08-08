import scrapy
from ..items import QuotesScraperItem

class QuotesSpider(scrapy.Spider):
    name="quotes"
    start_urls=[
        "https://quotes.toscrape.com/page/1/",
    ]
    def parse(self,response):
        #All data goes to response variable
        all_div_quotes= response.css('div.quote')
        for quote_div in all_div_quotes:
            items= QuotesScraperItem()
            text=quote_div.css("span.text::text").extract_first()
            author=quote_div.css(".author::text").extract_first()
            tags=quote_div.css(".tag::text").extract()
            items['text']=text
            items['author']=author
            items['tags']=tags
            yield items
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksScraperItem(scrapy.Item):
    # define the fields for your item here like:
    book_imagecover_link=scrapy.Field()
    rating=scrapy.Field()
    book_name=scrapy.Field()
    price= scrapy.Field()
    stock_check=scrapy.Field()

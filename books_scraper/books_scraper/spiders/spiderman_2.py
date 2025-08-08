from ..items import BooksScraperItem
import scrapy


class BookScraperItem(scrapy.Spider):
    name = "books"
    start_urls = [
        'https://books.toscrape.com/catalogue/category/books_1/index.html'
    ]

    def parse(self, response):
        all_div_books = response.css("article.product_pod")
        for book_div in all_div_books:
            items = BooksScraperItem()
            image = book_div.css("img::attr(src)").extract()
            image=image[0].replace('../../..','https://books.toscrape.com/')
            book_rating = book_div.css("p.star-rating::attr(class)").extract()
            book_rating[0]=book_rating[0].replace("star-rating ","")
            name = book_div.css("h3 a::attr(title)").extract()
            book_price = book_div.css(".price_color::text").extract()
            book_stock_check = book_div.css(".instock.availability::text").extract()
            book_stock_check=book_stock_check[1].strip()
            items["book_imagecover_link"] = image
            items["rating"] = book_rating
            items["book_name"] = name
            items["price"] = book_price
            items['stock_check']= book_stock_check
            yield items
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

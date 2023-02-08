from scrapy import Spider
# from ebook_scraper.item import EbookScraperItem 
# OR
from ..items import EbookScraperItem
from scrapy.loader import ItemLoader

def get_price_as_float(price):
    return float(price[1:])

class EbookSpider(Spider):
    name="ebook"
    start_urls = ['https://books.toscrape.com']
    def parse(self, response):
        print('---------------------------------------------')
        ebooks = response.css('article')
        
        for ebook in ebooks:
            loader = ItemLoader(item=EbookScraperItem(), selector=ebook)
            # loader.add_value('title',ebook.css('h3 a::attr(title)').get())
            loader.add_css('title', 'h3 a::attr(title)')
            loader.add_value('price', ebook.css('p.price_color::text').get())

            yield loader.load_item()
        

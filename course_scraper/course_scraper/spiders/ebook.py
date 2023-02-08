from scrapy import Spider, Request
# from ebook_scraper.item import EbookScraperItem 
# OR
from ..items import EbookScraperItem
from scrapy.loader import ItemLoader

def get_price_as_float(price):
    return float(price[1:])

class EbookSpider(Spider):
    name="ebook"
    start_urls = ['https://books.toscrape.com/catalogue/category/books/sequential-art_5/']

    def __init__(self):
        super().__init__()
        self.page_count = 0

    cols = ['title','price']
    def parse(self, response):
        print('---------------------------------------------')
        ebooks = response.css('article')
        self.page_count += 1
        for ebook in ebooks:
            loader = ItemLoader(item=EbookScraperItem(), selector=ebook)
            # loader.add_value('title',ebook.css('h3 a::attr(title)').get())
            loader.add_css('title', 'h3 a::attr(title)')
            loader.add_value('price', ebook.css('p.price_color::text').get())

            yield loader.load_item()
        print('Page Count: >>>>>>>>>>>>>>>>>>>>>>>>>>.', self.page_count)
        next_btn = response.css('li.next a').get()
       
        if(next_btn):
            next_url = response.css('li.next a::attr(href)').get()
            next_page_complete_url = self.start_urls[0] + '/' + next_url
            yield Request(url=next_page_complete_url)
       

      
        

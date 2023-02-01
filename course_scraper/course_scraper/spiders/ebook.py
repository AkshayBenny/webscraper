from scrapy import Spider
# from ebook_scraper.item import EbookScraperItem 
# OR
from ..items import EbookScraperItem

class EbookSpider(Spider):
    name="ebook"
    start_urls = ['https://books.toscrape.com']
    def parse(self, response):
        print('---------------------------------------------')
        ebooks = response.css('article')
        
        for ebook in ebooks:
            # ebooks = response.css('article.product_pod')
            # title = ebook.css('h3 a::attr(title)').get()
            # OR
            ebook_item = EbookScraperItem()
            ebook_item['title'] = response.css('article.product_pod')
            ebook_item['price'] = response.css('article.product_pod')
            # 
            # 
            # OR 
            title2 = ebook.css('h3 a').attrib['title']
            
            price = ebook.css('p.price_color::text').get()
            # yield {
            #     'title': title,
            #     'price': price
            # }
            # OR
            yield ebook_item
            # # Css selectors
            # title_selected_with_css = ebook.css('a::text').get()
            # price_selected_with_css = ebook.css('p.price_color::text').get()

            # #Or use xpath to select the elements
            # title_selected_with_xpath = ebook.xpath('//h3/a/text()').get()
            # price_selected_with_xpath = ebook.xpath("//p[@class='price_color']/text()").get() 

            # # Attribute selector for css
            # # This selects a tags that has got a title attribute
            # title_selected_with_css_attribute = ebook.css('a[title]').get()

            # print(title_selected_with_css_attribute)
            
            # yield {
            #     "title_selected_with_css":title_selected_with_css,
            #     "price_selected_with_css":price_selected_with_css
            # }
            # # scrapy crawl course -o course.json

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# yield and generator function
names= ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
def normal_function():
    for name in names:
        return name

name_value = normal_function()
# here name_value is only one value, it is not a list of values because in the first loop, a value is returned and the loop is terminated
# So we use yield to return a list of values 

def generator_function():
    for name in names:
        return name

new_names = generator_function()
# here the new_names will have the value in the form <generator object generator_function at 0x0000020B1B2B0F48>
# we can use for loop to get the values from the generator function using
for name in new_names:
    print(name)



# Scrapy, BeautifulSoup, Selenium
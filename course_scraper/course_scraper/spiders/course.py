from scrapy import Spider

class EbookSpider(Spider):
    name="course"
    start_urls = ['https://books.toscrape.com']
    def parse(self, response):
        print('---------------------------------------------')
        ebooks = response.css('article')
        
        for ebook in ebooks:
            # Css selectors
            title_selected_with_css = ebook.css('a::text').get()
            price_selected_with_css = ebook.css('p.price_color::text').get()

            #Or use xpath to select the elements
            title_selected_with_xpath = ebook.xpath('//h3/a/text()').get()
            price_selected_with_xpath = ebook.xpath("//p[@class='price_color']/text()").get() 

            # Attribute selector for css
            # This selects a tags that has got a title attribute
            title_selected_with_css_attribute = ebook.css('a[title]').get()

            print(title_selected_with_css_attribute)
            
            yield {
                "title_selected_with_css":title_selected_with_css,
                "price_selected_with_css":price_selected_with_css
            }
            # scrapy crawl course -o course.json

from scrapy import Item, Field


class CourseScraperItem(Item):
    #    
    pass

class EbookScraperItem(Item):
    title = Field()
    price = Field()
    pass

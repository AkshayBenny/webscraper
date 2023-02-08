from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
# Mapcompose is used to apply a transformation to a particular value
def get_price_as_float(price):
    return float(price[1:])


class CourseScraperItem(Item):
    #    
    pass

class EbookScraperItem(Item):
    title = Field()
    price = Field(
        input_processor = MapCompose(get_price_as_float),
        output_processor = TakeFirst()
    )
    pass

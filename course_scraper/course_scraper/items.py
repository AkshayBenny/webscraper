from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
# Mapcompose is used to apply a transformation to a particular value
def get_price_as_float(price):
    return float(price.replace('\u00a3', ''))


class CourseScraperItem(Item):
    #    
    pass

class EbookScraperItem(Item):
    title = Field(output_processor = TakeFirst())
    # if take first is not passed in then it returns a list
    # Can pass in multiple functions into MapCompose to apply multiple transformations
    price = Field(
        input_processor = MapCompose(get_price_as_float),
        output_processor = TakeFirst()
    )
    pass


# scrapy crawl course -o course.json    appends course data to course.json
# Use -O to overwrite course.json
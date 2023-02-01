from scrapy import Spider

class CourseSpider(Spider):
    name="course"
    start_urls = ['https://books.toscrape.com']
    def parse(self, response):
        print('---------------------------------------------')
        courses = response.css('article')
        
        for course in courses:
            # Css selectors
            title_selected_with_css = course.css('a::text').get()
            price_selected_with_css = course.css('p.price_color::text').get()

            #Or use xpath to select the elements
            title_selected_with_xpath = course.xpath('//h3/a/text()').get() 
            
            yield {
                "title_selected_with_css":title_selected_with_css,
                "price_selected_with_css":price_selected_with_css
            }
            # scrapy crawl course -o course.json

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
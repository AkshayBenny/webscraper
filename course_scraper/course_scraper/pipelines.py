from openpyxl import Workbook
from itemadapter import ItemAdapter


class EbookScraperPipeline:
    # here spider is the instance of the currencly running spider
    def open_spider(self,spider):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = 'Ebooks' #used to set the title of the sheet in excel file
        # self.sheet.append(['Title','Price']) OR
        self.sheet.append(spider.cols)



    def process_item(self, item, spider):
        self.sheet.append([item['title'],item['price']])

    def close_spider(self,spider):
        self.workbook.save('ebooks.xlsx')
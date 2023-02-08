from pymongo import MongoClient
from itemadapter import ItemAdapter


class EbookScraperPipeline:
    # here spider is the instance of the currencly running spider
    def open_spider(self,spider):
        self.client = MongoClient(
            host="mongodb+srv://admin:admin@cluster0.rsqjb.mongodb.net/?retryWrites=true&w=majority",
            connect=False
        )
        self.collection = self.client.get_database('scraper').get_collection('ebooks')



    def process_item(self, item, spider):
        # self.collection.insert_one({
        #     'title': item['title'],
        #     'price': item['price']
        # })
        # OR
        self.collection.insert_one(ItemAdapter(item).asdict())

    def close_spider(self,spider):
        self.client.close()


    # mongodb+srv://admin:<password>@cluster0.rsqjb.mongodb.net/?retryWrites=true&w=majority
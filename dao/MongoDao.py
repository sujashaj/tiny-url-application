from mongo import MongoClient


class MongoDao:
    def __init__(self, host='localhost', port=27017):
        self.mongo_client = MongoClient(f'mongodb://{host}:{port}/')
        self.db = self.mongo_client['tinyurl']

    def get_url(self, short_url):
        url_entry = self.db.urls.find_one({'short_url': short_url})
        return url_entry['full_url'] if url_entry else None

    def set_url(self, short_url, full_url):
        self.db.urls.insert_one({'short_url': short_url, 'full_url': full_url})


from pymongo import MongoClient
import os

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')


class MongoDao:
    def __init__(self):
        self.mongo_client = MongoClient(f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority&appName=Cluster0')
        self.db = self.mongo_client['tinyurl']

    def get_short_url(self, full_url):
        url_entry = self.db.urls.find_one({'full_url': full_url})
        return url_entry['short_url'] if url_entry else None

    def get_full_url(self, short_url):
        url_entry = self.db.urls.find_one({'short_url': short_url})
        return url_entry['full_url'] if url_entry else None

    def set_url(self, short_url, full_url):
        self.db.urls.insert_one({'short_url': short_url, 'full_url': full_url})


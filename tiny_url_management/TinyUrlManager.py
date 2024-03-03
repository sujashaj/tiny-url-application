import random
import string


class TinyUrlManager:
    def __init__(self, redis_dao, mongo_dao):
        self.redis_dao = redis_dao
        self.mongo_dao = mongo_dao

    def generate_random_key(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(self.key_length))

    def generate_key(self, full_url):
        key_candidate = self.generate_random_key()
        while self.mongo_dao.get_url(key_candidate):
            key_candidate = self.generate_random_key()
        self.mongo_dao.set_url(key_candidate, full_url)
        return key_candidate

    def get_url(self, short_url):
        full_url = self.redis_dao.get_url(short_url)

        if not full_url:
            full_url = self.mongo_dao.get_url(short_url)

            if not full_url:
                return None

            self.redis_dao.set_url(short_url, full_url)
        return full_url

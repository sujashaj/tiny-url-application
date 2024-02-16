class TinyUrlManager:
    def __init__(self, redis_dao, mongo_dao):
        self.redis_dao = redis_dao
        self.mongo_dao = mongo_dao

    def get_url(self, short_url):
        full_url = self.redis_dao.get_url(short_url)

        if not full_url:
            full_url = self.mongo_dao.get_url(short_url)

            if not full_url:
                return None

            self.redis_dao.set_url(short_url, full_url)
        return full_url

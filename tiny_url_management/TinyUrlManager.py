class TinyUrlManager:
    def __init__(self, redisDao, mongoDao):
        self.redisDao = redisDao
        self.mongoDao = mongoDao

    def get_url(self, short_url):
        full_url = self.redisDao.get_url(short_url)

        if not full_url:
            full_url = self.mongoDao.get_url(short_url)

            if not full_url:
                return None

            self.redisDao.set_url(short_url, full_url)
            return full_url

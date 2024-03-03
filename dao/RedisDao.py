import redis


class RedisDao:

    SHORT_PREFIX = "short:"
    FULL_PREFIX = "full:"
    def __init__(self, host='localhost', port=6379):
        self.redis_client = redis.StrictRedis(host=host, port=port, decode_responses=True)

    def get_short_url(self, full_url):
        return self.redis_client.get(RedisDao.FULL_PREFIX + full_url)

    def get_full_url(self, short_url):
        return self.redis_client.get(RedisDao.SHORT_PREFIX + short_url)

    def set_url(self, short_url, full_url):
        self.redis_client.set(RedisDao.SHORT_PREFIX + short_url, full_url)
        self.redis_client.set(RedisDao.FULL_PREFIX + full_url, short_url)

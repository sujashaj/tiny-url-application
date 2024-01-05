import redis


class RedisDao:
    def __init__(self, host='localhost', port=6379):
        self.redis_client = redis.StrictRedis(host=host, port=port, decode_responses=True)

    def get_url(self, short_url):
        return self.redis_client.get(short_url)

    def set_url(self, short_url, full_url):
        self.redis_client.set(short_url, full_url)
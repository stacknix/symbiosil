import redis


class RedisStore:

    def __init__(self, host, port, db, **kwargs):
        self.store = redis.Redis(host=host, port=port, db=db)

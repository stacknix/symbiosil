import redis
import pymongo


class RedisStore:

    def __init__(self, host, port, db, **kwargs):
        self.store = redis.Redis(host=host, port=port, db=db)


class MongoDBStore:

    def __init__(self, host, port, db, **kwargs):
        self.store = pymongo.MongoClient(host, port)

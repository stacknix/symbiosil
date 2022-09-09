import abc
import asyncio
import json
from threading import Thread

import redis

from symbiosil.commons import utils


class LiveData(abc.ABC):

    def __init__(self, channel: str, **config):
        self._config = config
        self._channel = channel
        self._closed = False

    @abc.abstractmethod
    def on_emit(self, channel: str):
        pass

    @abc.abstractmethod
    def on_publish(self, channel: str, value: str):
        pass

    @abc.abstractmethod
    def on_close(self, channel: str):
        pass

    def observer(self, callback):
        Thread(target=asyncio.run, args=(self.async_observer(callback),)).start()

    async def async_observer(self, callback):
        print("Async observer begins.")
        is_async = utils.is_async(callback)
        for value_string in self.on_emit(self._channel):
            if is_async:
                await callback(self, json.loads(value_string))
            else:
                callback(self, json.loads(value_string))
        print("Async observer exited.")

    def subscribe(self):
        for value_string in self.on_emit(self._channel):
            yield json.loads(value_string)

    def post(self, value: [dict, list]):
        if self._closed:
            raise IOError("Can't post value on already closed object.")
        self.on_publish(self._channel, json.dumps(value))

    def close(self):
        self.on_close(self._channel)
        self._closed = True


class RedisLiveData(LiveData):

    def __init__(self, channel: str, **kwargs):
        super().__init__(channel, **kwargs)
        host = kwargs.get('host')
        port = kwargs.get('port')
        self.broker = redis.StrictRedis(host, port, charset="utf-8", decode_responses=True)
        self.pubsub = self.broker.pubsub()

    def on_emit(self, channel: str):
        self.pubsub.subscribe(channel)
        for item in self.pubsub.listen():
            if item['type'] == 'message':
                yield item['data']

    def on_publish(self, channel: str, value: str):
        self.broker.publish(channel, value)

    def on_close(self, channel):
        self.pubsub.unsubscribe(channel)
        self.broker.close()

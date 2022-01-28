from pymemcache.client.base import Client

from app.fastapi_cache.backends import Backend


class MemcachedBackend(Backend):
    def __init__(self, mcache: Client):
        self.mcache = mcache

    def get(self, key: str):
        return self.mcache.get(key)

    def set(self, key: str, value: str, expire: int = None):
        return self.mcache.set(key, value, expire=expire or 0)

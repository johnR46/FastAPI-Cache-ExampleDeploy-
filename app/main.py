import logging
from fastapi import FastAPI
from pymemcache.client.base import Client

from app.fastapi_cache import FastAPICache, JsonCoder
from app.fastapi_cache.backends.memcached import MemcachedBackend
from app.fastapi_cache.key_builder import default_key_builder

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    client = Client(('pymemcached', 11211))
    FastAPICache.init(MemcachedBackend(client))
    logging.info("Application start")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutdown")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    cache_instance = FastAPICache.get_backend()
    cache_key = default_key_builder(prefix='cache_say_hello', func=say_hello, parameter={'name': name})
    cache_value = cache_instance.get(cache_key)
    print(cache_key)
    if cache_value is None:
        res = {"message": f"Hello {name}"}
        cache_instance.set(cache_key, JsonCoder.encode(res), expire=60 * 60)
        return {"value": res}
    else:
        return JsonCoder.decode(cache_value)

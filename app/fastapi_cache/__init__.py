from app.fastapi_cache.coder import Coder, JsonCoder


class FastAPICache:
    _init = False
    _backend = None

    @classmethod
    def init(
            cls,
            backend,
    ):
        if cls._init:
            return
        cls._init = True
        cls._backend = backend

    @classmethod
    def get_backend(cls):
        assert cls._backend, "You must call init first!"
        return cls._backend

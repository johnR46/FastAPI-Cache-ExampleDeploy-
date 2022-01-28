import hashlib
from typing import Optional


def default_key_builder(
        prefix: str,
        func,
        parameter: Optional[dict] = None,
):
    cache_key = (
            prefix + ':' + hashlib.md5(f"{func.__module__}:{func.__name__}:{parameter}".encode()).hexdigest()
    )

    return cache_key

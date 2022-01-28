import abc


class Backend:

    @abc.abstractmethod
    def get(self, key: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key: str, value: str, expire: int = None):
        raise NotImplementedError

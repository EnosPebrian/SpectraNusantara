from abc import ABC, abstractmethod


class RasterDriver(ABC):
    @abstractmethod
    def can_open(self, src): ...

    @abstractmethod
    def open(self, path): ...

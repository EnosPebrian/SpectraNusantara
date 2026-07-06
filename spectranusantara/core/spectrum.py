from abc import ABC, abstractmethod


class Sensor(ABC):
    @property
    @abstractmethod
    def name(self): ...

    @property
    @abstractmethod
    def wavelengths(self): ...

    @property
    @abstractmethod
    def band_names(self): ...

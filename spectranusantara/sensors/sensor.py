# spectranusantara/sensors/sensor.py

from abc import ABC
from abc import abstractmethod


class Sensor(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def wavelengths(self): ...

    @property
    @abstractmethod
    def band_names(self): ...

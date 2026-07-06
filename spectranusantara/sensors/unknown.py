# unknown.py

from .sensor import Sensor


class UnknownSensor(Sensor):
    @property
    def name(self):
        return "Unknown"

    @property
    def wavelengths(self):
        return None

    @property
    def band_names(self):
        return None

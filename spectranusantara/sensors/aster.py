# spectranusantara/sensors/aster.py

from .sensor import Sensor


class ASTERSensor(Sensor):
    @property
    def name(self):
        return "ASTER"

    @property
    def wavelengths(self):
        return [
            0.56,
            0.66,
            0.81,
            1.65,
            2.165,
            2.205,
            2.26,
            2.33,
            2.40,
        ]

    @property
    def band_names(self):

        return [
            "VNIR-1",
            "VNIR-2",
            "VNIR-3N",
            "SWIR-4",
            "SWIR-5",
            "SWIR-6",
            "SWIR-7",
            "SWIR-8",
            "SWIR-9",
        ]

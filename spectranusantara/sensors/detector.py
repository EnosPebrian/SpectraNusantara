from rasterio.io import DatasetReader

from .sensor import Sensor
from .aster import ASTERSensor
from .unknown import UnknownSensor


class SensorDetector:
    @staticmethod
    def detect(src: DatasetReader) -> Sensor:
        """
        Identify the sensor from raster metadata.
        """

        # Temporary implementation
        if src.count == 9:
            return ASTERSensor()

        return UnknownSensor()

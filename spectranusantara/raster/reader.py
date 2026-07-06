from pathlib import Path
import rasterio
from .dataset import RasterDataset
from spectranusantara.sensors.detector import SensorDetector


class RasterReader:
    @staticmethod
    def open(path: str | Path) -> RasterDataset:

        with rasterio.open(path) as src:
            cube = src.read()

        sensor = SensorDetector.detect(src)

        return RasterDataset(
            name=Path(path).stem,
            path=Path(path),
            data=cube,
            transform=src.transform,
            crs=str(src.crs),
            width=src.width,
            height=src.height,
            band_count=src.count,
            sensor=sensor,
        )

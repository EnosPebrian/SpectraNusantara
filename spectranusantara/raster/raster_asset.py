from dataclasses import dataclass

from .asset import Asset


@dataclass
class RasterAsset(Asset):
    width: int = 0

    height: int = 0

    bands: int = 0

    crs: str = ""

    transform: object = None

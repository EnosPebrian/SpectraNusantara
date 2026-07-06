from dataclasses import dataclass
from pathlib import Path
from .pixel import Pixel
from spectranusantara.sensors.sensor import Sensor
from rasterio.transform import xy

import numpy as np


@dataclass
class RasterDataset:
    """
    Represents a raster dataset loaded into memory.
    """

    name: str

    path: Path

    data: np.ndarray

    transform: object

    crs: str

    width: int

    height: int

    band_count: int

    sensor: Sensor | None = None

    def band(self, number: int):
        """
        Return a raster band using 1-based indexing.
        """

        if number < 1:
            raise ValueError("Band numbers start at 1.")

        if number > self.band_count:
            raise ValueError(f"Dataset has only {self.band_count} band(s).")

        return self.data[number - 1]

    @property
    def shape(self):

        return self.data.shape

    @property
    def dtype(self):

        return self.data.dtype

    @property
    def is_single_band(self):

        return self.band_count == 1

    @property
    def is_multiband(self):

        return self.band_count > 1

    @property
    def band_numbers(self):

        return range(1, self.band_count + 1)

    def value(self, band: int, row: int, col: int):
        return self.band(band)[row, col]

    def pixel(self, row: int, col: int) -> Pixel:

        if row < 0 or row >= self.height:
            raise ValueError(f"Row {row} outside raster.")

        if col < 0 or col >= self.width:
            raise ValueError(f"Column {col} outside raster.")

        values = self.data[:, row, col]

        x, y = xy(
            self.transform,
            row,
            col,
        )

        return Pixel(
            row=row,
            col=col,
            x=x,
            y=y,
            values=values,
        )

    @property
    def wavelengths(self):

        if self.band_count == 9:
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

        elif self.band_count == 3:
            return [
                0.56,
                0.66,
                0.81,
            ]

        elif self.band_count == 1:
            return [1]

        else:
            return list(range(1, self.band_count + 1))

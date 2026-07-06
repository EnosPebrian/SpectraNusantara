from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Pixel:
    """
    Represents one raster pixel.
    """

    row: int

    col: int

    values: np.ndarray

from dataclasses import dataclass, field
from uuid import uuid4

from spectranusantara.raster.pixel import Pixel


@dataclass
class Sample:
    """
    Represents one geological sample.
    """

    name: str

    pixel: Pixel

    id: str = field(default_factory=lambda: str(uuid4()))

    description: str = ""

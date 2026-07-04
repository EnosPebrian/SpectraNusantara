from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4


@dataclass
class Sample:
    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = "Untitled Sample"

    easting: Optional[float] = None

    northing: Optional[float] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    notes: str = ""

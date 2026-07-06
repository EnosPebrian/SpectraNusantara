"""
Base class for all assets.

Assets are immutable data imported into a project.
"""

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Asset:

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = "Unnamed Asset"

    filepath: str = ""
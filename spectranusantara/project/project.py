"""
Project model.

A Project is the top-level container for everything
loaded into SpectraNusantara.
"""

from dataclasses import dataclass, field

from spectranusantara.models.sample import Sample


@dataclass
class Project:
    name: str = "Untitled Project"

    samples: list[Sample] = field(default_factory=list)

    assets: list = field(default_factory=list)

    products: list = field(default_factory=list)

    history: list = field(default_factory=list)

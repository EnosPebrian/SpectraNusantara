"""
Project model.

A Project is the top-level container for everything
loaded into SpectraNusantara.
"""


class Project:
    def __init__(self):

        self.name = "Untitled Project"

        self.rasters = []

        self.targets = []

        self.spectral_libraries = []

        self.history = []

    def __repr__(self):

        return (
            f"<Project '{self.name}' | "
            f"{len(self.rasters)} rasters | "
            f"{len(self.targets)} targets>"
        )

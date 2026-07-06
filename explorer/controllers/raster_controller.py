from PySide6.QtWidgets import QFileDialog
from spectranusantara.raster.reader import RasterReader


class RasterController:
    def __init__(self, window, project):

        self.window = window

        self.project = project

    def open_raster(self):

        filename, _ = QFileDialog.getOpenFileName(
            self.window, "Open Raster", "", "GeoTIFF (*.tif *.tiff)"
        )

        if not filename:
            return

        dataset = RasterReader.open(filename)

        self.project.rasters.append(dataset)

        self.window.canvas.display(
            dataset,
            dataset.band(1),
        )

        self.window.statusBar().showMessage(f"{dataset.name} loaded")

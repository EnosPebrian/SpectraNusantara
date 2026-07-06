from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from explorer.gui.spectrum_canvas import SpectrumCanvas


class SpectrumPanel(QWidget):
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.info = QLabel("Click a pixel")

        self.canvas = SpectrumCanvas()

        layout.addWidget(self.info)

        layout.addWidget(self.canvas)

    def display_sample(self, dataset, pixel):

        self.dataset_label.setText(dataset.name)

        self.sensor_label.setText(dataset.sensor.name if dataset.sensor else "Unknown")

        self.band_label.setText(str(dataset.band_count))

        self.row_label.setText(str(pixel.row))

        self.col_label.setText(str(pixel.col))

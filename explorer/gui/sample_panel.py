from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from explorer.gui.sample_header import SampleHeader
from explorer.gui.spectrum_canvas import SpectrumCanvas


class SamplePanel(QWidget):
    def __init__(self):

        super().__init__()

        self.header = SampleHeader()

        self.spectrum = SpectrumCanvas()

        layout = QVBoxLayout(self)

        layout.addWidget(self.header)
        layout.addWidget(self.spectrum)

    def display(self, dataset, pixel):

        self.header.display(dataset, pixel)

        self.spectrum.display(
            dataset,
            pixel,
        )

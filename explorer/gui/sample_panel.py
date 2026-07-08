from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtCore import Signal
from explorer.gui.sample_header import SampleHeader
from explorer.gui.spectrum_canvas import SpectrumCanvas


class SamplePanel(QWidget):
    markRequested = Signal()

    def __init__(self):

        super().__init__()

        self.header = SampleHeader()

        self.spectrum = SpectrumCanvas()

        self.mark_button = QPushButton("📍 Mark")

        self.mark_button.setEnabled(False)

        self.mark_button.clicked.connect(self.markRequested.emit)

        layout = QVBoxLayout(self)
        layout.addWidget(self.header)
        layout.addWidget(self.spectrum)
        layout.addWidget(self.mark_button)

    def display(self, dataset, pixel):

        self.header.display(dataset, pixel)

        self.spectrum.display(
            dataset,
            pixel,
        )
        self.mark_button.setEnabled(True)

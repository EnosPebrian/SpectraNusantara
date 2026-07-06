from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
)

from spectranusantara.sample import sample
from spectranusantara.sample.sample import Sample


class SampleManager(QWidget):
    def __init__(self):

        super().__init__()

        self.list = QListWidget()

        layout = QVBoxLayout(self)

        layout.addWidget(self.list)

    def add_sample(self, sample: Sample):

        self.list.addItem(sample.name)

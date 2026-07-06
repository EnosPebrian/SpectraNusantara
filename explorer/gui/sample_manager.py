from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
)


class SampleManager(QWidget):
    def __init__(self):

        super().__init__()

        self.list = QListWidget()

        layout = QVBoxLayout(self)

        layout.addWidget(self.list)

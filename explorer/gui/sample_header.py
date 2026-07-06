from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class SampleHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("No sample selected")

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addStretch()

    def display(self, dataset, pixel):

        text = f"{dataset.sensor.name}   |   Row: {pixel.row}   Col: {pixel.col}"

        self.label.setText(text)

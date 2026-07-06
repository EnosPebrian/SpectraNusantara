from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class SampleHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.dataset_label = QLabel()

        self.location_label = QLabel()

        top = QHBoxLayout()
        top.addWidget(self.dataset_label)
        top.addStretch()

        bottom = QHBoxLayout()
        bottom.addWidget(self.location_label)
        bottom.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(top)
        layout.addLayout(bottom)

    def display(self, dataset, pixel):

        self.dataset_label.setText(
            f"Dataset: {dataset.name}    Sensor: {dataset.sensor.name}"
        )

        self.location_label.setText(f"X: {pixel.x:,.2f}    Y: {pixel.y:,.2f}")

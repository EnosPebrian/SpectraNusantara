import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("SpectraNusantara")

        self.resize(1600, 900)

        self.statusBar().showMessage("Ready")

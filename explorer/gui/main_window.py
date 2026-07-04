from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("SpectraNusantara")

        self.resize(1600, 900)

        self.statusBar().showMessage("Ready")

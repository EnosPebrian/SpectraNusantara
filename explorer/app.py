from PySide6.QtWidgets import QApplication

from explorer.gui.main_window import MainWindow


class Application:
    def __init__(self):

        self.app = QApplication([])

        self.window = MainWindow()

    def run(self):

        self.window.show()

        self.app.exec()

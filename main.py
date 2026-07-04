import sys

from PySide6.QtWidgets import QApplication
from explorer.app import MainWindow

app = QApplication(sys.argv)

window = MainWindow()

window.show()

sys.exit(app.exec())

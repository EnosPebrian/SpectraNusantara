from PySide6.QtWidgets import (
    QToolBar,
)
from PySide6.QtGui import QAction


class ToolBar(QToolBar):
    def __init__(self):

        super().__init__("Tools")

        self.action_save_sample = QAction(
            "Save Sample",
            self,
        )

        self.addAction(self.action_save_sample)

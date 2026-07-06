from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        file_menu = self.addMenu("&File")

        self.action_new = file_menu.addAction("New Project")

        self.action_open_project = file_menu.addAction("Open Project")

        file_menu.addSeparator()

        self.action_open_raster = file_menu.addAction("Open Raster...")

        file_menu.addSeparator()

        self.action_exit = file_menu.addAction("Exit")

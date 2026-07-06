from PySide6.QtWidgets import QMainWindow
from explorer.gui.map_canvas import MapCanvas
from spectranusantara.project import Project
from explorer.gui.menu_bar import MenuBar
from explorer.controllers.raster_controller import RasterController
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
from explorer.gui.sample_panel import SamplePanel
from explorer.gui.sample_manager import SampleManager
from explorer.gui.tool_bar import ToolBar


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("SpectraNusantara")

        self.resize(1600, 900)

        self.statusBar().showMessage("Ready")

        self.canvas = MapCanvas()

        self.setCentralWidget(self.canvas)

        self.menu = MenuBar(self)

        self.setMenuBar(self.menu)

        self.toolbar = ToolBar()

        self.addToolBar(self.toolbar)

        self.project = Project()

        self.raster_controller = RasterController(self, self.project)

        self.menu.action_open_raster.triggered.connect(
            self.raster_controller.open_raster
        )

        self.canvas.mouseMoved.connect(self.on_mouse_move)

        self.sample_panel = SamplePanel()

        self.sample_manager = SampleManager()

        dock = QDockWidget("Sample")

        dock.setWidget(self.sample_panel)

        self.addDockWidget(Qt.BottomDockWidgetArea, dock)

        sample_dock = QDockWidget("Samples")

        sample_dock.setWidget(self.sample_manager)

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            sample_dock,
        )

        self.canvas.pixelSelected.connect(
            lambda pixel: self.sample_panel.display(
                self.canvas.dataset,
                pixel,
            )
        )

        self.canvas.pixelSelected.connect(self.sample_manager.add_sample)

    def on_mouse_move(self, row, col):

        self.statusBar().showMessage(f"Row: {row}   Col: {col}")

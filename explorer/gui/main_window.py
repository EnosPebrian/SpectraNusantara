from PySide6.QtWidgets import QMainWindow
from explorer.gui.map_canvas import MapCanvas
from spectranusantara.project import Project
from explorer.gui.menu_bar import MenuBar
from explorer.controllers.raster_controller import RasterController
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
from explorer.gui.sample_panel import SamplePanel
from explorer.gui.project_explorer import ProjectExplorer
from explorer.gui.tool_bar import ToolBar
from spectranusantara.sample import sample
from spectranusantara.sample.sample import Sample


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

        self.current_pixel = None

        self.raster_controller = RasterController(self, self.project)

        self.menu.action_open_raster.triggered.connect(
            self.raster_controller.open_raster
        )

        self.canvas.mouseMoved.connect(self.on_mouse_move)

        self.sample_panel = SamplePanel()

        self.project_explorer = ProjectExplorer()

        dock = QDockWidget("Sample")

        dock.setWidget(self.sample_panel)

        self.addDockWidget(Qt.BottomDockWidgetArea, dock)

        sample_dock = QDockWidget("Samples")

        sample_dock.setWidget(self.project_explorer)

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            sample_dock,
        )

        self.canvas.pixelSelected.connect(self.on_pixel_selected)

        self.sample_panel.markRequested.connect(self.mark_current_sample)

        self.project_explorer.sampleActivated.connect(self.on_sample_activated)

    def on_mouse_move(self, row, col):

        self.statusBar().showMessage(f"Row: {row}   Col: {col}")

    def on_pixel_selected(self, pixel):

        self.current_pixel = pixel

        self.sample_panel.display(
            self.canvas.dataset,
            pixel,
        )

    def mark_current_sample(self):

        if self.current_pixel is None:
            return

        marked_sample = Sample(
            name=f"Sample {self.project_explorer.sample_count() + 1}",
            pixel=self.current_pixel,
        )

        self.project_explorer.add_sample(marked_sample)

    def on_sample_activated(self, sample):

        self.current_pixel = sample.pixel

        self.sample_panel.display(
            self.canvas.dataset,
            sample.pixel,
        )

        self.canvas.show_selection(
            sample.pixel.row,
            sample.pixel.col,
        )

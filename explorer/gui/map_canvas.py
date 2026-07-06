from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtCore import Signal


class MapCanvas(FigureCanvasQTAgg):
    """
    Widget for displaying raster images.
    """

    mouseMoved = Signal(int, int)

    pixelSelected = Signal(object)

    def __init__(self):

        self.figure = Figure()

        super().__init__(self.figure)

        self.ax = self.figure.add_subplot(111)

        self.dataset = None

        self.mpl_connect("motion_notify_event", self.on_mouse_move)

        self.mpl_connect("button_press_event", self.on_mouse_click)

        self.ax.set_axis_off()

        self.setMouseTracking(True)

        self.marker = None

    def show_band(self, band):

        self.ax.clear()

        self.ax.imshow(band, cmap="gray")

        self.ax.set_axis_off()

        self.draw()

    def display(self, dataset, image):

        self.dataset = dataset

        self.ax.clear()

        self.ax.imshow(image, cmap="gray")

        self.ax.set_axis_off()

        self.draw()

    def on_mouse_move(self, event):

        if event.inaxes != self.ax:
            return

        if event.xdata is None or event.ydata is None:
            return

        col = int(round(event.xdata))
        row = int(round(event.ydata))

        if row < 0:
            self.statusBar().clearMessage()

            return

        self.mouseMoved.emit(row, col)

    def on_mouse_click(self, event):

        if event.inaxes != self.ax:
            return

        if event.xdata is None or event.ydata is None:
            return

        if self.dataset is None:
            return

        row = int(round(event.ydata))
        col = int(round(event.xdata))

        pixel = self.dataset.pixel(row, col)

        if self.marker is not None:
            self.marker.remove()

        self.marker = self.ax.scatter(
            col,
            row,
            marker="+",
            s=150,
            c="red",
        )

        self.draw_idle()

        self.pixelSelected.emit(pixel)

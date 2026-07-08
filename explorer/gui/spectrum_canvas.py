from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class SpectrumCanvas(FigureCanvasQTAgg):
    def __init__(self):

        self.figure = Figure()

        super().__init__(self.figure)

        self.ax = self.figure.add_subplot(111)

        self.ax.set_xlabel("Band")

        self.ax.set_ylabel("Value")

    def display(
        self,
        dataset,
        pixel,
        append=False,
    ):
        if not append:
            self.ax.clear()

        self.ax.plot(
            dataset.wavelengths,
            pixel.values,
            marker="o",
        )

        if dataset.sensor.wavelengths is None:
            x = range(1, dataset.band_count + 1)

            xlabel = "Band"

        else:
            x = dataset.sensor.wavelengths

            xlabel = "Wavelength (µm)"

        self.ax.set_xlabel(xlabel)

        self.ax.set_ylabel("DN")

        self.ax.grid(True)

        self.draw()

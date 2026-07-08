from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeWidget,
)
from PySide6.QtWidgets import QTreeWidgetItem
from spectranusantara.sample import sample
from spectranusantara.sample.sample import Sample


class ProjectExplorer(QWidget):
    def __init__(self):

        super().__init__()

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)

        self.rasters_item = QTreeWidgetItem(["Rasters"])

        self.samples_item = QTreeWidgetItem(["Samples"])

        self.tree.addTopLevelItem(self.rasters_item)

        self.tree.addTopLevelItem(self.samples_item)

        layout = QVBoxLayout(self)

        layout.addWidget(self.tree)

    def add_sample(self, sample: Sample):

        item = QTreeWidgetItem([sample.name])

        self.samples_item.addChild(item)

        self.samples_item.setExpanded(True)

    def sample_count(self) -> int:
        return self.samples_item.childCount()

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea
from PySide6.QtCore import Qt

from src.components.preview_grid import PreviewGrid


class PreviewView(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("sidePanel")

        layout = QVBoxLayout()

        self.title = QLabel("Selected feature")
        self.title.setAlignment(Qt.AlignCenter)

        self.grid = PreviewGrid()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.grid)

        layout.addWidget(self.title)
        layout.addWidget(scroll)

        self.setLayout(layout)
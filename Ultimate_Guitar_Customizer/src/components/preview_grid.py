from PySide6.QtWidgets import QWidget, QGridLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
import os


class PreviewGrid(QWidget):
    item_clicked = Signal(str)  # nom du fichier cliqué

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

        self.items = []

        self.selected_label = None

    def clear(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def load_images(self, folder_path):
        self.clear()

        self.selected_label = None

        files = [f for f in os.listdir(folder_path)
                 if f.endswith((".png", ".svg"))]

        col_count = max(2, self.width() // 120)

        row = 0
        col = 0

        for file in files:
            path = os.path.join(folder_path, file)

            label = QLabel()
            label.file_name = file

            pixmap = QPixmap(path)

            label.setPixmap(pixmap.scaled(
                100, 100,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))

            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: 1px solid #4a5568; padding: 5px;")

            # click
            def on_click(event, lbl=label):
                # reset ancien sélectionné
                if self.selected_label:
                    self.selected_label.setStyleSheet(
                        "border: 1px solid #4a5568; padding: 5px;"
                    )

                # nouveau sélectionné
                lbl.setStyleSheet(
                    "border: 2px solid #2980b9; padding: 5px;"
                )

                self.selected_label = lbl

                # envoie au controller
                self.item_clicked.emit(lbl.file_name)

            label.mousePressEvent = on_click

            self.layout.addWidget(label, row, col)

            col += 1
            if col >= col_count:
                col = 0
                row += 1

    def resizeEvent(self, event):
        # reload pour recalculer colonnes
        super().resizeEvent(event)

    def select_item(self, value):
        """Sélectionne visuellement un item à partir de son nom"""

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()

            if hasattr(widget, "file_name"):
                name = widget.file_name.split(".")[0]

                if name == value:
                    # reset ancien
                    if self.selected_label:
                        self.selected_label.setStyleSheet(
                            "border: 1px solid #4a5568; padding: 5px;"
                        )

                    # nouveau
                    widget.setStyleSheet(
                        "border: 2px solid #2980b9; padding: 5px;"
                    )

                    self.selected_label = widget
                    break
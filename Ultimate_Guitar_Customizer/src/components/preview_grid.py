from pathlib import Path

from PySide6.QtWidgets import QWidget, QGridLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from src.paths import slugify

STYLE_NORMAL = "border: 1px solid #4a5568; padding: 5px;"
STYLE_SELECTED = "border: 2px solid #2980b9; padding: 5px;"


class PreviewGrid(QWidget):
    item_clicked = Signal(str)  # nom du fichier cliqué

    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()   # ne pas appeler "layout" : ça écrase QWidget.layout()
        self.grid_layout.setSpacing(10)
        self.setLayout(self.grid_layout)

        self.selected_label = None

    def clear(self):
        self.selected_label = None
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def load_images(self, folder_path):
        self.clear()

        folder = Path(folder_path)
        if not folder.is_dir():
            return

        files = sorted(f for f in folder.iterdir()
                       if f.suffix.lower() in (".png", ".svg"))

        col_count = max(2, self.width() // 120)

        for index, file in enumerate(files):
            label = QLabel()
            label.file_name = file.name

            pixmap = QPixmap(str(file))
            label.setPixmap(pixmap.scaled(
                100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(STYLE_NORMAL)
            label.setToolTip(file.stem)
            label.mousePressEvent = lambda event, lbl=label: self._on_click(lbl)

            self.grid_layout.addWidget(label, index // col_count, index % col_count)

    def _set_selected(self, label):
        if self.selected_label:
            self.selected_label.setStyleSheet(STYLE_NORMAL)
        label.setStyleSheet(STYLE_SELECTED)
        self.selected_label = label

    def _on_click(self, label):
        self._set_selected(label)
        self.item_clicked.emit(label.file_name)

    def select_item(self, value):
        """Sélectionne visuellement un item à partir de son nom."""
        target = slugify(value)
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if widget and slugify(Path(widget.file_name).stem) == target:
                self._set_selected(widget)
                break
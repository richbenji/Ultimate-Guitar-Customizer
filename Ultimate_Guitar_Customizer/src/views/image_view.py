from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from src.paths import ASSETS


class ImageView(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: black; border: 1px solid #444;")

        # Ignored + minimumSize : évite que le label refuse de rétrécir
        # à cause de la taille du pixmap
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setMinimumSize(200, 200)

        self.original_pixmap = QPixmap(str(ASSETS / "body_shape" / "Kiesel-CT6-1.png"))
        self.update_pixmap()

    def set_image(self, path):
        self.original_pixmap = QPixmap(str(path))
        self.update_pixmap()

    def update_pixmap(self):
        if self.original_pixmap.isNull():
            return
        self.setPixmap(self.original_pixmap.scaled(
            self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_pixmap()
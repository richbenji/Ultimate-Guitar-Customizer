from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ImageView(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        # 👉 FOND NOIR
        self.setStyleSheet("""
            background-color: black;
            border: 1px solid #444;
        """)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 👉 stocker l'image originale
        self.original_pixmap = QPixmap("assets/body_shape/Kiesel-CT6-1.png")

        self.update_pixmap()

    def update_pixmap(self):
        if not self.original_pixmap.isNull():
            scaled = self.original_pixmap.scaled(
                self.size() if self.size().width() > 0 else Qt.QSize(800, 600),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.setPixmap(scaled)

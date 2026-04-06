from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter, QLabel, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase

from .tabs_view import TabsView
from .preview_view import PreviewView
from .image_view import ImageView


class MainView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # ===== TOP BAR =====
        header = self.create_header()
        layout.addLayout(header)

        # ===== SPLITTER PRINCIPAL (GAUCHE / DROITE) =====
        main_splitter = QSplitter(Qt.Horizontal)

        # ===== PARTIE GAUCHE =====
        left_widget = QWidget()
        left_layout = QVBoxLayout()

        # Split vertical (image en haut, tabs en bas)
        left_splitter = QSplitter(Qt.Vertical)

        self.image_view = ImageView()
        self.tabs = TabsView()

        left_splitter.addWidget(self.image_view)
        left_splitter.addWidget(self.tabs)

        # proportions verticales
        left_splitter.setStretchFactor(0, 3)  # image
        left_splitter.setStretchFactor(1, 1)  # tabs

        left_splitter.setChildrenCollapsible(False)

        left_layout.addWidget(left_splitter)
        left_widget.setLayout(left_layout)

        # ===== PARTIE DROITE (PREVIEW) =====
        self.preview_view = PreviewView()
        self.preview_view.setMinimumWidth(250)  # évite qu'il disparaisse

        # ===== ASSEMBLAGE =====
        main_splitter.addWidget(left_widget)
        main_splitter.addWidget(self.preview_view)

        # proportions horizontales
        main_splitter.setStretchFactor(0, 3)
        main_splitter.setStretchFactor(1, 1)

        main_splitter.setChildrenCollapsible(False)

        # ===== AJOUT FINAL =====
        layout.addWidget(main_splitter, stretch=1)

        self.setLayout(layout)

    def create_header(self):
        main_layout = QVBoxLayout()

        # ===== LIGNE 1 : TITRE =====
        title_layout = QHBoxLayout()
        title = QLabel("🎸 Ultimate Guitar Customizer")
        font_id = QFontDatabase.addApplicationFont("fonts/MetalMania-Regular.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            title.setStyleSheet(f"font-family: '{font_family}'; font-size: 26px;")
        else:
            title.setStyleSheet("font-size: 26px; font-weight: bold;")

        title_layout.addStretch()
        title_layout.addWidget(title)
        title_layout.addStretch()

        # ===== LIGNE 2 : BOUTONS =====
        buttons_layout = QHBoxLayout()

        self.btn_dark = QPushButton("🌙 Dark")
        self.btn_reset = QPushButton("Reset")
        self.btn_front = QPushButton("Front")
        self.btn_rear = QPushButton("Rear")
        self.btn_load = QPushButton("📂 Charger")
        self.btn_save = QPushButton("💾 Sauvegarder")
        self.btn_export = QPushButton("📤 Exporter PDF")

        # 👉 ordre demandé
        buttons_layout.addWidget(self.btn_dark)
        buttons_layout.addWidget(self.btn_reset)
        buttons_layout.addWidget(self.btn_front)
        buttons_layout.addWidget(self.btn_rear)
        buttons_layout.addWidget(self.btn_load)
        buttons_layout.addWidget(self.btn_save)
        buttons_layout.addWidget(self.btn_export)

        buttons_layout.addStretch()

        # ===== ASSEMBLAGE =====
        main_layout.addLayout(title_layout)
        main_layout.addLayout(buttons_layout)

        return main_layout

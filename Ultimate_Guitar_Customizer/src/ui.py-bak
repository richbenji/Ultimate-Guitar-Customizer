import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QTabWidget, QScrollArea,
    QSizePolicy, QFrame, QCheckBox, QSpacerItem
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QColor, QPalette

# ── Palette de couleurs ──────────────────────────────────────────────────────
DARK_BG        = "#1a2535"
HEADER_BG      = "#0f1d2e"
CENTER_BG      = "#000000"
PANEL_BG       = "#2d3748"
TABS_BG        = "#252f3e"
BTN_BLUE       = "#2980b9"
BTN_HOVER      = "#3498db"
BTN_ACTIVE     = "#1a6fa0"
COMBO_BG       = "#2d3748"
COMBO_BORDER   = "#4a5568"
TEXT_COLOR     = "#ffffff"
TITLE_COLOR    = "#63b3ed"
TAB_SEL        = "#2980b9"
TAB_UNSEL      = "#2d3748"
TAB_TEXT_UNSEL = "#aab4c4"

QSS = f"""
/* ── Fenêtre principale ── */
QMainWindow, QWidget {{
    background-color: {DARK_BG};
    color: {TEXT_COLOR};
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}}

/* ── Barre d'outils ── */
#toolbarWidget {{
    background-color: {DARK_BG};
    border-bottom: 1px solid #2d3748;
}}

/* ── Header ── */
#headerWidget {{
    background-color: {HEADER_BG};
    border-bottom: 2px solid {BTN_BLUE};
}}

#titleLabel {{
    color: {TITLE_COLOR};
    font-size: 26px;
    font-weight: bold;
    font-family: 'Georgia', serif;
    letter-spacing: 2px;
}}

/* ── Zone image guitare ── */
#guitarFrame {{
    background-color: {CENTER_BG};
    border: 2px solid #2d3748;
    border-radius: 6px;
}}

#guitarImageLabel {{
    background-color: {CENTER_BG};
}}

/* ── Panneau latéral droit ── */
#sidePanel {{
    background-color: {PANEL_BG};
    border-left: 1px solid #3d4f63;
    border-radius: 0px 6px 6px 0px;
    min-width: 180px;
    max-width: 240px;
}}

#sidePanelTitle {{
    color: {TEXT_COLOR};
    font-size: 14px;
    font-weight: bold;
    padding: 8px;
    border-bottom: 1px solid #3d4f63;
}}

#sidePanelImage {{
    background-color: #1e2a3a;
    border-radius: 4px;
    min-height: 120px;
}}

/* ── Boutons bleus ── */
#blueBtn {{
    background-color: {BTN_BLUE};
    color: {TEXT_COLOR};
    border: none;
    border-radius: 5px;
    padding: 6px 14px;
    font-weight: bold;
    font-size: 13px;
    min-width: 90px;
}}
#blueBtn:hover {{
    background-color: {BTN_HOVER};
}}
#blueBtn:pressed {{
    background-color: {BTN_ACTIVE};
}}

/* ── Bouton Reset ── */
#resetBtn {{
    background-color: {BTN_BLUE};
    color: {TEXT_COLOR};
    border: none;
    border-radius: 5px;
    padding: 6px 16px;
    font-weight: bold;
    font-size: 13px;
    min-width: 70px;
}}
#resetBtn:hover {{
    background-color: {BTN_HOVER};
}}

/* ── ComboBox ── */
QComboBox {{
    background-color: {COMBO_BG};
    color: {TEXT_COLOR};
    border: 1px solid {COMBO_BORDER};
    border-radius: 4px;
    padding: 4px 8px;
    min-width: 130px;
    min-height: 28px;
}}
QComboBox:hover {{
    border-color: {BTN_BLUE};
}}
QComboBox::drop-down {{
    border: none;
    width: 20px;
}}
QComboBox::down-arrow {{
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid {TEXT_COLOR};
    margin-right: 6px;
}}
QComboBox QAbstractItemView {{
    background-color: {COMBO_BG};
    color: {TEXT_COLOR};
    selection-background-color: {BTN_BLUE};
    border: 1px solid {COMBO_BORDER};
}}

/* ── Onglets ── */
QTabWidget::pane {{
    background-color: {TABS_BG};
    border: none;
    border-top: 2px solid {BTN_BLUE};
}}
QTabBar::tab {{
    background-color: {TAB_UNSEL};
    color: {TAB_TEXT_UNSEL};
    padding: 7px 18px;
    margin-right: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    font-size: 13px;
}}
QTabBar::tab:selected {{
    background-color: {TAB_SEL};
    color: {TEXT_COLOR};
    font-weight: bold;
}}
QTabBar::tab:hover:!selected {{
    background-color: #3d4f63;
    color: {TEXT_COLOR};
}}

/* ── Toggle Dark Mode ── */
QCheckBox {{
    color: {TEXT_COLOR};
    font-size: 12px;
    spacing: 6px;
}}
QCheckBox::indicator {{
    width: 36px;
    height: 18px;
    border-radius: 9px;
    background-color: #4a5568;
    border: 1px solid #606878;
}}
QCheckBox::indicator:checked {{
    background-color: {BTN_BLUE};
}}

/* ── ScrollArea ── */
QScrollArea {{
    border: none;
    background-color: transparent;
}}
QScrollBar:vertical {{
    background-color: {PANEL_BG};
    width: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical {{
    background-color: {BTN_BLUE};
    border-radius: 4px;
    min-height: 20px;
}}
"""


def make_blue_btn(text, object_name="blueBtn"):
    btn = QPushButton(text)
    btn.setObjectName(object_name)
    return btn


def make_combo(items=None):
    combo = QComboBox()
    if items:
        combo.addItems(items)
    else:
        combo.addItem("...")
    return combo


def make_row(*widgets):
    """Crée une ligne horizontale de widgets avec espacement."""
    row = QHBoxLayout()
    row.setSpacing(8)
    for w in widgets:
        if isinstance(w, QSpacerItem):
            row.addSpacerItem(w)
        else:
            row.addWidget(w)
    return row


# ── Contenu des onglets ──────────────────────────────────────────────────────

def tab_general():
    w = QWidget()
    w.setObjectName("tabContent")
    layout = QVBoxLayout(w)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(10)

    row1 = make_row(
        make_blue_btn("Modèle"),   make_combo(["Standard", "Custom", "Signature"]),
        make_blue_btn("Marque"),   make_combo(["PRS", "Gibson", "Fender", "Ibanez"]),
        make_blue_btn("Dexterity"), make_combo(["Right", "Left"]),
    )
    row2 = make_row(
        make_blue_btn("Strings"),      make_combo(["6", "7", "8"]),
        make_blue_btn("Scale length"), make_combo(['25"', '24.75"', '25.5"']),
        make_blue_btn("Build"),        make_combo(["Bolt-on", "Set-in", "Neck-through"]),
    )

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addStretch()
    return w


def tab_body():
    w = QWidget()
    layout = QVBoxLayout(w)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(10)

    row1 = make_row(
        make_blue_btn("Body wood"),   make_combo(["Mahogany", "Alder", "Ash", "Black limba"]),
        make_blue_btn("Top wood"),    make_combo(["Maple", "Plain maple", "Quilted maple", "None"]),
        make_blue_btn("Top shape"),   make_combo(["Carved", "Flat", "Arched"]),
    )
    row2 = make_row(
        make_blue_btn("Colors"),      make_combo(["Natural", "Sunburst", "Black", "Blue"]),
        make_blue_btn("Body finish"), make_combo(["Gloss", "Satin", "Matte"]),
    )

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addStretch()
    return w


def tab_neck():
    w = QWidget()
    layout = QVBoxLayout(w)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(10)

    row1 = make_row(
        make_blue_btn("Neck wood"),    make_combo(["Maple", "Mahogany", "Rosewood"]),
        make_blue_btn("Fretboard"),    make_combo(["Rosewood", "Ebony", "Maple"]),
        make_blue_btn("Neck profile"), make_combo(["C", "D", "U", "V"]),
    )
    row2 = make_row(
        make_blue_btn("Frets"),        make_combo(["22", "24"]),
        make_blue_btn("Nut width"),    make_combo(['1 11/16"', '1 3/4"', '1 7/8"']),
        make_blue_btn("Inlays"),       make_combo(["Dots", "Birds", "Abalone", "None"]),
    )

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addStretch()
    return w


def tab_electronics():
    w = QWidget()
    layout = QVBoxLayout(w)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(10)

    row1 = make_row(
        make_blue_btn("Bridge PU"),   make_combo(["Humbucker", "Single coil", "P90"]),
        make_blue_btn("Neck PU"),     make_combo(["Humbucker", "Single coil", "P90"]),
        make_blue_btn("Config"),      make_combo(["HH", "HSS", "SSS", "HS"]),
    )
    row2 = make_row(
        make_blue_btn("Controls"),    make_combo(["1V 1T", "1V 2T", "2V 2T"]),
        make_blue_btn("Pickup brand"), make_combo(["PRS", "Seymour Duncan", "DiMarzio"]),
    )

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addStretch()
    return w


def tab_hardware():
    w = QWidget()
    layout = QVBoxLayout(w)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(10)

    row1 = make_row(
        make_blue_btn("Bridge"),     make_combo(["Tune-o-matic", "Floyd Rose", "Hardtail"]),
        make_blue_btn("Tuners"),     make_combo(["Grover", "Kluson", "Locking"]),
        make_blue_btn("Color"),      make_combo(["Gold", "Chrome", "Black"]),
    )
    row2 = make_row(
        make_blue_btn("Nut"),        make_combo(["Bone", "Tusq", "Locking"]),
        make_blue_btn("Strap pins"), make_combo(["Standard", "Schaller"]),
    )

    layout.addLayout(row1)
    layout.addLayout(row2)
    layout.addStretch()
    return w


def tab_export():
    w = QWidget()
    layout = QVBoxLayout(w)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(10)

    row1 = make_row(
        make_blue_btn("💾  Sauvegarder"),
        make_blue_btn("📂  Charger"),
        make_blue_btn("📤  Exporter PDF"),
    )

    layout.addLayout(row1)
    layout.addStretch()
    return w


# ── Fenêtre principale ───────────────────────────────────────────────────────

class GuitarCustomizer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultimate Guitar Customizer")
        self.resize(1300, 700)
        self.setMinimumSize(900, 550)

        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)

        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._build_header())
        root.addWidget(self._build_toolbar())
        root.addWidget(self._build_center(), stretch=1)
        root.addWidget(self._build_bottom())

    # ── Header (titre) ──────────────────────────────────────────────────────

    def _build_header(self):
        header = QWidget()
        header.setObjectName("headerWidget")
        header.setFixedHeight(46)

        lay = QHBoxLayout(header)
        lay.setContentsMargins(12, 0, 12, 0)
        lay.setSpacing(0)

        title = QLabel("Ultimate Guitar Customizer")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        lay.addWidget(title, stretch=1)

        return header

    # ── Barre d'outils (sous le titre) ──────────────────────────────────────

    def _build_toolbar(self):
        toolbar = QWidget()
        toolbar.setObjectName("toolbarWidget")
        toolbar.setFixedHeight(46)

        lay = QHBoxLayout(toolbar)
        lay.setContentsMargins(12, 6, 12, 6)
        lay.setSpacing(8)

        # Gauche : Reset
        self.resetBtn = make_blue_btn("Reset", "resetBtn")
        lay.addWidget(self.resetBtn)

        # Séparateur visuel
        sep = QFrame()
        sep.setFrameShape(QFrame.VLine)
        sep.setStyleSheet("color: #3d4f63;")
        lay.addWidget(sep)

        # Sauvegarde / Chargement / Export
        lay.addWidget(make_blue_btn("💾  Sauvegarder"))
        lay.addWidget(make_blue_btn("📂  Charger"))
        lay.addWidget(make_blue_btn("📤  Exporter PDF"))

        # Espace central
        lay.addStretch()

        # Droite : Front / Rear
        lay.addWidget(make_blue_btn("Front"))
        lay.addWidget(make_blue_btn("Rear"))

        # Séparateur visuel
        sep2 = QFrame()
        sep2.setFrameShape(QFrame.VLine)
        sep2.setStyleSheet("color: #3d4f63;")
        lay.addWidget(sep2)

        # Dark mode toggle
        self.darkToggle = QCheckBox("Dark Mode")
        self.darkToggle.setChecked(True)
        lay.addWidget(self.darkToggle)

        return toolbar

    # ── Zone centrale : image + panneau latéral ──────────────────────────────

    def _build_center(self):
        container = QWidget()
        lay = QHBoxLayout(container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        # Cadre image guitare
        guitar_frame = QFrame()
        guitar_frame.setObjectName("guitarFrame")
        guitar_lay = QVBoxLayout(guitar_frame)
        guitar_lay.setContentsMargins(0, 0, 0, 0)

        # Label image
        self.guitarImageLabel = QLabel()
        self.guitarImageLabel.setObjectName("guitarImageLabel")
        self.guitarImageLabel.setAlignment(Qt.AlignCenter)
        self.guitarImageLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.guitarImageLabel.setText("[ Image de la guitare ]")
        self.guitarImageLabel.setStyleSheet("color: #4a5568; font-size: 16px;")
        guitar_lay.addWidget(self.guitarImageLabel, stretch=1)

        lay.addWidget(guitar_frame, stretch=1)

        # Panneau latéral droit
        side = QWidget()
        side.setObjectName("sidePanel")
        side_lay = QVBoxLayout(side)
        side_lay.setContentsMargins(8, 8, 8, 8)
        side_lay.setSpacing(8)

        self.sidePanelTitle = QLabel("Top wood")
        self.sidePanelTitle.setObjectName("sidePanelTitle")
        self.sidePanelTitle.setAlignment(Qt.AlignCenter)
        side_lay.addWidget(self.sidePanelTitle)

        self.sidePanelImage = QLabel()
        self.sidePanelImage.setObjectName("sidePanelImage")
        self.sidePanelImage.setAlignment(Qt.AlignCenter)
        self.sidePanelImage.setText("Illustration")
        self.sidePanelImage.setStyleSheet("color: #4a5568; font-size: 13px; padding: 20px;")
        self.sidePanelImage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        side_lay.addWidget(self.sidePanelImage, stretch=1)

        lay.addWidget(side)

        return container

    # ── Panneau du bas : onglets ─────────────────────────────────────────────

    def _build_bottom(self):
        self.tabs = QTabWidget()
        self.tabs.setObjectName("controlTabs")
        self.tabs.setFixedHeight(175)

        self.tabs.addTab(tab_general(),     "General")
        self.tabs.addTab(tab_body(),        "Body")
        self.tabs.addTab(tab_neck(),        "Neck")
        self.tabs.addTab(tab_electronics(), "Electronics")
        self.tabs.addTab(tab_hardware(),    "Hardware")

        return self.tabs

    # ── Chargement d'image guitare ───────────────────────────────────────────

    def set_guitar_image(self, path: str):
        """Charge une image et l'affiche dans la zone centrale."""
        pix = QPixmap(path)
        if not pix.isNull():
            pix = pix.scaled(
                self.guitarImageLabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.guitarImageLabel.setPixmap(pix)
            self.guitarImageLabel.setText("")

    # ── Mise à jour du panneau latéral ───────────────────────────────────────

    def update_side_panel(self, title: str, image_path: str = None):
        """Met à jour le titre et l'image du panneau latéral."""
        self.sidePanelTitle.setText(title)
        if image_path:
            pix = QPixmap(image_path)
            if not pix.isNull():
                pix = pix.scaled(
                    self.sidePanelImage.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.sidePanelImage.setPixmap(pix)
        else:
            self.sidePanelImage.setText("Illustration")


# ── Point d'entrée ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)

    window = GuitarCustomizer()
    window.show()

    # Exemple : charger une image de guitare
    # window.set_guitar_image("ma_guitare.png")

    sys.exit(app.exec())

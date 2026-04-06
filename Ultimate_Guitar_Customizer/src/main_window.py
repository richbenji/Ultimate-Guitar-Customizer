from PySide6.QtWidgets import QMainWindow
from src.views.main_view import MainView
from src.controllers.main_controller import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ultimate Guitar Customizer")

        self.view = MainView()
        self.setCentralWidget(self.view)

        self.controller = MainController(self.view)

        self.setStyleSheet("""
        /* ===================================================== */
        /* ================= GLOBAL ============================= */
        /* ===================================================== */

        /* Fond général de l'application */
        QMainWindow, QWidget {
            background-color: #1a2535;
            color: white;
            font-size: 13px;
        }


        /* ===================================================== */
        /* ================= BOUTONS ============================ */
        /* ===================================================== */

        /* Boutons bleus (caractéristiques) */
        #blueBtn {
            background-color: #2980b9;
            color: white;
            border-radius: 5px;
            padding: 6px 12px;
            font-weight: bold;
        }

        /* Hover */
        #blueBtn:hover {
            background-color: #3498db;
        }

        /* Click */
        #blueBtn:pressed {
            background-color: #1a6fa0;
        }


        /* Boutons généraux (toolbar) */
        QPushButton {
            background-color: #2f6f9f;
            color: white;
            border-radius: 6px;
            padding: 6px 12px;
        }

        /* Hover */
        QPushButton:hover {
            background-color: #3f8fcf;
        }

        /* Focus (navigation clavier) */
        QPushButton:focus {
            border: 1px solid #63b3ed;
        }


        /* ===================================================== */
        /* ================= TABS =============================== */
        /* ===================================================== */

        /* Fond global des tabs */
        QTabWidget::pane {
            background: #252f3e;
            border-top: 2px solid #2980b9;
        }

        /* Onglets non sélectionnés */
        QTabBar::tab {
            background: #2d3748;
            color: #aab4c4;
            padding: 6px 14px;
            margin-right: 2px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }

        /* Onglet actif */
        QTabBar::tab:selected {
            background: #2980b9;
            color: white;
            font-weight: bold;
        }

        /* Hover sur onglet */
        QTabBar::tab:hover:!selected {
            background: #3d4f63;
            color: white;
        }
        
        
        /* ===================================================== */
        /* ================= COMBOBOX =========================== */
        /* ===================================================== */
        
        QComboBox QAbstractItemView {
            background-color: #2d3748;
            color: white;
            selection-background-color: #2980b9;  /* 🔥 le bleu */
            selection-color: white;
            border-radius: 6px;
        }
        

        /* ===================================================== */
        /* ================= SCROLL AREA ======================== */
        /* ===================================================== */

        /* Conteneur scroll */
        QScrollArea {
            background: transparent;
            border: none;
        }

        /* ===================================================== */
        /* ================= SCROLLBAR (GLOBAL) ================= */
        /* ===================================================== */
        
        /* Fond commun */
        QScrollBar {
            background: #2d3748;
            margin: 2px;
            border: none;
        }
        
        /* Taille selon orientation */
        QScrollBar:vertical {
            margin: 10px 0px 10px 0px;
            width: 10px;
        }
        
        QScrollBar:horizontal {
            height: 10px;
            margin: 0px 10px 0px 10px;

        }
        
        /* Barre draggable (commune) */
        QScrollBar::handle:vertical,
        QScrollBar::handle:horizontal {
            background: #2980b9;
            border-radius: 4px;
        }
        
        /* Taille minimale */
        QScrollBar::handle:vertical {
            min-height: 20px;
        }
        
        QScrollBar::handle:horizontal {
            min-width: 20px;
        }
        
        /* Hover commun */
        QScrollBar::handle:vertical:hover,
        QScrollBar::handle:horizontal:hover {
            background: #3498db;
        }
        
        /* Bouton gauche */
        QScrollBar::sub-line:horizontal {
            subcontrol-origin: margin;
            subcontrol-position: left;
            width: 10px;
        }
        
        /* Bouton droite */
        QScrollBar::add-line:horizontal {
            subcontrol-origin: margin;
            subcontrol-position: right;
            width: 10px;
        }
        
        /* Bouton haut */
        QScrollBar::sub-line:vertical {
            subcontrol-origin: margin;
            subcontrol-position: top;
            height: 10px;
        }
        
        /* Bouton bas */
        QScrollBar::add-line:vertical {
            subcontrol-origin: margin;
            subcontrol-position: bottom;
            height: 10px;
        }

        /* ===================================================== */
        /* ================= PREVIEW PANEL ====================== */
        /* ===================================================== */

        /* Panel de droite */
        #sidePanel {
            background-color: #2d3748;
            border-left: 1px solid #3d4f63;
        }


        /* ===================================================== */
        /* ================= IMAGE VIEW ========================= */
        /* ===================================================== */

        /* Fond guitare */
        #guitarFrame {
            background-color: black;
            border: 2px solid #2d3748;
            border-radius: 6px;
        }
        """)
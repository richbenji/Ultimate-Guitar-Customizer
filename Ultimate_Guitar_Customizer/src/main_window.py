from PySide6.QtWidgets import QMainWindow
from src.views.main_view import MainView
from src.controllers.main_controller import MainController
from PySide6.QtGui import QGuiApplication
from src.paths import STYLES

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ultimate Guitar Customizer")

        screen = QGuiApplication.primaryScreen().availableGeometry()
        w = int(screen.width() * 0.8)  # 80 % de la largeur de l'écran
        h = int(screen.height() * 0.8)  # 80 % de la hauteur
        self.resize(w, h)
        self.move(screen.x() + (screen.width() - w) // 2,
                  screen.y() + (screen.height() - h) // 2)  # centrée
        self.setMinimumSize(1000, 600)

        self.view = MainView()
        self.setCentralWidget(self.view)

        self.controller = MainController(self.view)

        self.setStyleSheet((STYLES / "style.qss").read_text(encoding="utf-8"))
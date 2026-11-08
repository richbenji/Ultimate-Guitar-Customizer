from PySide6.QtWidgets import (
    QWidget, QTabWidget, QPushButton,
    QVBoxLayout, QGridLayout, QScrollArea, QListView
)
from PySide6.QtCore import Signal

from src.models.menus import GuitarOptions
from src.components.elided_combo import ElidedComboBox


class TabsView(QWidget):
    option_changed = Signal(str, str)

    def __init__(self):
        super().__init__()

        self.combos = {}

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.build_tabs()

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def build_tabs(self):
        sections = GuitarOptions.get_section_options()

        for name, options in sections.items():

            # ===== CONTENU =====
            content_widget = QWidget()
            grid = QGridLayout(content_widget)

            grid.setHorizontalSpacing(20)
            grid.setVerticalSpacing(12)
            grid.setContentsMargins(20, 20, 20, 20)

            columns = 3

            for c in range(columns * 2):
                grid.setColumnStretch(c, 1)

            row = 0
            for i, (label, values) in enumerate(options):
                row = i // columns
                col = (i % columns) * 2

                # ===== BOUTON =====
                label_widget = QPushButton(label)
                label_widget.setObjectName("blueBtn")
                label_widget.clicked.connect(
                    lambda _, l=label: self.option_changed.emit(l, "")
                )

                # ===== COMBO =====
                combo = ElidedComboBox()
                combo.setView(QListView())   # d'abord la vue...
                combo.set_items(list(values) if values else ["N/A"])   # ...puis les items

                self.combos[label] = combo

                combo.currentTextChanged.connect(
                    lambda val, l=label: self.option_changed.emit(l, val)
                )

                # ===== PLACEMENT DANS LA GRILLE =====
                grid.addWidget(label_widget, row, col)
                grid.addWidget(combo, row, col + 1)

            # pousse le contenu en haut
            grid.setRowStretch(row + 1, 1)

            # ===== SCROLL AREA =====
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setWidget(content_widget)

            # ===== AJOUT TAB =====
            self.tabs.addTab(scroll, name)

    def set_combo_value(self, label, value):
        """Met à jour un combo sans émettre option_changed (évite les boucles)."""
        combo = self.combos.get(label)
        if combo is None:
            return

        index = combo.findText(value)
        if index == -1:
            return

        combo.blockSignals(True)
        combo.setCurrentIndex(index)
        combo.blockSignals(False)
        combo.setToolTip(value)   # le signal bloqué ne l'a pas mis à jour
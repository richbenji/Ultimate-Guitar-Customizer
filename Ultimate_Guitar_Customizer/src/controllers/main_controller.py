from pathlib import Path

from PySide6.QtWidgets import QFileDialog

from src.models.guitar_config import GuitarConfig
from src.paths import ASSETS, slugify


class MainController:
    def __init__(self, view):
        self.view = view
        self.config = GuitarConfig()
        self.current_feature = None

        self.feature_folders = {
            "body wood": "body_wood",
            "brand": "brands",
            "bridge pickup brand": "pickup_brands",
            "colors": "colors",
            "dexterity": "dexterity",
            "fingerboard material": "fingerboard_material",
            "inlay shape": "inlays_shape",
            "middle pickup brand": "pickup_brands",
            "neck pickup brand": "pickup_brands",
            "neck shape": "neck_shape",
            "neck wood": "neck_wood",
            "top wood": "top_wood",
        }

        # Vue -> contrôleur
        self.view.tabs.option_changed.connect(self.on_option_clicked)
        self.view.preview_view.grid.item_clicked.connect(self.on_preview_clicked)

        self.view.btn_reset.clicked.connect(self.config.reset)
        self.view.btn_save.clicked.connect(self.save_config)
        self.view.btn_load.clicked.connect(self.load_config)

        # Modèle -> vue
        self.config.replaced.connect(self.sync_view)
        self.config.changed.connect(self.on_config_changed)

        self.sync_view()

    # ---------- interactions ----------

    def on_option_clicked(self, label, value):
        """Appelé par un clic sur un bouton (value == "") ou un changement de combo."""
        self.current_feature = label
        self.view.preview_view.title.setText(label)

        if value:
            self.config.set(label, value)

        self.refresh_preview()

    def on_preview_clicked(self, filename):
        if not self.current_feature:
            return

        combo = self.view.tabs.combos.get(self.current_feature)
        if not combo:
            return

        target = slugify(Path(filename).stem)
        for i in range(combo.count()):
            if slugify(combo.itemText(i)) == target:
                combo.setCurrentIndex(i)   # déclenche option_changed -> config.set
                break

    # ---------- réactions au modèle ----------

    def on_config_changed(self, label, value):
        print(f"[config] {label} = {value}")   # temporaire, pour tester

    def sync_view(self):
        """Recopie toute la config dans les combos (après reset ou chargement)."""
        for label, value in self.config.values.items():
            self.view.tabs.set_combo_value(label, value)
        self.refresh_preview()

    def refresh_preview(self):
        grid = self.view.preview_view.grid
        folder = self.feature_folders.get((self.current_feature or "").lower())

        if not folder:
            grid.clear()
            return

        grid.load_images(ASSETS / folder)
        value = self.config.get(self.current_feature)
        if value:
            grid.select_item(value)

    # ---------- fichiers ----------

    def save_config(self):
        path, _ = QFileDialog.getSaveFileName(
            self.view, "Sauvegarder la guitare", "ma_guitare.json", "Guitare (*.json)"
        )
        if path:
            self.config.save(path)

    def load_config(self):
        path, _ = QFileDialog.getOpenFileName(
            self.view, "Charger une guitare", "", "Guitare (*.json)"
        )
        if path:
            try:
                self.config.load(path)
            except (OSError, ValueError):
                pass   # on ajoutera un message d'erreur plus tard
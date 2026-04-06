import os

class MainController:
    def __init__(self, view):
        self.view = view

        self.view.tabs.option_changed.connect(self.on_option_clicked)
        self.view.preview_view.grid.item_clicked.connect(self.on_preview_clicked)

        self.current_feature = None

        self.feature_folders = {
            "Body wood": "assets/body_wood",
            "Brand": "assets/brands",
            "Bridge pickup brand": "assets/pickup_brands",
            "Colors": "assets/colors",
            "Dexterity": "assets/Dexterity",
            "Fingerboard material": "assets/Fingerboard_material",
            "Middle pickup brand": "assets/pickup_brands",
            "Neck pickup brand": "assets/pickup_brands",
            "Neck shape": "assets/neck_shape",
            "Neck wood": "assets/neck_wood",
            "Top wood": "assets/top_wood",
        }

    def on_option_clicked(self, label, value):
        self.current_feature = label

        # update titre
        self.view.preview_view.title.setText(label)

        # récupérer dossier automatiquement
        folder = self.feature_folders.get(label)

        if folder:
            self.view.preview_view.grid.load_images(folder)
        else:
            # si pas d'assets → vider
            self.view.preview_view.grid.clear()
            return

        # si une valeur est sélectionnée → sync preview
        if value:
            self.view.preview_view.grid.select_item(value)

    def on_preview_clicked(self, filename):
        if not self.current_feature:
            return

        value = filename.split(".")[0]

        combo = self.view.tabs.combos.get(self.current_feature)

        if combo:
            index = combo.findText(value)
            if index != -1:
                combo.setCurrentIndex(index)
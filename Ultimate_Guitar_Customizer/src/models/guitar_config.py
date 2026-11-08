import json
from pathlib import Path

from PySide6.QtCore import QObject, Signal

from src.models.menus import GuitarOptions

CONFIG_VERSION = 1


class GuitarConfig(QObject):
    changed = Signal(str, str)   # une option a changé : (libellé, valeur)
    replaced = Signal()          # toute la config a changé (reset, chargement)

    def __init__(self):
        super().__init__()

        # libellé -> valeurs autorisées
        self._choices = {}
        for options in GuitarOptions.get_section_options().values():
            for label, values in options:
                if values:                      # on ignore les options vides ("N/A")
                    self._choices[label] = tuple(values)

        # valeur par défaut = première de la liste
        self._defaults = {label: values[0] for label, values in self._choices.items()}
        self._values = dict(self._defaults)

    # ---------- lecture ----------

    def get(self, label, default=None):
        return self._values.get(label, default)

    @property
    def values(self):
        return dict(self._values)   # copie : on ne modifie la config que via set()

    # ---------- écriture ----------

    def set(self, label, value):
        """Change une option. Renvoie True si la valeur a réellement changé."""
        if label not in self._choices or value not in self._choices[label]:
            return False
        if self._values[label] == value:
            return False
        self._values[label] = value
        self.changed.emit(label, value)
        return True

    def reset(self):
        self._values = dict(self._defaults)
        self.replaced.emit()

    # ---------- sauvegarde / chargement ----------

    def to_dict(self):
        return {"version": CONFIG_VERSION, "options": dict(self._values)}

    def load_dict(self, data):
        """Charge une config en ignorant les libellés ou valeurs inconnus
        (utile si menus.py a évolué depuis la sauvegarde)."""
        values = dict(self._defaults)
        for label, value in data.get("options", {}).items():
            if label in self._choices and value in self._choices[label]:
                values[label] = value
        self._values = values
        self.replaced.emit()

    def save(self, path):
        Path(path).write_text(
            json.dumps(self.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def load(self, path):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        self.load_dict(data)
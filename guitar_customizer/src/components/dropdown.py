import customtkinter as ctk

class Dropdown(ctk.CTkComboBox):
    def __init__(self, parent, values, placeholder="...", **kwargs):
        """
        Classe Dropdown customisée basée sur CTkComboBox.

        :param parent: Widget parent dans lequel le dropdown est ajouté.
        :param values: Liste des valeurs à afficher dans le menu déroulant.
        :param placeholder: Texte affiché par défaut.
        :param kwargs: Autres paramètres supplémentaires pour CTkComboBox.
        """
        super().__init__(parent, values=values, **kwargs)
        self.set(placeholder)  # Définit le texte par défaut

    def get_selected_value(self):
        """Retourne la valeur sélectionnée dans le dropdown."""
        return self.get()

    def reset(self):
        """Réinitialise le dropdown en affichant le placeholder."""
        self.set("Select an option")

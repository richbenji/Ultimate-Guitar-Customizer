import customtkinter as ctk

# TODO : mettre une icône jour/nuit pour activer ou désactiver les modes clair et sombre ?

class ModeSwitch(ctk.CTkSwitch):
    def __init__(self, parent, controller, root, **kwargs):
        """
        Crée un switch pour basculer entre le dark mode et le light mode.
        :param parent: Le widget parent (Frame où le switch sera placé).
        :param controller: La fonction de contrôle (logique de bascule).
        :param root: La fenêtre principale (pour changer l'apparence globale).
        :param kwargs: Autres arguments pour CTkSwitch.
        """
        # appelle le constructeur de la classe parente, c'est-à-dire la méthode __init__() de CTkSwitch,
        # qui configure le widget de switch dans Tkinter
        super().__init__(parent, **kwargs)

        self.controller = controller  # Stocke la fonction de contrôle
        self.root = root  # Stocke la référence à la fenêtre principale
        self.configure(text="Dark Mode", command=self.calling_toggle_mode)  # Configure le switch
        self.select()  # Par défaut, sélectionne le mode sombre

    def calling_toggle_mode(self):
        """
        Appelle le contrôleur pour gérer la bascule entre le dark mode et le light mode.
        """
        self.controller(self, self.root)

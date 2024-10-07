import customtkinter as ctk

from src.components.switch import ModeSwitch
from src.controllers.menus_controller import create_options_section
from src.views.menus import section_options
from src.controllers.mode_controller import toggle_mode


class GuitarCustomizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Customizer")
        self.root.geometry("1000x500")

        ctk.set_appearance_mode("dark")  # Choisir le mode d'apparence : "dark" ou "light"
        ctk.set_default_color_theme("blue")  # Choisir le thème de couleur : "blue", "green", "dark-blue"

        # Initialisation des attributs d'instance
        self.left_frame = None
        self.center_frame = None
        self.right_frame = None
        self.sections = None

        #Créer la mise en page
        self.create_layout()

    def create_layout(self):
        # Frame gauche pour les options de la guitare
        self.left_frame = ctk.CTkFrame(self.root, width=300)
        self.left_frame.pack(side='left', fill='y', padx=5, pady=5)

        # Panneau central pour l'image de la guitare
        self.center_frame = ctk.CTkFrame(self.root, width=500)
        self.center_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        # Ajouter le switch en haut à droite du panneau central
        self.add_mode_switch(self.center_frame)

        # Frame droite pour les aperçus
        self.right_frame = ctk.CTkFrame(self.root, width=200)
        self.right_frame.pack(side='right', fill='y', padx=5, pady=5)

        # Créer un CTkScrollableFrame pour ajouter le scroll
        scrollable_frame = ctk.CTkScrollableFrame(self.left_frame, width=200, height=300)  # Taille personnalisée
        scrollable_frame.pack(fill="both", expand=True)

        # Ajouter tous les menus déroulants dans le panneau de gauche
        self.add_collapsible_sections(scrollable_frame)

    def add_collapsible_sections(self, parent):
        """
        Ajouter des sections repliables dans le panneau de gauche à partir d'une liste de sections.
        """
        self.sections = ["General", "Body", "Neck", "Electronics", "Hardware"]

        for section_name in self.sections:
            options = section_options.get(section_name, [])
            section_frame, section_content = create_options_section(parent, section_name, options)
            section_frame.pack(fill="x", pady=5)

    def add_mode_switch(self, parent):
        """
        Ajouter le switch pour basculer entre dark mode et light mode en haut à droite du panneau central.
        """
        # Créer un frame pour positionner le switch en haut à droite
        switch_frame = ctk.CTkFrame(parent, fg_color="transparent")
        switch_frame.pack(anchor='ne', pady=10, padx=10)

        # Ajouter le ModeSwitch
        mode_switch = ModeSwitch(switch_frame, toggle_mode, self.root)
        mode_switch.pack(anchor='ne')


if __name__ == "__main__":
    root = ctk.CTk()
    app = GuitarCustomizerApp(root)
    root.mainloop()

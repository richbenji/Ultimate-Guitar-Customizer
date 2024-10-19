from pathlib import Path
import customtkinter as ctk

from src.components.switch import ModeSwitch
from src.controllers.image_controller import load_image
from src.controllers.menus_controller import add_dropdowns_to_tab
from src.views.menus import section_options
from src.controllers.mode_controller import toggle_mode

# TODO : fixer les proportions des frame par rapport aux proportions de la fenêtre

class GuitarCustomizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Guitar Customizer")
        self.root.geometry("1000x500")
        self.root.configure(fg_color="#000000")

        ctk.set_appearance_mode("dark")  # Choisir le mode d'apparence : "dark" ou "light"
        ctk.set_default_color_theme("blue")  # Choisir le thème de couleur : "blue", "green", "dark-blue"

        # Initialisation des attributs d'instance
        self.top_frame = None
        self.bottom_frame = None
        self.center_frame = None
        self.right_frame = None
        self.sections = None
        self.title_label = None
        self.tabview = None

        # Charger la police personnalisée (en fait ça l'enregistre dans notre dossier de polices)
        base_path = Path(__file__).resolve().parent.parent.parent  # Remonte de 3 niveaux pour atteindre guitar_customizer
        font_path = base_path / "fonts" / "MetalMania-Regular.ttf"
        ctk.FontManager.load_font(font_path)  # Charge la police
        self.custom_font = ctk.CTkFont(family="MetalMania", size=38)

        #Créer la mise en page
        self.create_layout()

    def create_layout(self):
        # Frame du haut pour le titre
        self.top_frame = ctk.CTkFrame(self.root, width=100, corner_radius=0, fg_color="#03224C")
        self.top_frame.pack(side='top', fill='x', padx=0, pady=0)

        # Ajouter le switch en haut à droite du panneau central
        self.add_mode_switch(self.top_frame)

        # Ajouter le titre centré à droite du switch
        self.title_label = ctk.CTkLabel(self.top_frame, text="Ultimate Guitar Customizer", font=self.custom_font)
        self.title_label.place(relx=0.5, rely=0.5, anchor='center')

        # Frame droite pour les aperçus
        self.right_frame = ctk.CTkFrame(self.root, width=300, corner_radius=0)
        self.right_frame.pack(side='right', fill='y', padx=0, pady=0)

        self.create_tabview()

        # Panneau central pour l'image de la guitare
        self.center_frame = ctk.CTkFrame(self.root, width=500, corner_radius=0, fg_color="#000000")
        self.center_frame.pack(side='left', fill='both', expand=True, padx=5, pady=0)

        # Ajouter les boutons "Reset", "Front", et "Rear"
        self.add_center_buttons()

        # Afficher l'image dans le panneau central
        self.display_center_image()

    def display_center_image(self):
        """
        Charger et afficher l'image dans le panneau central.
        """
        # Charger l'image avec le contrôleur
        guitar_image = load_image("stratocaster.png", image_size=(400, 400))

        # Créer un label pour afficher l'image dans center_frame
        image_label = ctk.CTkLabel(self.center_frame, image=guitar_image)
        image_label.image = guitar_image  # Conserver une référence à l'image pour éviter le garbage collection
        image_label.pack(pady=20)

    def add_center_buttons(self):
        """
        Ajouter les boutons "Reset", "Front", et "Rear" dans le panneau central.
        """
        # Bouton Reset (en haut à gauche)
        reset_button = ctk.CTkButton(self.center_frame, text="Reset", width=100, corner_radius=20)
        reset_button.pack(side='left', anchor='nw', padx=10, pady=10)

        # Frame pour les boutons Front et Rear (en haut à droite)
        button_frame = ctk.CTkFrame(self.center_frame, fg_color="transparent")
        button_frame.pack(side='top', anchor='ne', padx=10, pady=10)

        # Bouton Front
        front_button = ctk.CTkButton(button_frame, text="Front", width=100, corner_radius=20)  # Bord arrondi extérieur
        front_button.pack(side='left', padx=(0, 10), pady=0)  # Espacement entre les deux boutons

        # Bouton Rear
        rear_button = ctk.CTkButton(button_frame, text="Rear", width=100, corner_radius=20)  # Bord arrondi extérieur
        rear_button.pack(side='left', pady=0)

    def create_tabview(self):
        # Créer un CTkTabview dans le panneau du bas pour les options de guitare
        self.tabview = ctk.CTkTabview(self.root, width=100, corner_radius=0)
        self.tabview.pack(side='bottom', fill='x', padx=5, pady=0)

        # Utiliser les clés de section_options pour créer dynamiquement les onglets
        for section_name in section_options.keys():
            tab = self.tabview.add(section_name)  # Crée un onglet pour chaque section
            add_dropdowns_to_tab(tab, section_name)  # Ajoute les dropdowns dans l'onglet correspondant


    def add_mode_switch(self, parent):
        """
        Ajouter le switch pour basculer entre dark mode et light mode en haut à droite du panneau central.
        """
        # Ajouter le ModeSwitch
        mode_switch = ModeSwitch(parent, toggle_mode, self.root)
        mode_switch.pack(side='left', anchor='w', padx=5, pady=5)


if __name__ == "__main__":
    root = ctk.CTk()
    app = GuitarCustomizerApp(root)
    root.mainloop()

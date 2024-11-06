from pathlib import Path
import customtkinter as ctk
from src.components.switch import ModeSwitch
from src.controllers.image_controller import load_image, resize_image
from src.controllers.menus_controller import add_dropdowns_to_tab
from src.controllers.mode_controller import toggle_mode
from src.views.menus import GuitarOptions

# TODO : résoudre le scrollbar avec le touchpad


class GuitarCustomizerApp:
    def __init__(self, main_window):
        self.root = main_window
        self.root.title("Ultimate Guitar Customizer")

        # Calculer et appliquer la taille de la fenêtre selon le format de l'écran de l'utilisateur
        window_width, window_height = self.calculate_window_size()
        self.root.geometry(f"{window_width}x{window_height}")

        # Couleurs de l'interface
        self.root.configure(fg_color="#03224C")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Charger la police personnalisée
        base_path = Path(__file__).resolve().parent.parent.parent  # Remonte de 3 niveaux pour atteindre guitar_customizer
        font_path = base_path / "fonts" / "MetalMania-Regular.ttf"
        ctk.FontManager.load_font(str(font_path))
        self.custom_font = ctk.CTkFont(family="MetalMania", size=38)

        # Initialisation des attributs d'instance
        self.top_frame = None
        self.bottom_frame = None
        self.center_frame = None
        self.right_frame = None
        self.sections = None
        self.title_label = None
        self.tabview = None
        self.spacing = 0.005

        # Créer la mise en page
        self.create_layout()

    def create_layout(self):
        # Frame du haut pour le titre (occupe toute la largeur)
        self.top_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="#03224C")
        self.top_frame.place(relx=0, rely=0, relwidth=1, relheight=1 / 13)  # Hauteur 1/13 de la fenêtre

        # Ajouter le switch
        self.add_mode_switch(self.top_frame)

        # Ajouter le titre centré à droite du switch
        self.title_label = ctk.CTkLabel(self.top_frame, text="Ultimate Guitar Customizer", font=self.custom_font,
                                        text_color="#00b2ff")
        self.title_label.place(relx=0.5, rely=0.5, anchor='center')

        # Frame droite pour les aperçus (occupe 1/4 de la largeur)
        self.right_frame = ctk.CTkScrollableFrame(self.root, corner_radius=10)
        self.right_frame.place(relx=3 / 4, rely=1 / 13, relwidth=1 / 4 - self.spacing,
                               relheight=12 / 13 - self.spacing)

        # Panneau central pour l'image de la guitare (occupe 3/4 de la largeur)
        self.center_frame = ctk.CTkFrame(self.root, corner_radius=10, fg_color="#000000")
        self.center_frame.place(relx=self.spacing, rely=1 / 13, relwidth=3 / 4 - 2 * self.spacing,
                                relheight=7 / 13)  # Prend 3/4 de la largeur et 2/3 de la hauteur restante

        # Ajouter les boutons et l'image dans le panneau central
        self.add_center_buttons()
        self.display_center_image()

        # Créer les onglets dans la zone inférieure (tabview)
        self.create_tabview()

    def calculate_window_size(self, width_ratio=0.8):
        """
        Calcule la taille de la fenêtre à 80 % de la résolution de l'écran de l'utilisateur.
        :param width_ratio: Proportion de la largeur de l'écran à utiliser (ex: 0.8 pour 80%)
        :return: Largeur et hauteur calculées pour la fenêtre
        """
        # Obtenir la résolution de l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculer la largeur et la hauteur de la fenêtre selon la proportion spécifiée
        window_width = int(screen_width * width_ratio)
        window_height = int(screen_height * width_ratio)  # Ajustez la hauteur en fonction de la largeur

        return window_width, window_height

    def display_center_image(self):
        """
        Charger et afficher l'image dans le panneau central, redimensionnée selon la taille de la frame.
        """
        # Charger l'image à sa taille d'origine
        guitar_image = load_image("Kiesel-CT6-1.png")

        # Mettre à jour l'interface pour s'assurer que les dimensions des frames sont calculées
        self.center_frame.update_idletasks()

        # Obtenir les dimensions de la frame centrale
        frame_width = self.center_frame.winfo_width()
        frame_height = self.center_frame.winfo_height()

        # Redimensionner l'image pour qu'elle corresponde à la taille de la frame
        resized_image = resize_image(guitar_image, frame_width, frame_height)

        # Créer un label pour afficher l'image redimensionnée dans center_frame
        image_label = ctk.CTkLabel(self.center_frame,
                                   image=resized_image,
                                   text="")  # texte vide sinon il affiche "CTKLabel sur l'image)
        image_label.image = resized_image  # Conserver une référence à l'image pour éviter le garbage collection

        # Centrer l'image dans la frame
        image_label.place(relx=0.5, rely=0.5, anchor='center')

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
        # Créer une CTkScrollableFrame pour contenir le tabview
        scrollable_frame = ctk.CTkScrollableFrame(self.root, corner_radius=10)
        scrollable_frame.place(relx=self.spacing, rely=8 / 13 + self.spacing,
                               relwidth=3 / 4 - 2 * self.spacing,
                               relheight=5 / 13 - 2 * self.spacing)

        # Créer un CTkTabview dans la scrollable_frame pour les options de guitare
        self.tabview = ctk.CTkTabview(scrollable_frame, corner_radius=10)
        self.tabview.pack(fill='both', expand=True)

        # Utiliser les clés de section_options pour créer dynamiquement les onglets
        section_options = GuitarOptions.get_section_options()
        for section_name in section_options.keys():
            tab = self.tabview.add(section_name)  # Crée un onglet pour chaque section
            add_dropdowns_to_tab(tab, section_name,
                                 self.right_frame)  # Ajoute les dropdowns dans l'onglet correspondant

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

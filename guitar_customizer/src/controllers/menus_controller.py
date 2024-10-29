import customtkinter as ctk
from src.components.dropdown import Dropdown
from src.views.menus import section_options

# TODO : insérer une barre pour pouvoir descendre dans les menus quand ça dépasse de la fenêtre
# TODO : scrollbar -> si les options des menus sont trop long par rapport à l'écran, on doit pouvoir naviguer avec la roulette
# TODO : insérer des boutons pour le bois ou les couleurs, qui apparaitront par la suite dans le panneau de droite

def add_dropdowns_to_tab(tab, section_name, columns=4):
    """
    Ajouter les dropdowns correspondant aux options de chaque section dans une grille de l'onglet.
    :param tab: Onglet où ajouter les options.
    :param section_name: Nom de la section (General, Body, etc.).
    :param columns: Nombre de colonnes dans la grille (par défaut 4).
    """
    # Récupérer les options pour la section
    options = section_options.get(section_name, [])

    # Variables pour gérer la disposition dans la grille
    row = 0
    col = 0

    # Créer et ajouter un label et un dropdown pour chaque option
    for label_text, dropdown_values in options:
        # Créer le label pour l'option
        option_label = ctk.CTkLabel(tab, text=label_text)

        # Créer le dropdown menu pour l'option
        dropdown_menu = Dropdown(tab, values=dropdown_values)

        # Positionner le label et le dropdown dans la grille
        option_label.grid(row=row, column=col, padx=10, pady=5, sticky="w")
        dropdown_menu.grid(row=row+1, column=col, padx=10, pady=5, sticky="w")

        # Gérer la position suivante dans la grille (sur 4 colonnes)
        col += 1
        if col >= columns:
            col = 0
            row += 2  # On avance de 2 lignes (une pour le label, une pour le dropdown)

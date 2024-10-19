import customtkinter as ctk
from src.components.dropdown import Dropdown
from src.views.menus import section_options

# TODO : insérer une barre pour pouvoir descendre dans les menus quand ça dépasse de la fenêtre
# TODO : scrollbar -> si les options des menus sont trop long par rapport à l'écran, on doit pouvoir naviguer avec la roulette
# TODO : insérer des boutons pour le bois ou les couleurs, qui apparaitront par la suite dans le panneau de droite


def add_dropdowns_to_tab(tab, section_name):
    """
    Ajouter les dropdowns correspondant aux options de chaque section dans l'onglet.
    :param tab: Onglet où ajouter les options.
    :param section_name: Nom de la section (General, Body, etc.).
    """
    # Récupérer les options pour la section
    options = section_options.get(section_name, [])

    # Créer et ajouter un label et un dropdown pour chaque option
    for label_text, dropdown_values in options:
        option_label = ctk.CTkLabel(tab, text=label_text)
        option_label.pack(pady=5)

        dropdown_menu = Dropdown(tab, values=dropdown_values)
        dropdown_menu.pack(fill="x", padx=5, pady=5)
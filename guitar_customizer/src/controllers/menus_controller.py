import customtkinter as ctk
from src.components.dropdown import Dropdown
from src.views.menus import section_options
from pathlib import Path

# Options nécessitant un affichage sous forme de boutons dans right_frame
options_with_images = {
    "Body": ["Body wood", "Top wood", "Colors"],
    "Neck": ["Wood", "Fingerboard material"]
}

def add_dropdowns_to_tab(tab, section_name, right_frame, columns=4):
    """
    Ajouter les dropdowns ou boutons correspondant aux options de chaque section dans une grille de l'onglet.
    :param tab: Onglet où ajouter les options.
    :param section_name: Nom de la section (ex: General, Body).
    :param right_frame: Frame pour afficher les options dynamiques sous forme de boutons.
    :param columns: Nombre de colonnes dans la grille (par défaut 4).
    """
    # Récupère les options pour la section
    options = section_options.get(section_name, [])
    row = 0

    for label_text, dropdown_values in options:
        # Vérifie si l'option doit être affichée sous forme de boutons dans right_frame
        if section_name in options_with_images and label_text in options_with_images[section_name]:
            # Crée un bouton pour afficher les options dans la frame de droite
            image_button = ctk.CTkButton(
                tab,
                text=label_text,
                command=lambda values=dropdown_values, label=label_text: show_options_with_text(right_frame, values, label)
            )
            image_button.grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky="w")
            row += 1
        else:
            # Place le label et le dropdown sur la même ligne
            option_label = ctk.CTkLabel(tab, text=label_text)
            option_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            # Crée et place le dropdown à côté du label
            dropdown_menu = Dropdown(tab, values=dropdown_values)
            dropdown_menu.grid(row=row, column=1, padx=10, pady=5, sticky="ew")

            # Configure les colonnes pour que le dropdown prenne plus d'espace horizontal
            tab.grid_columnconfigure(1, weight=1)  # Permet au dropdown d'étendre sa largeur

            # Passe à la ligne suivante
            row += 1


def show_options_with_text(right_frame, option_values, option_label):
    """
    Affiche le nom de l'option centré en haut de la frame et les options sous forme de boutons redimensionnables sur 2 colonnes.
    :param right_frame: Frame où afficher le nom de l'option et les boutons.
    :param option_values: Liste des valeurs d'options à afficher sous forme de boutons.
    :param option_label: Nom de l'option à afficher en haut de la frame.
    """
    # Efface les widgets existants dans la frame droite
    for widget in right_frame.winfo_children():
        widget.destroy()

    # Configure la grille de la frame pour un redimensionnement automatique
    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(1, weight=1)

    # Affiche le nom de l'option centré en haut de la frame
    title_label = ctk.CTkLabel(right_frame, text=option_label, font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n", padx=10)

    # Affiche les options sous forme de boutons, alignés sur 2 colonnes et redimensionnables
    row = 1  # Commence après le titre
    col = 0
    for value in option_values:
        option_button = ctk.CTkButton(
            right_frame,
            text=value,
            command=lambda selected=value: select_option(option_label, selected)
        )
        # Le bouton remplit sa cellule et s'adapte à la taille de la frame
        option_button.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")

        # Alterne entre les colonnes pour créer 2 colonnes
        col += 1
        if col >= 2:  # Passe à la ligne suivante après 2 colonnes
            col = 0
            row += 1

def select_option(option_label, selected_value):
    """
    Enregistre ou affiche le choix de l'utilisateur pour l'option spécifiée.
    :param option_label: Nom de l'option (ex: "Body wood").
    :param selected_value: Valeur sélectionnée.
    """
    print(f"{option_label} sélectionné: {selected_value}")
    # Cette fonction peut être étendue pour mettre à jour un modèle de données ou l'interface

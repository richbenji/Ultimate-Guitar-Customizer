import customtkinter as ctk
from src.views.menus import GuitarOptions

def add_dropdowns_to_tab(tab, section_name, right_frame, placeholder="...", columns=3):
    """
    Ajoute un bouton pour chaque option, suivi d'un ComboBox pour les options disponibles, alignés sur 3 colonnes.
    :param placeholder: texte affiché par défaut.
    :param tab: Onglet où ajouter les boutons et ComboBox.
    :param section_name: Nom de la section (ex: General, Body).
    :param right_frame: Frame pour afficher les options dynamiques sous forme de boutons.
    :param columns: Nombre de colonnes d'options dans la grille (par défaut 3 pour un alignement sur 3 colonnes).
    """
    # Récupère les options pour la section
    # Appel de GuitarOptions.get_section_options() pour récupérer les options de section
    section_options = GuitarOptions.get_section_options()
    options = section_options.get(section_name, [])
    row = 0
    col = 0

    for label_text, dropdown_values in options:
        # Crée un bouton pour l'option
        option_button = ctk.CTkButton(
            tab,
            text=label_text,
            command=lambda label=label_text: show_selected_option(right_frame, label)
        )
        option_button.grid(row=row, column=col * 2, padx=10, pady=5, sticky="w")

        # Crée un ComboBox à côté du bouton pour afficher les options disponibles
        option_combobox = ctk.CTkComboBox(tab, values=dropdown_values)
        option_combobox.set(placeholder)
        option_combobox.grid(row=row, column=col * 2 + 1, padx=10, pady=5, sticky="ew")

        # Configure la colonne de ComboBox pour qu'elle s'étende
        tab.grid_columnconfigure(col * 2 + 1, weight=1)

        # Alterne entre les colonnes et passe à la ligne suivante après 3 ensembles
        col += 1
        if col >= columns:
            col = 0
            row += 1

def show_selected_option(right_frame, selected_option):
    """
    Affiche le nom de l'option sélectionnée dans la frame de droite.
    :param right_frame: Frame où afficher l'option sélectionnée.
    :param selected_option: Nom de l'option sélectionnée.
    """
    # Efface les widgets existants dans la frame droite
    for widget in right_frame.winfo_children():
        widget.destroy()

    # Affiche le nom de l'option sélectionnée en haut de la frame
    label = ctk.CTkLabel(right_frame, text=f"{selected_option}", font=(None, 16, "bold"))
    label.pack(pady=20)

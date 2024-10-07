import customtkinter as ctk
from src.components.dropdown import Dropdown

# TODO : insérer une barre pour pouvoir descendre dans les menus quand ça dépasse de la fenêtre
# TODO : scrollbar -> si les options des menus sont trop long par rapport à l'écran, on doit pouvoir naviguer avec la roulette
# TODO : insérer des boutons pour le bois ou les couleurs, qui apparaitront par la suite dans le panneau de droite

def toggle_section(content_frame):
    """
    Basculer la visibilité d'un frame. Si le frame est caché, il apparaît, sinon il se cache.
    :param content_frame: Le frame dont on veut basculer la visibilité.
    """
    if content_frame.winfo_ismapped():  # Si le frame est visible
        content_frame.pack_forget()  # Masquer le contenu
    else:
        content_frame.pack(fill="x", pady=5)  # Afficher le contenu

def create_options_section(parent, section_name, options):
    """
    Crée une section repliable de manière générique.
    :param parent: Frame parent dans lequel ajouter les options.
    :param section_name: Nom de la section (ex. "General Options", "Body Options").
    :param options: Liste d'options à afficher sous forme de tuples (label, [valeurs du dropdown]).
    :return: La frame de la section et la frame du contenu déroulant.
    """
    section_frame = ctk.CTkFrame(parent)
    content_frame = ctk.CTkFrame(section_frame)

    # Bouton pour dérouler/réduire la section, relié à la fonction de bascule
    toggle_button = ctk.CTkButton(section_frame, text=section_name,
                                  command=lambda: toggle_section(content_frame))
    toggle_button.pack(fill="x")

    content_frame.pack_forget()  # On cache le contenu par défaut

    # Ajout des options sous forme de Dropdown
    for label_text, dropdown_values in options:
        option_label = ctk.CTkLabel(content_frame, text=label_text)
        option_label.pack()
        dropdown_menu = Dropdown(content_frame, values=dropdown_values)
        dropdown_menu.pack(fill="x", pady=5)

    return section_frame, content_frame

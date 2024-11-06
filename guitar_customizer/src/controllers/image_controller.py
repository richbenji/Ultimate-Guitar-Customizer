from PIL import Image, UnidentifiedImageError
from pathlib import Path
from customtkinter import CTkImage

def load_image(image_name, image_folder="assets/body_shape/"):
    """
    Charger une image depuis le dossier assets à sa taille d'origine.
    :param image_name: Nom du fichier image (ex: stratocaster.png).
    :param image_folder: Dossier où se trouve l'image.
    :return: Image PIL à utiliser pour le redimensionnement.
    """

    # Construire un chemin absolu en partant du dossier racine
    base_path = Path(__file__).resolve().parent.parent.parent  # Chemin vers le dossier racine
    image_path = base_path / image_folder / image_name

    if not image_path.exists():
        print(f"Erreur : l'image {image_name} n'a pas été trouvée dans {image_folder}.")
        return None
    try:
        # Charger l'image
        image = Image.open(image_path)
        return image
    except UnidentifiedImageError:
        print(f"Erreur : le fichier {image_name} n'est pas une image valide.")
        return None


def resize_image(image, frame_width, frame_height):
    """
    Redimensionner l'image en fonction de la taille de la frame tout en conservant les proportions.
    :param image: Image PIL à redimensionner.
    :param frame_width: Largeur de la frame.
    :param frame_height: Hauteur de la frame.
    :return: CTkImage redimensionnée.
    """
    # Obtenir les dimensions de l'image d'origine
    original_width, original_height = image.size

    # Calculer le rapport d'aspect
    aspect_ratio = original_width / original_height

    # Calculer les nouvelles dimensions en fonction de la taille de la frame
    if frame_width / frame_height > aspect_ratio:
        new_width = int(frame_height * aspect_ratio)
        new_height = frame_height
    else:
        new_width = frame_width
        new_height = int(frame_width / aspect_ratio)

    # Redimensionner l'image tout en préservant le rapport d'aspect
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Convertir l'image redimensionnée en CTkImage compatible avec CustomTkinter
    return CTkImage(resized_image, size=(new_width, new_height))
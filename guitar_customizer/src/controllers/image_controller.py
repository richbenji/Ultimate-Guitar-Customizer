from PIL import Image, ImageTk
from pathlib import Path

# TODO : importer en gardant les proportions de l'image, et que la taille s'adapte à la taille de la fenêtre

def load_image(image_name, image_folder="assets/body_shape", image_size=(400, 400)):
    """
    Charger une image depuis le dossier assets.
    :param image_name: Nom du fichier image (ex: stratocaster.png).
    :param image_folder: Dossier où se trouve l'image.
    :param image_size: Tuple (width, height) pour redimensionner l'image.
    :return: ImageTk.PhotoImage à utiliser dans un widget Tkinter.
    """
    # Chemin de l'image
    image_path = Path(image_folder) / image_name

    # Charger l'image avec PIL et la redimensionner
    image = Image.open(image_path)
    # Obtenir les dimensions de l'image d'origine
    original_width, original_height = image.size

    # Calculer le rapport d'aspect
    aspect_ratio = original_width / original_height

    # Déterminer les nouvelles dimensions
    frame_width, frame_height = image_size
    if frame_width / frame_height > aspect_ratio:
        new_width = int(frame_height * aspect_ratio)
        new_height = frame_height
    else:
        new_width = frame_width
        new_height = int(frame_width / aspect_ratio)

    # Redimensionner l'image tout en préservant le rapport d'aspect
    image = image.resize((new_width, new_height), Image.LANCZOS)

    # Convertir l'image en PhotoImage compatible avec Tkinter
    return ImageTk.PhotoImage(image)

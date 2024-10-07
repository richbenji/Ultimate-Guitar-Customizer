import customtkinter as ctk

def toggle_mode(switch, root):
    """
    Bascule entre le mode clair et le mode sombre.
    :param switch: Le ModeSwitch qui gère l'état actuel.
    :param root: La fenêtre principale à laquelle appliquer le changement.
    """
    if switch.get():  # Si le switch est activé, on bascule en mode sombre
        ctk.set_appearance_mode("dark")
        switch.configure(text="Dark Mode")
    else:  # Si le switch est désactivé, on bascule en mode clair
        ctk.set_appearance_mode("light")
        switch.configure(text="Light Mode")

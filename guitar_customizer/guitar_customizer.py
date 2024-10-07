import customtkinter as ctk
from src.views.main_view import GuitarCustomizerApp

if __name__ == "__main__":
    root = ctk.CTk()
    app = GuitarCustomizerApp(root)
    root.mainloop()

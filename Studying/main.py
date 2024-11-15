from Flashcards import Flashcard
import customtkinter as ct

flashcard = Flashcard()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

Window = ct.CTk()
Window.geometry("500x300")
Window.resizable(True, True)
Window.title(" ")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

MainLabel = ct.CTkLabel(master=Frame, text="Welcome to flashcards program!")
MainLabel.pack()

ButtonLabel = ct.CTkLabel(master=Frame, text="To start, please create a flashcard ↓")
ButtonLabel.pack()

CreateFlashcard = ct.CTkButton(master=Frame, text="Create a flashcard here!", command=None)
CreateFlashcard.pack()

Window.mainloop()
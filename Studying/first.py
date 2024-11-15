# Window for people who are opening the program for the first time

import customtkinter as ct

class SpawnWindow:
    def spawnWindow(self):
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        Window = ct.CTk()
        Window.geometry("500x300")
        Window.resizable(True, True)
        Window.title(" ")

        Frame = ct.CTkFrame(master=Window)
        Frame.pack(fill="both", expand=True)

        MainLabel = ct.CTkLabel(master=Frame, text="Welcome to flashcard program!")
        MainLabel.pack()

        CreateButtonLabel = ct.CTkLabel(master=Frame, text="Create your first flashcard here ↓↓↓↓↓")
        CreateButtonLabel.pack()
        CreateButton = ct.CTkButton(master=Frame, text="Create a flashcard", command=None)
        CreateButton.pack()

        Window.mainloop()
    
    def sayHi(self):
        print("Hi")

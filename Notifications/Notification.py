import customtkinter as ct
import datetime
import time


def createWindow(Number=None, Date=None, Hour=None, Title=None, Content=None):
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    Window = ct.CTk() 
    Window.geometry("500x300") 
    Window.resizable(False, False)

    Window.title("  ")

    Frame = ct.CTkFrame(master=Window) 
    Frame.pack(fill="both", expand=True)

    MainLabel = ct.CTkLabel(master=Frame, text=f"Notification {Number}")
    MainLabel.pack()

    TitleLabel = ct.CTkLabel(master=Frame, text=f"Title: {Title}")
    TitleLabel.pack()

    ContentLabel = ct.CTkLabel(master=Frame, text=f"Content: {Content}")
    ContentLabel.pack()

    DateLabel = ct.CTkLabel(master=Frame, text=f"Date: {Date}")
    DateLabel.pack()

    HourLabel = ct.CTkLabel(master=Frame, text=f"Hour: {Hour}")
    HourLabel.pack()

    Window.mainloop()
from winotify import Notification

import customtkinter as ct
import datetime
import time
import threading

def GetCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

Date, Hour = GetCurrentTime()
now = datetime.datetime.now()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

Window = ct.CTk()
Window.geometry("450x350")

Window.title("                                               Notification Program")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

Label = ct.CTkLabel(master=Frame, text=GetCurrentTime())
Label.pack(pady=10, padx=10)

Entry1 = ct.CTkEntry(master=Frame, placeholder_text="Date")
Entry1.pack(pady=10, padx=10)

Entry2 = ct.CTkEntry(master=Frame, placeholder_text="Hour")
Entry2.pack(pady=10, padx=10)

Entry3 = ct.CTkEntry(master=Frame, placeholder_text="Title")
Entry3.pack(pady=10, padx=10)

Entry4 = ct.CTkEntry(master=Frame, placeholder_text="Content")
Entry4.pack(pady=10, padx=10)

def check_time(entry_date, entry_hour, entry_title, entry_content, duration):
    while True:
        current_date, current_hour = GetCurrentTime()
        if current_date == entry_date and current_hour == entry_hour:
            Noti = Notification(
                app_id="Notification program",
                title=entry_title,
                msg=entry_content,
                duration=duration.lower()
            )
            Noti.show()
            break
        
        time.sleep(20)

def get_entry(WhateverIsThis=None):
    entry_date = Entry1.get()
    entry_hour = Entry2.get()
    entry_title = Entry3.get()
    entry_content = Entry4.get()
    duration = Combobox.get()

    threading.Thread(target=check_time, args=(entry_date, entry_hour, entry_title, entry_content, duration), daemon=True).start()

Combobox = ct.CTkComboBox(Frame, values=["Short (recommended)", "Long"], command=get_entry)
Combobox.pack(pady=10, padx=10)

Button = ct.CTkButton(master=Frame, text="Confirm", command=get_entry)
Button.pack(pady=10, padx=10)

Window.mainloop()
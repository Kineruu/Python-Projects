from winotify import Notification
from clipboard import copy, paste

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
Window.geometry("350x250")

Window.title("              Notification Program")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

Label = ct.CTkLabel(master=Frame, text=GetCurrentTime())
Label.pack(pady=4)

Entry1 = ct.CTkEntry(master=Frame, placeholder_text="Date")
Entry1.pack(pady=4)

Entry2 = ct.CTkEntry(master=Frame, placeholder_text="Hour")
Entry2.pack(pady=4)

Entry3 = ct.CTkEntry(master=Frame, placeholder_text="Title")
Entry3.pack(pady=4)

Entry4 = ct.CTkEntry(master=Frame, placeholder_text="Content")
Entry4.pack(pady=4)

def CurrentDate():
    now = datetime.datetime.now()
    NowDate = now.strftime("%d.%m.%y")
    Entry1.insert(0, NowDate)

Entry5 = ct.CTkButton(master=Frame, text="Current Date", command=CurrentDate, width=40)
Entry5.place(x=250, y=40)

def CurrentHour():
    now = datetime.datetime.now()
    NowHour = now.strftime("%H:%M")
    Entry2.insert(0, NowHour)

Entry5 = ct.CTkButton(master=Frame, text="Current Hour", command=CurrentHour, width=40)
Entry5.place(x=250, y=77)

def Paste6():
    UserPaste = paste()
    Entry3.insert(0, UserPaste)

Entry6 = ct.CTkButton(master=Frame, text="Paste", command=Paste6, width=85)
Entry6.place(x=250, y=112)

def Paste7():
    UserPaste = paste()
    Entry4.insert(0, UserPaste) 

Entry7 = ct.CTkButton(master=Frame, text="Paste", command=Paste7, width=85)
Entry7.place(x=250, y=148)


def check_time(entry_date, entry_hour, entry_title, entry_content):
    while True:
        current_date, current_hour = GetCurrentTime()
        if current_date == entry_date and current_hour == entry_hour:
            Noti = Notification(
                app_id="Notification program",
                title=entry_title,
                msg=entry_content,
                duration="short"
            )
            Noti.show()
            break
        
        time.sleep(20)

def get_entry(WhateverIsThis=None):
    entry_date = Entry1.get()
    entry_hour = Entry2.get()
    entry_title = Entry3.get()
    entry_content = Entry4.get()
    
    threading.Thread(target=check_time, args=(entry_date, entry_hour, entry_title, entry_content), daemon=True).start()


Button = ct.CTkButton(master=Frame, text="Confirm", command=get_entry)
Button.pack(pady=10, padx=10)

Window.mainloop()

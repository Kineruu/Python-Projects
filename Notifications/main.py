from winotify import Notification, audio
from clipboard import paste

import customtkinter as ct
import datetime
import time
import threading

def GetCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

def GetCurrentHour():
    now = datetime.datetime.now()
    CurrentHour = now.hour
    return CurrentHour

Hour = GetCurrentHour()

if Hour <= 6:
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
else:
    ct.set_appearance_mode("light")
    ct.set_default_color_theme("green")


Window = ct.CTk()
Window.geometry("370x300")
Window.resizable(False, False)

Window.title("              Notification Program")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

Label = ct.CTkLabel(master=Frame, text=GetCurrentTime())
Label.pack(pady=4)

DateEntry = ct.CTkEntry(master=Frame, placeholder_text="Date")
DateEntry.pack(pady=4)

HourEntry = ct.CTkEntry(master=Frame, placeholder_text="Hour")
HourEntry.pack(pady=4)

TitleEntry = ct.CTkEntry(master=Frame, placeholder_text="Title")
TitleEntry.pack(pady=4)

ContentEntry = ct.CTkEntry(master=Frame, placeholder_text="Content")
ContentEntry.pack(pady=4)

def CurrentDate():
    now = datetime.datetime.now()
    NowDate = now.strftime("%d.%m.%y")
    DateEntry.delete(0, ct.END)
    DateEntry.insert(0, NowDate)

CurrentDateButton = ct.CTkButton(master=Frame, text="Current Date", command=CurrentDate, width=92)
CurrentDateButton.place(x=260, y=40)

def CurrentHour():
    now = datetime.datetime.now()
    NowHour = now.strftime("%H:%M")
    HourEntry.delete(0, ct.END)
    HourEntry.insert(0, NowHour)

CurrentHourButton = ct.CTkButton(master=Frame, text="Current Hour", command=CurrentHour, width=92)
CurrentHourButton.place(x=260, y=77)

def Paste1():
    UserPaste = paste()
    TitleEntry.delete(0, ct.END)
    TitleEntry.insert(0, UserPaste)

PasteButton1 = ct.CTkButton(master=Frame, text="Paste title", command=Paste1, width=92)
PasteButton1.place(x=260, y=112)

def Paste2():
    UserPaste = paste()
    ContentEntry.delete(0, ct.END)
    ContentEntry.insert(0, UserPaste) 

PasteButton2 = ct.CTkButton(master=Frame, text="Paste content", command=Paste2, width=88)
PasteButton2.place(x=260, y=148)

WarningLabel = ct.CTkLabel(master=Frame, text="If the entries boxes are empty, \nthe notification will NOT show up.")
WarningLabel.place(x=90, y=221)

def check_time(entry_date, entry_hour, entry_title, entry_content):
    while True:
        current_date, current_hour = GetCurrentTime()
        if current_date == entry_date and current_hour == entry_hour and entry_title != "" and entry_content != "":
            print("Triggering notification...")
            Noti = Notification(
                app_id="Notification program",
                title=entry_title,
                msg=entry_content,
                duration="short"
            )

            Noti.set_audio(audio.Default, loop=False)
            Noti.show()
            break

        else:
            pass

        time.sleep(5)

def get_entry(WhateverIsThis=None):
    entry_date = DateEntry.get()
    entry_hour = HourEntry.get()
    entry_title = TitleEntry.get()
    entry_content = ContentEntry.get()
    
    threading.Thread(target=check_time, args=(entry_date, entry_hour, entry_title, entry_content), daemon=True).start()

Button = ct.CTkButton(master=Frame, text="Confirm", command=get_entry)
Button.pack(pady=10, padx=10)

Window.mainloop()
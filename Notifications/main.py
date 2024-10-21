from Notification import createWindow
from winotify import Notification, audio
from clipboard import paste

import customtkinter as ct
import threading
import datetime
import time
import json
import os

BasePath = os.path.dirname(os.path.abspath(__file__))

def GetCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

def GetCurrentHour():
    now = datetime.datetime.now()
    CurrentHour = now.hour
    return CurrentHour

Hour = GetCurrentHour()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

Window = ct.CTk()
Window.geometry("500x300")
Window.resizable(False, False)
Window.title("  Notification Program") 

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

Label = ct.CTkLabel(master=Frame, text=GetCurrentTime()) 
Label.pack(pady=4)

DateEntry = ct.CTkEntry(master=Frame, placeholder_text="Date") 
DateEntry.pack(pady=4)

HourEntry = ct.CTkEntry(master=Frame, placeholder_text="Hour") 
HourEntry.pack(pady=4)

TitleEntry = ct.CTkEntry(master=Frame, placeholder_text="Title <=256 char")
TitleEntry.pack(pady=4)

ContentEntry = ct.CTkEntry(master=Frame, placeholder_text="Content <=256 char")
ContentEntry.pack(pady=4)

def CurrentDate():
    now = datetime.datetime.now()
    NowDate = now.strftime("%d.%m.%y")
    DateEntry.delete(0, ct.END)
    DateEntry.insert(0, NowDate)

CurrentDateButton = ct.CTkButton(master=Frame, text="Current Date", command=CurrentDate, width=92) 
CurrentDateButton.place(x=325, y=40)

def CurrentHour(): 
    now = datetime.datetime.now()
    NowHour = now.strftime("%H:%M")
    HourEntry.delete(0, ct.END)
    HourEntry.insert(0, NowHour)

CurrentHourButton = ct.CTkButton(master=Frame, text="Current Hour", command=CurrentHour, width=92)
CurrentHourButton.place(x=325, y=77)

def PasteTitleDef():
    UserPaste = paste()
    TitleEntry.delete(0, ct.END)
    TitleEntry.insert(0, UserPaste)

PasteTitle = ct.CTkButton(master=Frame, text="Paste title", command=PasteTitleDef, width=92) 
PasteTitle.place(x=325, y=112)

def PasteContentDef():
    UserPaste = paste()
    ContentEntry.delete(0, ct.END)
    ContentEntry.insert(0, UserPaste) 

PasteContent = ct.CTkButton(master=Frame, text="Paste content", command=PasteContentDef, width=88) 
PasteContent.place(x=325, y=148)


def LatestNotification():
    with open(os.path.join(BasePath, "Number.txt"), "r") as f:
        NumberFile = int(f.read().strip())

    with open(os.path.join(BasePath, f"NotificationsList\\Notification{NumberFile}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]
        Content = FileContent["Content"]
        Date = FileContent["Date"]
        Hour = FileContent["Hour"]

    createWindow(Number=int(NumberFile), Title=Title, Content=Content, Date=Date, Hour=Hour)

def PreviousNotification():
    with open(os.path.join(BasePath, "Number.txt"), "r") as f:
        NumberFile = int(f.read().strip())

    with open(os.path.join(BasePath, f"NotificationsList\\Notification{NumberFile-1}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]
        Content = FileContent["Content"]
        Date = FileContent["Date"]
        Hour = FileContent["Hour"]

    createWindow(Number=int(NumberFile-1), Title=Title, Content=Content, Date=Date, Hour=Hour)

def GetTitleFromFiles():
    with open(os.path.join(BasePath, "Number.txt"), "r") as f:
        NumberFile = int(f.read().strip())

    with open(os.path.join(BasePath, f"NotificationsList\\Notification{NumberFile}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]
    
    LatestNotificationButton.configure(text=(Title[:15] + "..." if len(Title) > 25 else Title))

    with open(os.path.join(BasePath, f"NotificationsList\\Notification{NumberFile-1}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]

    PreviousNotificationButton.configure(text=Title[:10] + "..." if len(Title) > 15 else Title)

LatestNotificationButton = ct.CTkButton(master=Frame, text=None, command=LatestNotification, width=60, height=35)
LatestNotificationButton.place(x=5, y=10)

PreviousNotificationButton = ct.CTkButton(master=Frame, text=None, command=PreviousNotification, width=40, height=35)
PreviousNotificationButton.place(x=15, y=50)

GetTitleFromFiles()

def check_time(entry_date, entry_hour, entry_title, entry_content):
    while True:
        current_date, current_hour = GetCurrentTime()

        if current_date == entry_date and current_hour == entry_hour and entry_title != "" and entry_content != "":
            Noti = Notification( # Self explanatory
                app_id="Notification program",
                title=entry_title,
                msg=entry_content,
                duration="short"
            )

            with open(os.path.join(BasePath, "Number.txt"), "r+") as f:
                Number = int(f.read().strip())
                Number += 1
                f.seek(0) 
                f.write(str(Number))
                f.truncate()

            NotificationJSON = {
                "Title": entry_title,
                "Content": entry_content,
                "Date": entry_date,
                "Hour": entry_hour
            }

            jsonPath = os.path.join(BasePath, f"NotificationsList\\Notification{Number}.json")
            with open(jsonPath, "w") as f:
                json.dump(NotificationJSON, f, indent=4)

            GetTitleFromFiles()

            Noti.set_audio(audio.Default, loop=False)
            Noti.show()
            break
        else:
            pass
        time.sleep(5)

def get_entry():
    entry_date = DateEntry.get()
    entry_hour = HourEntry.get()
    entry_title = TitleEntry.get()
    entry_content = ContentEntry.get()
    
    threading.Thread(target=check_time, args=(entry_date, entry_hour, entry_title, entry_content), daemon=True).start() 

Button = ct.CTkButton(master=Frame, text="Confirm", command=get_entry)
Button.pack(pady=10, padx=10)

Window.mainloop()
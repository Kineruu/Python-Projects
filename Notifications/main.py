from Notification import createWindow
from winotify import Notification, audio
from clipboard import paste
import customtkinter as ct
import threading
import datetime
import time
import json
import os

#Base path for the current file
BasePath = os.path.dirname(os.path.abspath(__file__))

#Creating a folder "NotificationsList" if it doesn't exists
NotificationsDir = os.path.join(BasePath, "NotificationsList")
if not os.path.exists(NotificationsDir):
    os.makedirs(NotificationsDir)

#Creating a file named Number.txt that stores Notification numbers if user doesn't change the file name (added soon)
NumberPath = os.path.join(BasePath, "Number.txt")
if not os.path.isfile(NumberPath):
    with open(NumberPath, "w") as f:
        f.write("2")

#Gets current day and hour
def GetCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

#Gets only current hour
def GetCurrentHour():
    now = datetime.datetime.now()
    CurrentHour = now.hour
    return CurrentHour

#Hour
Hour = GetCurrentHour()


#Setting up the main window
#Colors!!
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

#Main window settings
Window = ct.CTk()
Window.geometry("700x500")
Window.resizable(False, False)
Window.title("  Notification Program") 

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

#Label that says time
Label = ct.CTkLabel(master=Frame, text=GetCurrentTime()) 
Label.pack(pady=4)

#You enter your date here
DateEntry = ct.CTkEntry(master=Frame, placeholder_text="Date") 
DateEntry.pack(pady=4)

#You enter your... hour here!
HourEntry = ct.CTkEntry(master=Frame, placeholder_text="Hour") 
HourEntry.pack(pady=4)

#Bold white text in your notification at the top (I think it's max up to 256 characters otherwise it won't spawn the notification)
TitleEntry = ct.CTkEntry(master=Frame, placeholder_text="Title <=256 char")
TitleEntry.pack(pady=4)

#I think the most useful one, giving you more context later what you had in mind while creating a notification
ContentEntry = ct.CTkEntry(master=Frame, placeholder_text="Content <=256 char")
ContentEntry.pack(pady=4)

#If you don't want to write your date every single time you create a notification, there's a button next to the Entrybox to do that for you
def CurrentDate():
    now = datetime.datetime.now()
    NowDate = now.strftime("%d.%m.%y")
    DateEntry.delete(0, ct.END)
    DateEntry.insert(0, NowDate)

CurrentDateButton = ct.CTkButton(master=Frame, text="Current Date", command=CurrentDate, width=92) 
CurrentDateButton.place(x=325, y=40)

#Same thing as CurrentDate() but it's for hour
def CurrentHour(): 
    now = datetime.datetime.now()
    NowHour = now.strftime("%H:%M")
    HourEntry.delete(0, ct.END)
    HourEntry.insert(0, NowHour)

CurrentHourButton = ct.CTkButton(master=Frame, text="Current Hour", command=CurrentHour, width=92)
CurrentHourButton.place(x=325, y=77)

#Basically pasting what you have in your clipboard
def PasteTitleDef():
    UserPaste = paste()
    TitleEntry.delete(0, ct.END)
    TitleEntry.insert(0, UserPaste)

PasteTitle = ct.CTkButton(master=Frame, text="Paste title", command=PasteTitleDef, width=92) 
PasteTitle.place(x=325, y=112)

#Same as above
def PasteContentDef():
    UserPaste = paste()
    ContentEntry.delete(0, ct.END)
    ContentEntry.insert(0, UserPaste) 

PasteContent = ct.CTkButton(master=Frame, text="Paste content", command=PasteContentDef, width=88) 
PasteContent.place(x=325, y=148)

#Displays (not fully YET) your latest notification
def LatestNotification():
    with open(os.path.join(BasePath, "Number.txt"), "r") as f:
        NumberFile = int(f.read().strip())

    with open(os.path.join(NotificationsDir, f"Notification{NumberFile}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]
        Content = FileContent["Content"]
        Date = FileContent["Date"]
        Hour = FileContent["Hour"]

    #CreateWindow function is from Notification.py file
    createWindow(Number=int(NumberFile), Title=Title, Content=Content, Date=Date, Hour=Hour)

#Same as LatestNotification but -1
def PreviousNotification():
    with open(os.path.join(BasePath, "Number.txt"), "r") as f:
        NumberFile = int(f.read().strip())

    with open(os.path.join(NotificationsDir, f"Notification{NumberFile-1}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]
        Content = FileContent["Content"]
        Date = FileContent["Date"]
        Hour = FileContent["Hour"]

    createWindow(Number=int(NumberFile-1), Title=Title, Content=Content, Date=Date, Hour=Hour)

#Those two buttons have their titles (You gave them the name)
def GetTitleFromFiles():
    with open(os.path.join(BasePath, "Number.txt"), "r") as f:
        NumberFile = int(f.read().strip())

    with open(os.path.join(NotificationsDir, f"Notification{NumberFile}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]
    
    LatestNotificationButton.configure(text=(Title[:15] + "..." if len(Title) > 25 else Title))

    with open(os.path.join(NotificationsDir, f"Notification{NumberFile-1}.json"), "r") as f:
        FileContent = json.load(f)
        Title = FileContent["Title"]

    PreviousNotificationButton.configure(text=Title[:10] + "..." if len(Title) > 15 else Title)

LatestNotificationButton = ct.CTkButton(master=Frame, text=None, command=LatestNotification, width=60, height=35)
LatestNotificationButton.place(x=5, y=10)

PreviousNotificationButton = ct.CTkButton(master=Frame, text=None, command=PreviousNotification, width=40, height=35)
PreviousNotificationButton.place(x=15, y=50)

GetTitleFromFiles()

#Main notification function I guess?
def check_time(entry_date, entry_hour, entry_title, entry_content):
    while True:
        current_date, current_hour = GetCurrentTime()
        # If current date and hour is equal to the hour etc.
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

            jsonPath = os.path.join(NotificationsDir, f"Notification{Number}.json")
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
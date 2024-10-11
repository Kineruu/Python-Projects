from winotify import Notification, audio
from clipboard import paste

import customtkinter as ct
import datetime
import time
import threading
import os

def GetCurrentTime(): # Getting current date and hour, output should be like this: dd.mm.yyy HH:MM
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

def GetCurrentHour(): # Getting current hour without minutes
    now = datetime.datetime.now()
    CurrentHour = now.hour
    return CurrentHour

Hour = GetCurrentHour()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")


Window = ct.CTk() # Setting up the main window
Window.geometry("500x300") # Size of it
Window.resizable(False, False) # Not resizable

Window.title("              Notification Program") # The title, the text that appears at the top of the window, there are spaces because if it wouldn't be centered without them.

Frame = ct.CTkFrame(master=Window) # Creating the window itself
Frame.pack(fill="both", expand=True)

Label = ct.CTkLabel(master=Frame, text=GetCurrentTime()) # Date and hour at the top of the Frame
Label.pack(pady=4)

DateEntry = ct.CTkEntry(master=Frame, placeholder_text="Date") # Letting the user to put at what date you want the notification to be at. It requires the program to be in the background, if you shut down your device, the notification will NOT show up.
DateEntry.pack(pady=4)

HourEntry = ct.CTkEntry(master=Frame, placeholder_text="Hour") # Same goes for hours
HourEntry.pack(pady=4)

TitleEntry = ct.CTkEntry(master=Frame, placeholder_text="Title") # Self explanatory
TitleEntry.pack(pady=4)

ContentEntry = ct.CTkEntry(master=Frame, placeholder_text="Content") # Self explanatory
ContentEntry.pack(pady=4)

def CurrentDate(): # Getting current date, delete and insert are here because if we press the button it'll clear whatever is in the Entry box and will paste the current date
    now = datetime.datetime.now()
    NowDate = now.strftime("%d.%m.%y")
    DateEntry.delete(0, ct.END)
    DateEntry.insert(0, NowDate)

CurrentDateButton = ct.CTkButton(master=Frame, text="Current Date", command=CurrentDate, width=92) # Current Date button
CurrentDateButton.place(x=325, y=40)

def CurrentHour(): # Same thing for the hour
    now = datetime.datetime.now()
    NowHour = now.strftime("%H:%M")
    HourEntry.delete(0, ct.END)
    HourEntry.insert(0, NowHour)

CurrentHourButton = ct.CTkButton(master=Frame, text="Current Hour", command=CurrentHour, width=92) # Current Hour button
CurrentHourButton.place(x=325, y=77)

def PasteTitleDef(): # Self explanatory
    UserPaste = paste()
    TitleEntry.delete(0, ct.END)
    TitleEntry.insert(0, UserPaste)

PasteTitle = ct.CTkButton(master=Frame, text="Paste title", command=PasteTitleDef, width=92) # Paste Title button
PasteTitle.place(x=325, y=112)

def PasteContentDef(): # Self explanatory
    UserPaste = paste()
    ContentEntry.delete(0, ct.END)
    ContentEntry.insert(0, UserPaste) 

PasteContent = ct.CTkButton(master=Frame, text="Paste content", command=PasteContentDef, width=88) # Paste Content button
PasteContent.place(x=325, y=148)

#WarningLabel = ct.CTkLabel(master=Frame, text="If the entries boxes are empty, \nthe notification will NOT show up.") # Warning for people who think that putting empty entries will do something
#WarningLabel.place(x=90, y=221)

with open("C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\Number.txt") as f:
    NumberFile = int(f.read())

with open(f"C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\NotificationsList\\Notification{NumberFile}.txt", "r") as GetTitle:
    GetNotificationTitle = GetTitle.readline(1)     
    GetNotificationTitle = GetNotificationTitle[7:] 
    GetTitle.close()

def LatestNotification():
    os.system(f"C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\NotificationsList\\Notification{NumberFile}.txt")

def PreviousNotification():
    os.system(f"C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\NotificationsList\\Notification{NumberFile-1}.txt")

LatestNotificationButton = ct.CTkButton(master=Frame, text=f"{GetNotificationTitle}", command=LatestNotification, width=60, height=35)
LatestNotificationButton.place(x=5, y=10)

PreviousNotificationButton = ct.CTkButton(master=Frame, text=f"Notification{NumberFile-1}", command=PreviousNotification, width=40, height=35)
PreviousNotificationButton.place(x=15, y=50)


def check_time(entry_date, entry_hour, entry_title, entry_content): # Getting all requirements that winotify (The module/library that shows notification) needs
    while True: # Yes, it'll always run in the background as long as you have it opened and it'll check if it's correct date/hour to send the notification every 5 seconds
        current_date, current_hour = GetCurrentTime() # now.strftime("%d.%m.%y"), now.strftime("%H:%M")
        if current_date == entry_date and current_hour == entry_hour and entry_title != "" and entry_content != "": # Checking if all entries are filled and not empty
            Noti = Notification( # Self explanatory
                app_id="Notification program",
                title=entry_title,
                msg=entry_content,
                duration="short" # "Short" because it's long enough for everyone to read the notification content
            )
            with open("Number.txt", "r+") as f:
                Number = int(f.read().strip())
                Number += 1
                f.seek(0) 
                f.write(str(Number))
                f.truncate()
                with open(f"C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\NotificationsList\\Notification{Number}.txt", "w") as f:
                    f.write(f"TITLE: {entry_title}\nCONTENT: {entry_content}\nDATE: {entry_date}\nHOUR: {entry_hour}")
                    f.close()

            LatestNotificationButton.configure(text=f"Notification{Number}", command=lambda: os.system(f"C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\NotificationsList\\Notification{Number}.txt"))
            PreviousNotificationButton.configure(text=f"Notification{Number-1}", command=lambda: os.system(f"C:\\Users\\Me\\Desktop\\Programming-Projects\\Python-Projects\\NotificationsList\\Notification{Number-1}.txt"))

            Noti.set_audio(audio.Default, loop=False) # Audio for people who have system sounds enabled
            Noti.show()
            break
        else:
            pass
        time.sleep(5)

def get_entry(WhateverIsThis=None):
    entry_date = DateEntry.get() # Getting everything that is in the Entries and putting them into the notification.
    entry_hour = HourEntry.get()
    entry_title = TitleEntry.get()
    entry_content = ContentEntry.get()
    
    threading.Thread(target=check_time, args=(entry_date, entry_hour, entry_title, entry_content), daemon=True).start() 

Button = ct.CTkButton(master=Frame, text="Confirm", command=get_entry) # Confirm button, what else would you expect
Button.pack(pady=10, padx=10)

Window.mainloop()
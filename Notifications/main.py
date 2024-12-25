from utils.Notification import utilsNotifications
from utils.Settings import Settings
from utils.Titles import Titles
from utils.Paste import Paste
from utils.Time import Time

# https://www.youtube.com/watch?v=dQw4w9WgXcQ
# Really cool music to listen in the background

from winotify import Notification, audio
import customtkinter as ct
import importlib
import threading
import utils
import time
import json
import os

def reloadSettings():
    importlib.reload(utils.Settings)

#Initialize utilities and setup paths
notification = utilsNotifications()

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_PATH, "config.json"), "r") as f:
    config = json.load(f)

UTILS_DIR = os.path.join(BASE_PATH, config["UTILS_DIR"])
NOTIFICATIONS_DIR = os.path.join(BASE_PATH, config["NOTIFICATIONS_DIR"])
NUMBER_PATH = os.path.join(BASE_PATH, config["NUMBER_PATH"])

#Setting up the main window - Theme!!
ct.set_appearance_mode(config["THEME"])
ct.set_default_color_theme(config["COLOR_THEME"])

#Main window settings
Window = ct.CTk()
Window.iconbitmap(os.path.join(BASE_PATH, "utils//Icon.ico"))

RandomTitle = Titles()
TitlesFilePath = os.path.join(UTILS_DIR, "Titles.json")

if config["CUSTOMTITLES"] == "YES":
    Window.title(RandomTitle.randomTitle(TitlesFilePath)) 
else:
    Window.title("Notifications")

Window.grid_rowconfigure((0, 1, 2, 3, 4), weight=0) 
Window.grid_rowconfigure(0, weight=1)
Window.grid_columnconfigure(0, weight=1)  
Window.grid_columnconfigure(1, weight=7)

#Quite important code
def showMainFrame():
    for widget in Window.winfo_children():
        widget.pack_forget()
    MainFrame.pack(fill="both", expand=True)

MainFrame = ct.CTkFrame(master=Window)
MainFrame.grid(row=0, column=1, sticky="nsew")
MainFrame.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
MainFrame.grid_columnconfigure((0, 1), weight=1)

#Label that says time
Label = ct.CTkLabel(master=MainFrame, text=Time.GetCurrentTime())
Label.grid(row=0, column=1, columnspan=2, pady=(10, 5), sticky="n")

def UpdateTimeEveryMinute(Label):
    Time.UpdateTime(Label)
    Label.after(60000, UpdateTimeEveryMinute, Label)

UpdateTimeEveryMinute(Label=Label)

#You enter your date here
DateEntry = ct.CTkEntry(master=MainFrame, placeholder_text="Date") 
DateEntry.grid(row=1, column=1, padx=5, pady=5, sticky="e")

#You enter your... hour here!
HourEntry = ct.CTkEntry(master=MainFrame, placeholder_text="Hour") 
HourEntry.grid(row=2, column=1, padx=5, pady=5, sticky="e")

#Bold white text in your notification at the top (I think it's max up to 256 characters otherwise it won't spawn the notification)
TitleEntry = ct.CTkEntry(master=MainFrame, placeholder_text="Title <=256 char")
TitleEntry.grid(row=3, column=1, padx=5, pady=5, sticky="e")

#I think the most useful one, giving you more context later what you had in mind while creating a notification
ContentEntry = ct.CTkEntry(master=MainFrame, placeholder_text="Content <=256 char")
ContentEntry.grid(row=4, column=1, padx=5, pady=5, sticky="e")

#If you don't want to write your date every single time you create a notification, 
#there's a button next to the Entrybox to do that for you
CurrentDateButton = ct.CTkButton(
    master=MainFrame, 
    text="Current Date", 
    command=lambda: Time.SetCurrentDate(DateEntry), 
    width=config["BUTTONSWIDTH"],
    fg_color=config["BUTTONSCOLOR"]
)
CurrentDateButton.grid(row=1, column=2, padx=5, pady=5, sticky="w")

#Same thing as CurrentDateButton but it's for hour
CurrentHourButton = ct.CTkButton(
    master=MainFrame, 
    text="Current Hour", 
    command=lambda: Time.SetCurrentHour(HourEntry), 
    width=config["BUTTONSWIDTH"],
    fg_color=config["BUTTONSCOLOR"]
)
CurrentHourButton.grid(row=2, column=2, padx=5, pady=5, sticky="w")

#Basically pasting what you have in your clipboard
PasteTitle = ct.CTkButton(
    master=MainFrame, 
    text="Paste title", 
    command=lambda: Paste.PasteTitle(TitleEntry),
    width=config["BUTTONSWIDTH"],
    fg_color=config["BUTTONSCOLOR"]
) 
PasteTitle.grid(row=3, column=2, padx=5, pady=5, sticky="w")

#Same as above
PasteContent = ct.CTkButton(
    master=MainFrame, 
    text="Paste content", 
    command=lambda: Paste.PasteContent(ContentEntry), 
    width=config["BUTTONSWIDTH"],
    fg_color=config["BUTTONSCOLOR"]
) 
PasteContent.grid(row=4, column=2, padx=5, pady=5, sticky="w")

SettingsButton = ct.CTkButton(
    master=MainFrame, 
    text="⚙️", 
    command=lambda: 
    Settings.loadWindow(Window, MainFrame, reloadSettings),
    width=config["BUTTONSWIDTH"],
    fg_color=config["BUTTONSCOLOR"]
)
SettingsButton.grid(row=0, column=3, columnspan=2, pady=5, padx=5, sticky="")

#!LEFT FRAME

with open(os.path.join(NOTIFICATIONS_DIR, "Notifications.json"), "r") as f:
    data = json.load(f)

SidebarFrame = ct.CTkScrollableFrame(master=Window, width=config["LEFTFRAMESIZE"])
SidebarFrame.grid(row=0, column=0, rowspan=6, sticky="nsw")

SidebarFrame.grid_rowconfigure(0, weight=0)
SidebarFrame.grid_rowconfigure(1, weight=0)
SidebarFrame.grid_columnconfigure(0, weight=1)

Label = ct.CTkLabel(
    master=SidebarFrame,
    text=""
)

for idx, Noti in enumerate(data["ACTIVE"]):
    btn = ct.CTkButton(
        master=SidebarFrame,
        text=data["ACTIVE"][Noti]["TITLE"],
        command=lambda noti=Noti: print(noti)
    )
    btn.grid(row=idx + 1, column=0, sticky="ew", pady=2)

ActiveList = ct.CTkLabel(
    master=SidebarFrame,
    text="List",
    width=config["NOTIWIDTH"]
)
ActiveList.grid(row=0, column=0, pady=5, padx=5, sticky="ew")

InactiveList = ct.CTkLabel(
    master=SidebarFrame,
    text="INACTIVE",
    width=config["NOTIWIDTH"]
)
InactiveList.grid(row=idx + 2, column=0, pady=5, padx=5, sticky="ew")

#I don't like this part for some reason
#Main notification function I guess?
def check_time(entry_date, entry_hour, entry_title, entry_content):
    while True:
        current_date, current_hour = Time.GetCurrentTime()
        # If current date and hour is equal to the hour etc.
        if current_date == entry_date and current_hour == entry_hour and entry_title != "" and entry_content != "":
            Noti = Notification( # Self explanatory
                app_id="Notification program",
                title=entry_title,
                msg=entry_content,
                duration="short"
            )

            with open(os.path.join(NOTIFICATIONS_DIR, "Number.txt"), "r+") as f:
                Number = int(f.read().strip())
                Number += 1
                f.seek(0) 
                f.write(str(Number))
                f.truncate()

            NotificationJSON = {
                "DATE": entry_date,
                "HOUR": entry_hour,
                "TITLE": entry_title,
                "CONTENT": entry_content
            }

            jsonPath = os.path.join(NOTIFICATIONS_DIR, "Notifications.json")
            with open(jsonPath, "r") as f:
                data = json.load(f)

            NewNotificationName = f"Notification{Number}" #Is this even a good way to write my json? Who knows
            data["ACTIVE"][NewNotificationName] = NotificationJSON

            with open(jsonPath, "w") as f:
                json.dump(data, f, indent=4)

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

    threading.Thread(
        target=check_time, 
        args=(entry_date, entry_hour, entry_title, entry_content), 
        daemon=True
    ).start() 

Button = ct.CTkButton(
    master=MainFrame, 
    text="Confirm", 
    command=get_entry, 
    width=config["BUTTONSWIDTH"],
    fg_color=config["BUTTONSCOLOR"]
)
Button.grid(row=5, column=1, columnspan=2, pady=5, sticky="")


Window.mainloop()

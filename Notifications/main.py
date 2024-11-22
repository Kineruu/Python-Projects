from utils.Notification import utilsNotification
from utils.History import History
from utils.Time import Time
from utils.Paste import Paste

from winotify import Notification, audio
from clipboard import paste
import customtkinter as ct
import threading
import config
import time
import json
import os

#Initialize utilities and setup paths
notification = utilsNotification()
history = History()
BasePath = os.path.dirname(os.path.abspath(__file__))
NotificationsDir = config.NOTIFICATIONS_DIR
NumberPath = config.NUMBER_PATH
UtilsDir = config.UTILS_DIR

def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def ensure_file_exists(path, default_content="2"):
    if not os.path.isfile(path):
        with open(path, "w") as f:
            f.write(default_content)

# Ensure necessary directories and files are in place
ensure_dir_exists(NotificationsDir)
ensure_file_exists(NumberPath)
ensure_dir_exists(UtilsDir)

#Setting up the main window - Theme!!
ct.set_appearance_mode(config.THEME)
ct.set_default_color_theme(config.COLOR_THEME)

#Main window settings
Window = ct.CTk()
Window.geometry(f"{config.WIDTH}x{config.HEIGHT}")
Window.title(config.TITLE) 
Window.grid_rowconfigure((0, 1, 2, 3, 4), weight=0) 
Window.grid_rowconfigure(5, weight=1) 
Window.grid_columnconfigure(0, weight=1)  
Window.grid_columnconfigure(1, weight=0)

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)
Frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
Frame.grid_columnconfigure((0, 1), weight=1)

#Label that says time
Label = ct.CTkLabel(master=Frame, text=Time.GetCurrentTime())
Label.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="n")

def UpdateTimeEveryMinute(Label):
    Time.UpdateTime(Label)
    Label.after(60000, UpdateTimeEveryMinute, Label)

UpdateTimeEveryMinute(Label=Label)

#You enter your date here
DateEntry = ct.CTkEntry(master=Frame, placeholder_text="Date") 
DateEntry.grid(row=1, column=0, padx=10, pady=5, sticky="e")

#You enter your... hour here!
HourEntry = ct.CTkEntry(master=Frame, placeholder_text="Hour") 
HourEntry.grid(row=2, column=0, padx=10, pady=5, sticky="e")

#Bold white text in your notification at the top (I think it's max up to 256 characters otherwise it won't spawn the notification)
TitleEntry = ct.CTkEntry(master=Frame, placeholder_text="Title <=256 char")
TitleEntry.grid(row=3, column=0, padx=10, pady=5, sticky="e")

#I think the most useful one, giving you more context later what you had in mind while creating a notification
ContentEntry = ct.CTkEntry(master=Frame, placeholder_text="Content <=256 char")
ContentEntry.grid(row=4, column=0, padx=10, pady=5, sticky="e")

#If you don't want to write your date every single time you create a notification, 
#there's a button next to the Entrybox to do that for you
CurrentDateButton = ct.CTkButton(master=Frame, text="Current Date", command=lambda: Time.SetCurrentDate(DateEntry), width=92) 
CurrentDateButton.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#Same thing as CurrentDateButton but it's for hour
CurrentHourButton = ct.CTkButton(master=Frame, text="Current Hour", command=lambda: Time.SetCurrentHour(HourEntry), width=92)
CurrentHourButton.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#Basically pasting what you have in your clipboard
PasteTitle = ct.CTkButton(master=Frame, text="Paste title", command=lambda: Paste.PasteTitle(TitleEntry), width=92) 
PasteTitle.grid(row=3, column=1, padx=10, pady=5, sticky="w")

#Same as above
PasteContent = ct.CTkButton(master=Frame, text="Paste content", command=lambda: Paste.PasteContent(ContentEntry), width=88) 
PasteContent.grid(row=4, column=1, padx=10, pady=5, sticky="w")

LatestNotificationButton = ct.CTkButton(master=Frame, text=None, command=lambda: history.LatestNotification(), width=60, height=35)
LatestNotificationButton.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="w")

PreviousNotificationButton = ct.CTkButton(master=Frame, text=None, command=lambda: history.PreviousNotification(), width=40, height=35)
PreviousNotificationButton.grid(row=1, column=0, padx=(5, 10), pady=(10, 5), sticky="w")

history.GetTitleFromFiles(LatestNotificationButton, PreviousNotificationButton)

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

            with open(os.path.join(NotificationsDir, "Number.txt"), "r+") as f:
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

            history.GetTitleFromFiles(LatestNotificationButton, PreviousNotificationButton)

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
Button.grid(row=5, column=0, columnspan=2, pady=(20, 10), sticky="")

Window.mainloop()
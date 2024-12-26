from utils.Notification import utilsNotifications
from utils.Settings import Settings
from utils.Titles import Titles
from utils.Paste import Paste
from utils.Time import Time

from winotify import Notification, audio
import customtkinter as ct
import importlib
import threading
import datetime
import utils
import time
import json
import os

class NotificationApp:
    def __init__(self):
        # Initialize utilities and setup paths
        self.notification = utilsNotifications()
        self.BASE_PATH = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(self.BASE_PATH, "config.json"), "r") as f:
            self.config = json.load(f)

        self.UTILS_DIR = os.path.join(self.BASE_PATH, self.config["UTILS_DIR"])
        self.NOTIFICATIONS_DIR = os.path.join(self.BASE_PATH, self.config["NOTIFICATIONS_DIR"])
        self.NUMBER_PATH = os.path.join(self.BASE_PATH, self.config["NUMBER_PATH"])

        # Setting up the main window theme
        ct.set_appearance_mode(self.config["THEME"])
        ct.set_default_color_theme(self.config["COLOR_THEME"])

        # Main window settings
        self.Window = ct.CTk()
        self.Window.iconbitmap(os.path.join(self.BASE_PATH, "utils//Icon.ico"))

        self.RandomTitle = Titles()
        self.TitlesFilePath = os.path.join(self.UTILS_DIR, "Titles.json")

        if self.config["CUSTOMTITLES"] == "YES":
            self.Window.title(self.RandomTitle.randomTitle(self.TitlesFilePath))
        else:
            self.Window.title("Notifications")

        self.Window.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.Window.grid_rowconfigure(0, weight=1)
        self.Window.grid_columnconfigure(0, weight=1)
        self.Window.grid_columnconfigure(1, weight=7)

        # Main frame setup
        self.MainFrame = ct.CTkFrame(master=self.Window)
        self.MainFrame.grid(row=0, column=1, sticky="nsew")
        self.MainFrame.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.MainFrame.grid_columnconfigure((0, 1), weight=1)

        # Label that displays the current time
        self.Label = ct.CTkLabel(master=self.MainFrame, text=Time.GetCurrentTime())
        self.Label.grid(row=0, column=1, columnspan=2, pady=(10, 5), sticky="n")
        self.UpdateTimeEveryMinute(self.Label)

        # Entry fields for date, hour, title, and content
        self.DateEntry = ct.CTkEntry(master=self.MainFrame, placeholder_text="Date")
        self.DateEntry.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        self.HourEntry = ct.CTkEntry(master=self.MainFrame, placeholder_text="Hour")
        self.HourEntry.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        self.TitleEntry = ct.CTkEntry(master=self.MainFrame, placeholder_text="Title <=256 char")
        self.TitleEntry.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        self.ContentEntry = ct.CTkEntry(master=self.MainFrame, placeholder_text="Content <=256 char")
        self.ContentEntry.grid(row=4, column=1, padx=5, pady=5, sticky="e")

        # Buttons for setting current date and hour, and pasting title and content
        self.CurrentDateButton = ct.CTkButton(
            master=self.MainFrame,
            text="Current Date",
            command=lambda: Time.SetCurrentDate(self.DateEntry),
            width=self.config["BUTTONSWIDTH"],
            fg_color=self.config["BUTTONSCOLOR"]
        )
        self.CurrentDateButton.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.CurrentHourButton = ct.CTkButton(
            master=self.MainFrame,
            text="Current Hour",
            command=lambda: Time.SetCurrentHour(self.HourEntry),
            width=self.config["BUTTONSWIDTH"],
            fg_color=self.config["BUTTONSCOLOR"]
        )
        self.CurrentHourButton.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        self.PasteTitle = ct.CTkButton(
            master=self.MainFrame,
            text="Paste title",
            command=lambda: Paste.PasteTitle(self.TitleEntry),
            width=self.config["BUTTONSWIDTH"],
            fg_color=self.config["BUTTONSCOLOR"]
        )
        self.PasteTitle.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        self.PasteContent = ct.CTkButton(
            master=self.MainFrame,
            text="Paste content",
            command=lambda: Paste.PasteContent(self.ContentEntry),
            width=self.config["BUTTONSWIDTH"],
            fg_color=self.config["BUTTONSCOLOR"]
        )
        self.PasteContent.grid(row=4, column=2, padx=5, pady=5, sticky="w")

        self.SettingsButton = ct.CTkButton(
            master=self.MainFrame,
            text="⚙️",
            command=lambda: Settings.loadWindow(self.Window, self.MainFrame),
            width=self.config["BUTTONSWIDTH"],
            fg_color=self.config["BUTTONSCOLOR"]
        )
        self.SettingsButton.grid(row=0, column=3, columnspan=2, pady=5, padx=5, sticky="")

        # Load notifications data
        with open(os.path.join(self.NOTIFICATIONS_DIR, "Notifications.json"), "r") as f:
            self.data = json.load(f)

        # Sidebar frame setup
        self.SidebarFrame = ct.CTkScrollableFrame(master=self.Window, width=self.config["LEFTFRAMESIZE"])
        self.SidebarFrame.grid(row=0, column=0, rowspan=6, sticky="nsw")

        self.SidebarFrame.grid_rowconfigure(0, weight=0)
        self.SidebarFrame.grid_rowconfigure(1, weight=0)
        self.SidebarFrame.grid_columnconfigure(0, weight=1)

        self.Label = ct.CTkLabel(master=self.SidebarFrame, text="List")
        self.Label.grid(row=0, column=0, pady=5)

        # Confirm button to add a new notification
        self.Button = ct.CTkButton(
            master=self.MainFrame,
            text="Confirm",
            command=self.get_entry,
            width=self.config["BUTTONSWIDTH"],
            fg_color=self.config["BUTTONSCOLOR"]
        )
        self.Button.grid(row=5, column=1, columnspan=2, pady=5, sticky="")

        # Check for active notifications
        self.checkIfActive()
        self.Window.mainloop()

    def reloadSettings(self):
        importlib.reload(utils.Settings)

    def UpdateTimeEveryMinute(self, Label):
        # Update the time label every minute
        Time.UpdateTime(Label)
        Label.after(60000, self.UpdateTimeEveryMinute, Label)

    def isValidDatetime(self, date_str, hour_str):
        # Check if the date and hour strings are in the correct format
        try:
            datetime.datetime.strptime(f"{date_str} {hour_str}", "%d.%m.%y %H:%M")
            return True
        except ValueError:
            return False

    def checkIfActive(self):
        # Check and display active and inactive notifications
        for widget in self.SidebarFrame.winfo_children():
            widget.destroy()
        Label = ct.CTkLabel(master=self.SidebarFrame, text="List")
        Label.grid(row=0, column=0, pady=5)

        for idx, noti_key in enumerate(self.data["ACTIVE"]):
            notification = self.data["ACTIVE"][noti_key]
            if self.isValidDatetime(notification["DATE"], notification["HOUR"]):
                past_unix_time = Time.GetPastUnixTime(notification["DATE"], notification["HOUR"])
                current_unix_time = Time.GetCurrentUnixTime()
                fg_color = self.config["ACTIVECOLOR"] if past_unix_time > current_unix_time else self.config["INACTIVECOLOR"]
                btn = ct.CTkButton(
                    master=self.SidebarFrame,
                    text=notification["TITLE"],
                    command=lambda noti=noti_key: print(noti),
                    fg_color=fg_color
                )
                btn.grid(row=idx + 1, column=0, sticky="ew", pady=2)

        for idx, noti_key in enumerate(self.data["INACTIVE"]):
            notification = self.data["INACTIVE"][noti_key]
            if self.isValidDatetime(notification["DATE"], notification["HOUR"]):
                btn = ct.CTkButton(
                    master=self.SidebarFrame,
                    text=notification["TITLE"],
                    command=lambda noti=noti_key: print(noti),
                    fg_color=self.config["INACTIVECOLOR"]
                )
                btn.grid(row=idx + 1, column=0, sticky="ew", pady=2)

    def RefreshSidebar(self):
        # Refresh the sidebar to display updated notifications
        self.SidebarFrame.after(100, self.checkIfActive)

    def check_time(self, entry_date, entry_hour, entry_title, entry_content):
        # Check if the current time matches the notification time
        while True:
            current_date, current_hour = Time.GetCurrentTime()
            if current_date == entry_date and current_hour == entry_hour and entry_title != "" and entry_content != "":
                Noti = Notification(
                    app_id="Notification program",
                    title=entry_title,
                    msg=entry_content,
                    duration="short"
                )

                with open(os.path.join(self.NOTIFICATIONS_DIR, "Number.txt"), "r+") as f:
                    Number = int(f.read().strip())
                    Number += 1
                    f.seek(0)
                    f.write(str(Number))
                    f.truncate()

                NotificationJSON = {
                    "DATE": entry_date,
                    "HOUR": entry_hour,
                    "TITLE": entry_title,
                    "CONTENT": entry_content,
                    "UnixTime": Time.GetPastUnixTime(entry_date, entry_hour)
                }

                jsonPath = os.path.join(self.NOTIFICATIONS_DIR, "Notifications.json")
                with open(jsonPath, "r") as f:
                    self.data = json.load(f)

                NewNotificationName = f"Notification{Number}"
                self.data["ACTIVE"][NewNotificationName] = NotificationJSON

                with open(jsonPath, "w") as f:
                    json.dump(self.data, f, indent=4)

                Noti.set_audio(audio.Default, loop=False)
                Noti.show()
                self.RefreshSidebar()
                break
            else:
                pass
            time.sleep(5)

    def get_entry(self):
        # Get the entry data and start a thread to check the notification time
        entry_date = self.DateEntry.get()
        entry_hour = self.HourEntry.get()
        entry_title = self.TitleEntry.get()
        entry_content = self.ContentEntry.get()

        threading.Thread(
            target=self.check_time,
            args=(entry_date, entry_hour, entry_title, entry_content),
            daemon=True
        ).start()
        self.RefreshSidebar()

if __name__ == "__main__":
    app = NotificationApp()

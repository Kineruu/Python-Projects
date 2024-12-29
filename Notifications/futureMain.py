from utils.Notification import utilsNotifications
from utils.Settings import Settings
from utils.Titles import Titles
from utils.Paste import Paste
from utils.Time import Time

from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore, PySide6.QtGui, PySide6.QtWidgets

from winotify import Notification, audio
from clipboard import paste
import threading
import random
import utils
import time
import json
import sys
import os

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(self.BASE_PATH, "config.json"), "r") as f:
            self.config = json.load(f)

        self.UTILS_DIR = os.path.join(self.BASE_PATH, self.config["UTILS_DIR"])
        self.NOTIFICATIONS_DIR = os.path.join(self.BASE_PATH, self.config["NOTIFICATIONS_DIR"])
        self.NUMBER_PATH = os.path.join(self.BASE_PATH, self.config["NUMBER_PATH"])
        self.TitlesFilePath = os.path.join(self.UTILS_DIR, "Titles.json")
    
    def customTitles(self):
        if self.config["CUSTOMTITLES"] == "YES": # Why isn't that working
            Titles.randomTitle(self.TitlesFilePath)
        else:
            return "Notifications"

    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText(str(Time.GetCurrentTime()[0] + " | " + Time.GetCurrentTime()[1]))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.date_entry = QtWidgets.QLineEdit(self)
        self.date_entry.setPlaceholderText("Date")
        self.date_entry.setFixedSize(125, 35)

        self.date_button = QtWidgets.QPushButton(self)
        self.date_button.setText("Today's date")
        self.date_button.clicked.connect(self.TodayDate)
        self.date_button.setFixedSize(125, 35)

        self.hour_entry = QtWidgets.QLineEdit(self)
        self.hour_entry.setPlaceholderText("Hour")
        self.hour_entry.setFixedSize(125, 35)

        self.hour_button = QtWidgets.QPushButton(self)
        self.hour_button.setText("Current hour")
        self.hour_button.clicked.connect(self.CurrentHour)
        self.hour_button.setFixedSize(125, 35)

        self.title_entry = QtWidgets.QLineEdit(self)
        self.title_entry.setPlaceholderText("Title")
        self.title_entry.setFixedSize(125, 35)

        self.title_button = QtWidgets.QPushButton(self)
        self.title_button.setText("Paste")
        self.title_button.clicked.connect(self.PasteTitle)
        self.title_button.setFixedSize(125, 35)

        self.content_entry = QtWidgets.QLineEdit(self)
        self.content_entry.setPlaceholderText("Content")
        self.content_entry.setFixedSize(125, 35)

        self.content_button = QtWidgets.QPushButton(self)
        self.content_button.setText("Paste")
        self.content_button.clicked.connect(self.PasteContent)
        self.content_button.setFixedSize(125, 35)

        self.confirm_button = QtWidgets.QPushButton(self)
        self.confirm_button.setText("Confirm")
        self.confirm_button.clicked.connect(self.sendNotification)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.settings_button = QtWidgets.QPushButton(self)
        self.settings_button.setText("Settings")
        self.settings_button.setFixedSize(125, 35)
        #self.settings_button.clicked.connect(self.settings)
        #self.settings_button.setFixedSize(125, 35)

        # Create layouts and add widgets
        self.layout = QtWidgets.QVBoxLayout(self)
        #self.layout.addStretch()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.settings_button)
        self.layout.addLayout(self.create_hbox_layout(self.date_entry, self.date_button))
        self.layout.addLayout(self.create_hbox_layout(self.hour_entry, self.hour_button))
        self.layout.addLayout(self.create_hbox_layout(self.title_entry, self.title_button))
        self.layout.addLayout(self.create_hbox_layout(self.content_entry, self.content_button))
        self.layout.addWidget(self.confirm_button)

    def confirm(self):
        print("Hello")

    def TodayDate(self):
        self.date_entry.setText(Time.GetCurrentTime()[0])
    
    def CurrentHour(self):
        self.hour_entry.setText(Time.GetCurrentTime()[1])

    def PasteTitle(self):
        self.title_entry.setText(paste())
    
    def PasteContent(self):
        self.content_entry.setText(paste())

    def create_hbox_layout(self, widget1, widget2):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        return layout

    def sendNotification(self):
        while True:
            date = self.date_entry.text()
            hour = self.hour_entry.text()
            title = self.title_entry.text()
            content = self.content_entry.text()
            if date == "" or hour == "" or title == "" or content == "":
                print("Please fill in all the fields")
                return
            
            # Rewrite that later so I can have the number in the json file
            with open(os.path.join(self.NOTIFICATIONS_DIR, "Number.txt"), "r+") as f:
                Number = int(f.read().strip())
                Number += 1
                f.seek(0)
                f.write(str(Number))
                f.truncate()

                NotificationJSON = {
                    "DATE": date,
                    "HOUR": hour,
                    "TITLE": title,
                    "CONTENT": content,
                    "UnixTime": Time.GetPastUnixTime(date, hour)
                }

                Noti = Notification(
                    app_id="Notification program",
                    title=title,
                    msg=content,
                    duration="short"
                )


                jsonPath = os.path.join(self.NOTIFICATIONS_DIR, "Notifications.json")
                with open(jsonPath, "r") as f:
                    self.data = json.load(f)

                NewNotificationName = f"Notification{Number}"
                self.data["Notifications"][NewNotificationName] = NotificationJSON

                with open(jsonPath, "w") as f:
                    json.dump(self.data, f, indent=4)

                Noti.set_audio(audio.Default, loop=False)
                Noti.show()
                break
        else:
            pass
        time.sleep(2) # Replace this with something else later

    def checkTime(self):
        date = self.date_entry.text()
        hour = self.hour_entry.text()
        title = self.title_entry.text()
        content = self.content_entry.text()

        if date == "" or hour == "" or title == "" or content == "":
            print("Please fill in all the fields")
            return

        def timeChecker():
            while True:
                current_date, current_hour = Time.GetCurrentTime()
                if current_date == date and current_hour == hour:
                    self.sendNotification(date, hour, title, content)
                    break
                time.sleep(5)

        threading.Thread(
            target=timeChecker,
            daemon=True
        ).start()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    with open(os.path.join(widget.BASE_PATH, "style.css"), "r") as f:
        app.setStyleSheet(f.read())

    #widget.resize(widget.config["WIDTH"], widget.config["HEIGHT"])
    iconPath = os.path.join(widget.BASE_PATH, "utils/Icon.ico")
    widget.setWindowIcon(QtGui.QIcon(iconPath))
    widget.setWindowTitle(widget.customTitles())
    widget.show()

    widget.sendNotification()

    sys.exit(app.exec())
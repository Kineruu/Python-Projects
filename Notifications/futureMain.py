from utils.Notification import utilsNotifications
from utils.Settings import Settings
from utils.Titles import Titles
from utils.Paste import Paste
from utils.Time import Time

from PySide6 import QtCore, QtWidgets
import PySide6.QtCore, PySide6.QtGui, PySide6.QtWidgets

import threading
import random
import utils
import time
import json
import sys
import os

# https://www.youtube.com/watch?v=dQw4w9WgXcQ
# Really cool music to listen in the background

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_PATH, "config.json"), "r") as f:
    config = json.load(f)

UTILS_DIR = os.path.join(BASE_PATH, config["UTILS_DIR"])
NOTIFICATIONS_DIR = os.path.join(BASE_PATH, config["NOTIFICATIONS_DIR"])
NUMBER_PATH = os.path.join(BASE_PATH, config["NUMBER_PATH"])

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        #                          x, y, width, height
        #self.DateEntry.setGeometry(10, 10, 125, 35)

        self.Label = QtWidgets.QLabel(self)
        self.Label.setText(str(Time.GetCurrentTime()))
        self.Label.setFixedSize(125, 35)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)

        self.DateEntry = QtWidgets.QLineEdit(self)
        self.DateEntry.setPlaceholderText("Enter the date")
        self.DateEntry.setFixedSize(125, 35)

        self.DateButton = QtWidgets.QPushButton(self)
        self.DateButton.setText("Enter")
        self.DateButton.setFixedSize(125, 35)


        self.HourEntry = QtWidgets.QLineEdit(self)
        self.HourEntry.setPlaceholderText("Enter the hour")
        self.HourEntry.setFixedSize(125, 35)

        self.HourButton = QtWidgets.QPushButton(self)
        self.HourButton.setText("Enter")
        self.HourButton.setFixedSize(125, 35)
        

        self.TitleEntry = QtWidgets.QLineEdit(self)
        self.TitleEntry.setPlaceholderText("Enter the title")
        self.TitleEntry.setFixedSize(125, 35)

        self.TitleButton = QtWidgets.QPushButton(self)
        self.TitleButton.setText("Enter")
        self.TitleButton.setFixedSize(125, 35)


        self.ContentEntry = QtWidgets.QLineEdit(self)
        self.ContentEntry.setPlaceholderText("Enter the content")
        self.ContentEntry.setFixedSize(125, 35)

        self.ContentButton = QtWidgets.QPushButton(self)
        self.ContentButton.setText("Enter")
        self.ContentButton.setFixedSize(125, 35)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.dateLayout = QtWidgets.QHBoxLayout()
        self.dateLayout.addWidget(self.DateEntry)
        self.dateLayout.addWidget(self.DateButton)

        self.hourLayout = QtWidgets.QHBoxLayout()
        self.hourLayout.addWidget(self.HourEntry)
        self.hourLayout.addWidget(self.HourButton)

        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.addWidget(self.TitleEntry)
        self.titleLayout.addWidget(self.TitleButton)

        self.contentLayout = QtWidgets.QHBoxLayout()
        self.contentLayout.addWidget(self.ContentEntry)
        self.contentLayout.addWidget(self.ContentButton)

        self.layout.addWidget(self.Label)
        self.layout.addLayout(self.dateLayout)
        self.layout.addLayout(self.hourLayout)
        self.layout.addLayout(self.titleLayout)
        self.layout.addLayout(self.contentLayout)
        #self.layout.addWidget(self.text)
        #self.layout.addWidget(self.button)

        #self.button.clicked.connect(self.magic)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    with open(os.path.join(BASE_PATH, "style.css"), "r") as f:
        app.setStyleSheet(f.read())

    widget = MyWidget()
    widget.resize(config["WIDTH"], config["HEIGHT"])
    iconPath = os.path.join(BASE_PATH, "utils//Icon.ico")
    widget.setWindowIcon(PySide6.QtGui.QIcon(iconPath))
    widget.setWindowTitle("Notifications")

    widget.show()

    sys.exit(app.exec())
    
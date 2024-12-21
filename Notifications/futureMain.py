from utils.Notification import utilsNotifications
from utils.Settings import Settings
from utils.Titles import Titles
from utils.Paste import Paste
from utils.Time import Time

from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore, PySide6.QtGui, PySide6.QtWidgets

import importlib
import threading
import random
import utils
import time
import json
import sys
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_PATH, "config.json"), "r") as f:
    config = json.load(f)

UTILS_DIR = os.path.join(BASE_PATH, config["UTILS_DIR"])
NOTIFICATIONS_DIR = os.path.join(BASE_PATH, config["NOTIFICATIONS_DIR"])
NUMBER_PATH = os.path.join(BASE_PATH, config["NUMBER_PATH"])

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText(str(Time.GetCurrentTime()))
        self.label.setFixedSize(125, 35)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.date_entry = QtWidgets.QLineEdit(self)
        self.date_entry.setPlaceholderText("Enter the date")
        self.date_entry.setFixedSize(125, 35)

        self.date_button = QtWidgets.QPushButton(self)
        self.date_button.setText("Enter")
        self.date_button.setFixedSize(125, 35)

        self.hour_entry = QtWidgets.QLineEdit(self)
        self.hour_entry.setPlaceholderText("Enter the hour")
        self.hour_entry.setFixedSize(125, 35)

        self.hour_button = QtWidgets.QPushButton(self)
        self.hour_button.setText("Enter")
        self.hour_button.setFixedSize(125, 35)

        self.title_entry = QtWidgets.QLineEdit(self)
        self.title_entry.setPlaceholderText("Enter the title")
        self.title_entry.setFixedSize(125, 35)

        self.title_button = QtWidgets.QPushButton(self)
        self.title_button.setText("Enter")
        self.title_button.setFixedSize(125, 35)

        self.content_entry = QtWidgets.QLineEdit(self)
        self.content_entry.setPlaceholderText("Enter the content")
        self.content_entry.setFixedSize(125, 35)

        self.content_button = QtWidgets.QPushButton(self)
        self.content_button.setText("Enter")
        self.content_button.setFixedSize(125, 35)

        # Create layouts and add widgets
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.label)
        self.layout.addLayout(self.create_hbox_layout(self.date_entry, self.date_button))
        self.layout.addLayout(self.create_hbox_layout(self.hour_entry, self.hour_button))
        self.layout.addLayout(self.create_hbox_layout(self.title_entry, self.title_button))
        self.layout.addLayout(self.create_hbox_layout(self.content_entry, self.content_button))

    def create_hbox_layout(self, widget1, widget2):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        return layout

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    with open(os.path.join(BASE_PATH, "style.css"), "r") as f:
        app.setStyleSheet(f.read())

    widget = MyWidget()
    widget.resize(config["WIDTH"], config["HEIGHT"])
    icon_path = os.path.join(BASE_PATH, "utils/Icon.ico")
    widget.setWindowIcon(QtGui.QIcon(icon_path))
    widget.setWindowTitle("Notifications")
    widget.show()

    sys.exit(app.exec())
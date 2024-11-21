import os

#Main file path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

#Other useful paths
NOTIFICATIONS_DIR = os.path.join(BASE_PATH, "NotificationsList")
NUMBER_PATH = os.path.join(NOTIFICATIONS_DIR, "Number.txt")
UTILS_DIR = os.path.join(BASE_PATH, "utils")

#Window stuff
THEME = "dark"
COLOR_THEME = "dark-blue"
WIDTH = 700
HEIGHT = 400
BUTTONS_WIDTH = 100

#Notification settings
NOTIFICATION_AUDIO = "default"
TITLE = "Notification program"

#How often should the program check the time (seconds)
TIME_CHECK = 5

#Placeholders
TITLE_PLACEHOLDER = "No title"
CONTENT_PLACEHOLDER = "No content"

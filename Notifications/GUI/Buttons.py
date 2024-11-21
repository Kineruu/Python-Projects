from utils.Notification import utilsNotification

import customtkinter as ct
import config
import os

class Buttons:
    def __init__(self):
        pass

    def notificationButtons(self, left_frame):
        notification = utilsNotification()
        notification_files = [
            f for f in os.listdir(config.NOTIFICATIONS_DIR)
            if f.startswith("Notification") and f.endswith(".json")
        ]
        
        for idx, file_name in enumerate(sorted(notification_files)):
            notification_number = int(file_name.replace("Notification", "").replace(".json", ""))
            button = ct.CTkButton(
                master=left_frame,
                text=f"Notification {notification_number}",
                width=130,
                command=lambda num=notification_number: notification.openNotification(num)
            )
            button.grid(row=idx, column=0, padx=5, pady=5)
import customtkinter as ct
import json
import os

BasePath = os.path.dirname(os.path.abspath(__file__))


class utilsNotifications:
    def __init__(self):
        pass

    def GetNotificationDir(self):
        """Get current notification directory"""
        BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        NotificationsDir = os.path.join(BasePath, "NotificationsList")
        return NotificationsDir

    def createWindow(self, Number=None, Date=None, Hour=None, Title=None, Content=None):
        """Creates a window. Arguments: Number, Date, Hour, Title, and Content."""
        NotificationsDir = self.GetNotificationDir()

        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        Window = ct.CTk()
        Window.geometry("500x300")
        Window.resizable(False, False)
        Window.title(f"Notification {Number}")

        Frame = ct.CTkFrame(master=Window)
        Frame.pack(fill="both", expand=True)

        TitleLabel = ct.CTkLabel(master=Frame, text=f"Title: {Title}")
        TitleLabel.pack()

        ContentLabel = ct.CTkLabel(master=Frame, text=f"Content: {Content}")
        ContentLabel.pack()

        DateLabel = ct.CTkLabel(master=Frame, text=f"Date: {Date}")
        DateLabel.pack()

        HourLabel = ct.CTkLabel(master=Frame, text=f"Hour: {Hour}")
        HourLabel.pack()

        # Pass the current window to the editWindow method
        editWindowButton = ct.CTkButton(master=Frame, text="Edit", command=lambda: self.editWindow(Number, Window))
        editWindowButton.pack()

        Window.mainloop()

    def editWindow(self, Number, current_window):
        """Edits the notification, replacing the old GUI."""
        current_window.destroy()  # Close the current window

        NotificationsDir = self.GetNotificationDir()
        Number = int(Number)

        # Load the notification data
        with open(os.path.join(NotificationsDir, f"Notification{Number}.json"), "r") as f:
            Notification = json.load(f)

        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        # Create the new window
        Window = ct.CTk()
        Window.geometry("500x300")
        Window.resizable(False, False)
        Window.title(f"Editing notification {Number}")

        Frame = ct.CTkFrame(master=Window)
        Frame.pack(fill="both", expand=True)

        # Widgets for editing
        TitleLabel = ct.CTkEntry(master=Frame, placeholder_text=Notification["Title"])
        TitleLabel.grid(row=0, column=0, padx=10, pady=5, sticky="E")

        ContentLabel = ct.CTkEntry(master=Frame, placeholder_text=Notification["Content"])
        ContentLabel.grid(row=1, column=0, padx=10, pady=5, sticky="E")

        DateLabel = ct.CTkEntry(master=Frame, placeholder_text=Notification["Date"])
        DateLabel.grid(row=2, column=0, padx=10, pady=5, sticky="E")

        HourLabel = ct.CTkEntry(master=Frame, placeholder_text=Notification["Hour"])
        HourLabel.grid(row=3, column=0, padx=10, pady=5, sticky="E")

        # Save changes
        def saveChanges():
            newTitle = TitleLabel.get() if TitleLabel.get() else Notification["Title"]
            newContent = ContentLabel.get() if ContentLabel.get() else Notification["Content"]
            newDate = DateLabel.get() if DateLabel.get() else Notification["Date"]
            newHour = HourLabel.get() if HourLabel.get() else Notification["Hour"]

            # Update notification
            Notification["Title"] = newTitle
            Notification["Content"] = newContent
            Notification["Date"] = newDate
            Notification["Hour"] = newHour

            # Save updated data
            with open(os.path.join(NotificationsDir, f"Notification{Number}.json"), "w") as f:
                json.dump(Notification, f, indent=4)

            # Replace the edit window with an updated view
            self.updateNotificationWindow(Number, newTitle, newContent, newDate, newHour, Window)

        saveButton = ct.CTkButton(master=Frame, text="Save", command=saveChanges)
        saveButton.grid(row=4, column=0, pady=10)

        Window.mainloop()

    def updateNotificationWindow(self, Number, Title, Content, Date, Hour, current_window):
        """Replaces the current notification view with updated data."""
        current_window.destroy()  # Close the current window

        # Create a new notification window with updated data
        Window = ct.CTk()
        Window.geometry("500x300")
        Window.resizable(False, False)
        Window.title(f"Notification {Number}")

        Frame = ct.CTkFrame(master=Window)
        Frame.pack(fill="both", expand=True)

        TitleLabel = ct.CTkLabel(master=Frame, text=f"Title: {Title}")
        TitleLabel.pack()

        ContentLabel = ct.CTkLabel(master=Frame, text=f"Content: {Content}")
        ContentLabel.pack()

        DateLabel = ct.CTkLabel(master=Frame, text=f"Date: {Date}")
        DateLabel.pack()

        HourLabel = ct.CTkLabel(master=Frame, text=f"Hour: {Hour}")
        HourLabel.pack()

        Window.mainloop()

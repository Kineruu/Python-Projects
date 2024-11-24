from utils.Notification import utilsNotifications
import json
import os

notification = utilsNotifications()

BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NotificationsDir = os.path.join(BasePath, "NotificationsList")
NumberPath = os.path.join(NotificationsDir, "Number.txt")

class History:
    def __init__(self):
        pass

    def GetNotificationDir(self):
        """Get current notification directory"""
        BasePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Adjust to project root
        NotificationsDir = os.path.join(BasePath, "NotificationsList")
        return NotificationsDir
    
    def GetTitleFromFiles(self, LatestNotificationButton, PreviousNotificationButton):
        """Opens up .json file with the notification and takes ["Title"] thing"""
        NotificationsDir = self.GetNotificationDir()

        with open(os.path.join(NotificationsDir, "Number.txt"), "r") as f:
            NumberFile = int(f.read().strip())

        with open(os.path.join(NotificationsDir, f"Notification{NumberFile}.json"), "r") as f:
            FileContent = json.load(f)
            Title = FileContent["Title"]
        
        LatestNotificationButton.configure(text=(Title[:15] + "..." if len(Title) > 25 else Title))

        # Read the previous notification title (NumberFile - 1)
        if NumberFile > 1:  # To avoid trying to read a non-existent previous notification
            with open(os.path.join(NotificationsDir, f"Notification{NumberFile-1}.json"), "r") as f:
                FileContent = json.load(f)
                Title = FileContent["Title"]

            PreviousNotificationButton.configure(text=Title[:10] + "..." if len(Title) > 15 else Title)

    #Displays (not fully YET) your latest notification
    def LatestNotification(self):
        NotificationsDir = self.GetNotificationDir()
        with open(os.path.join(NotificationsDir, "Number.txt"), "r") as f:
            NumberFile = int(f.read().strip())

        with open(os.path.join(NotificationsDir, f"Notification{NumberFile}.json"), "r") as f:
            FileContent = json.load(f)
            Title = FileContent["Title"]
            Content = FileContent["Content"]
            Date = FileContent["Date"]
            Hour = FileContent["Hour"]

        #CreateWindow function is from Notification.py file
        notification.createWindow(Number=int(NumberFile), Title=Title, Content=Content, Date=Date, Hour=Hour)

    #Same as LatestNotification but -1
    def PreviousNotification(self):
        NotificationsDir = self.GetNotificationDir()
        with open(os.path.join(NotificationsDir, "Number.txt"), "r") as f:
            NumberFile = int(f.read().strip())

        with open(os.path.join(NotificationsDir, f"Notification{NumberFile-1}.json"), "r") as f:
            FileContent = json.load(f)
            Title = FileContent["Title"]
            Content = FileContent["Content"]
            Date = FileContent["Date"]
            Hour = FileContent["Hour"]

        notification.createWindow(Number=int(NumberFile-1), Title=Title, Content=Content, Date=Date, Hour=Hour)

    #Those two buttons have their titles (You gave them the name)
    def GetTitleFromFiles(self, LatestNotificationButton, PreviousNotificationButton):
        NotificationsDir = self.GetNotificationDir()
        with open(os.path.join(NotificationsDir, "Number.txt"), "r") as f:
            NumberFile = int(f.read().strip())

        with open(os.path.join(NotificationsDir, f"Notification{NumberFile}.json"), "r") as f:
            FileContent = json.load(f)
            Title = FileContent["Title"]
        
        LatestNotificationButton.configure(text=(Title[:15] + "..." if len(Title) > 25 else Title))

        with open(os.path.join(NotificationsDir, f"Notification{NumberFile-1}.json"), "r") as f:
            FileContent = json.load(f)
            Title = FileContent["Title"]

        PreviousNotificationButton.configure(text=Title[:10] + "..." if len(Title) > 15 else Title)

    
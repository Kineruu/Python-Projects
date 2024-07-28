from winotify import Notification, audio
import datetime
import time

def GetCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

Date, Hour = GetCurrentTime()

AtWhatDate = input("[DATE]: ")
AtWhatHour = input("[HOUR]: ")

Title = input("Title: ")
Content = input("Content: ")

time.sleep(2)

while True:
    Date, Hour = GetCurrentTime()
    if Date == AtWhatDate and Hour == AtWhatHour:
        print("LETSGO")
        Noti = Notification(
            app_id="Notification program",
            title=Title,
            msg=Content,
            duration="short"
        )
        
        Noti.show()
        break
    time.sleep(50)
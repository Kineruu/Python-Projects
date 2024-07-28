from winotify import Notification

Title = input("Title: ")
Content = input("Content: ")
icon = input("Any icon? [Coming soon]: ")

Noti = Notification(
    app_id = "Notification program",
    title = Title,
    msg = Content,
    duration = "short"
)

Noti.show()
import customtkinter as ct
import datetime
import time

class Time:
    @staticmethod
    def GetCurrentTime():
        """Returns current day and hour"""
        now = datetime.datetime.now()
        return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

    @staticmethod
    def GetCurrentHour():
        """Returns only current hour"""
        now = datetime.datetime.now()
        NowHour = now.strftime("%H:%M")
        return NowHour

    @staticmethod
    def GetCurrentDate():
        """Returns only current date"""
        now = datetime.datetime.now()
        return now.strftime("%d.%m.%y")
    
    @staticmethod
    def SetCurrentDate(DateEntry):
        """Paste current date in the entry box"""
        DateEntry.delete(0, ct.END)
        DateEntry.insert(0, Time.GetCurrentDate())

    @staticmethod
    def SetCurrentHour(HourEntry):
        """Paste current hour in the entry box"""
        HourEntry.delete(0, ct.END)
        HourEntry.insert(0, Time.GetCurrentHour())

    @staticmethod
    def UpdateTime(TimeLabel):
        """Updates the time every 1 minute"""
        CurrentTime = Time.GetCurrentTime()
        TimeLabel.configure(text=f"{CurrentTime[0]} - {CurrentTime[1]}")
        time.sleep(60)

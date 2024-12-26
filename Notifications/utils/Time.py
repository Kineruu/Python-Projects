import customtkinter as ct
import datetime
import json
import time
import os


BasePath = os.path.dirname(os.path.abspath(__file__))
ConfigPath = os.path.join(BasePath, "..", "config.json")
ConfigPath = os.path.abspath(ConfigPath) 
with open(ConfigPath, "r") as f:
    data = json.load(f)


class Time:
    @staticmethod
    def GetCurrentTime():
        """Returns current day and hour"""
        now = datetime.datetime.now()
        return now.strftime(data["DATE"]), now.strftime((data["HOUR"]))


    @staticmethod
    def GetCurrentYear():
        """Returns only current year"""
        now = datetime.datetime.now()
        return now.strftime(data["YEAR"])
    
    @staticmethod
    def GetCurrentMonth():
        """Returns only current month"""
        now = datetime.datetime.now()
        return now.strftime(data["MONTH"])
    
    @staticmethod
    def GetCurrentHour():
        """Returns only current hour"""
        now = datetime.datetime.now()
        NowHour = now.strftime(data["HOUR"])
        return NowHour

    @staticmethod
    def GetCurrentMinute():
        """Returns only current minute"""
        now = datetime.datetime.now()
        return now.strftime(data["MINUTE"])

    @staticmethod
    def GetCurrentSecond():
        """Returns only current second"""
        now = datetime.datetime.now()
        return now.strftime(data["SECOND"])

    @staticmethod
    def GetCurrentDate():
        """Returns only current date"""
        now = datetime.datetime.now()
        return now.strftime(data["DATE"])


    @staticmethod
    def GetCurrentUnixTime():
        """Returns current unix time"""
        utime = int(time.time())
        return utime
    
    @staticmethod
    def GetPastUnixTime(date, hour):
        """Returns past unix time"""
        PastDateSTR = f"{date} {hour}"
        PastDate = datetime.datetime.strptime(PastDateSTR, "%d.%m.%y %H:%M")
        return int(PastDate.timestamp())

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

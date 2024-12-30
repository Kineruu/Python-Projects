import customtkinter as ct
import datetime
import json
import time
import os

# I think I can remove at least half of this code because it won't be used anymore soon

BasePath = os.path.dirname(os.path.abspath(__file__))
ConfigPath = os.path.join(BasePath, "..", "config.json")
ConfigPath = os.path.abspath(ConfigPath) 
with open(ConfigPath, "r") as f:
    data = json.load(f)


class Time:
    @staticmethod
    def GetCurrentTime():
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
    
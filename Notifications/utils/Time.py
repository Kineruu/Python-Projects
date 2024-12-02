import customtkinter as ct
import datetime
import json
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
        return now.strftime(data["DATE"]), now.strftime(data["HOUR"])

    @staticmethod
    def GetCurrentHour():
        """Returns only current hour"""
        now = datetime.datetime.now()
        NowHour = now.strftime(data["HOUR"])
        return NowHour

    @staticmethod
    def GetCurrentDate():
        """Returns only current date"""
        now = datetime.datetime.now()
        return now.strftime(data["DATE"])
    
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

import customtkinter as ct
import datetime

class Time:
    #Gets current day and hour
    @staticmethod
    def GetCurrentTime():
        now = datetime.datetime.now()
        return now.strftime("%d.%m.%y"), now.strftime("%H:%M")

    #Gets only current hour
    @staticmethod
    def GetCurrentHour():
        now = datetime.datetime.now()
        NowHour = now.strftime("%H:%M")
        return NowHour

    #Gets current date
    @staticmethod
    def GetCurrentDate():
        now = datetime.datetime.now()
        return now.strftime("%d.%m.%y")
    
    @staticmethod
    def SetCurrentDate(DateEntry):
        DateEntry.delete(0, ct.END)
        DateEntry.insert(0, Time.GetCurrentDate())

    @staticmethod
    def SetCurrentHour(HourEntry):
        HourEntry.delete(0, ct.END)
        HourEntry.insert(0, Time.GetCurrentHour())
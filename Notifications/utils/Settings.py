import customtkinter as ct
import json
import os

class Settings:

    @staticmethod
    def loadWindow(Window):
        """ Loading the settings window"""

        Window = ct.CTk()
        Window.geometry("500x350")
        Window.title("Settings!")

        BasePath = os.path.dirname(os.path.abspath(__file__))
        ConfigPath = os.path.join(BasePath, "..", "config.json")
        ConfigPath = os.path.abspath(ConfigPath) 
        with open(ConfigPath, "r") as f:
            data = json.load(f)

        #Time format
        TimeFormatLabel = ct.CTkLabel(master=Window, text="Time format:")
        TimeFormatLabel.pack()

        TimeFormatDateEntry = ct.CTkEntry(master=Window, placeholder_text=data["DATE"])
        TimeFormatDateEntry.pack(pady=5)

        TimeFormatHourEntry = ct.CTkEntry(master=Window, placeholder_text=data["HOUR"])
        TimeFormatHourEntry.pack()

        #Size of the window
        SizeLabel = ct.CTkLabel(master=Window, text="Size of the window:")
        SizeLabel.pack()

        WidthEntry = ct.CTkEntry(master=Window, placeholder_text=data["WIDTH"])
        WidthEntry.pack()

        HeightEntry = ct.CTkEntry(master=Window, placeholder_text=data["HEIGHT"])
        HeightEntry.pack()

        #Replace "if"s with cleaner code in the future!!
        def newData():
            if TimeFormatDateEntry.get().strip() and TimeFormatDateEntry.get() != data["DATE"]:
                data["DATE"] = TimeFormatDateEntry.get()

            if TimeFormatHourEntry.get().strip() and TimeFormatHourEntry.get() != data["HOUR"]:
                data["HOUR"] = TimeFormatHourEntry.get()

            if WidthEntry.get().strip() and WidthEntry.get() != data["WIDTH"]:
                data["WIDTH"] = WidthEntry.get()

            if HeightEntry.get().strip() and HeightEntry.get() != data["HEIGHT"]:
                data["HEIGHT"] = HeightEntry.get()

            with open(ConfigPath, "w") as f:
                json.dump(data, f, indent=4)
        
        def CustomTitlesBox():
            if checkVar.get() == "on":
                data["CUSTOMTITLES"] = "YES"
            else:
                data["CUSTOMTITLES"] = "NO"

            with open(ConfigPath, "w") as f:
                json.dump(data, f, indent=4)

        CustomTitlesLabel = ct.CTkLabel(master=Window, text="Custom titles?")
        CustomTitlesLabel.pack()

        checkVar = ct.StringVar(value="on")
        CustomTitlesCheckBox = ct.CTkCheckBox(master=Window, text="CustomTitles", command=CustomTitlesBox, variable=checkVar, onvalue="on", offvalue="off")
        CustomTitlesCheckBox.pack()

        ConfirmButton = ct.CTkButton(master=Window, text="Save", command=newData)
        ConfirmButton.pack(pady=5)

        Window.mainloop()

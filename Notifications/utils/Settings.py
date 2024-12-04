import customtkinter as ct
import datetime
import json
import os

class Settings:
    @staticmethod
    def loadWindow(Window, MainFrame, reloadSettings):
        """ Loading the settings window"""
        MainFrame.pack_forget()

        SettingsFrame = ct.CTkScrollableFrame(master=Window)
        SettingsFrame.pack(fill="both", expand=True)

        BasePath = os.path.dirname(os.path.abspath(__file__))
        ConfigPath = os.path.join(BasePath, "..", "config.json")
        ConfigPath = os.path.abspath(ConfigPath) 
        with open(ConfigPath, "r") as f:
            data = json.load(f)

        #Time format
        TimeFormatDateLabel = ct.CTkLabel(master=SettingsFrame, text="Time format:")
        TimeFormatDateLabel.pack()

        TimeFormatDateEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=data["DATE"])
        TimeFormatDateEntry.pack(pady=5)

        TimeFormatHourLabel = ct.CTkLabel(master=SettingsFrame, text="Time format (24/12 hours)")
        TimeFormatHourLabel.pack()

        def ChooseTimeFormat(choice):
            now = datetime.datetime.now()

            data["TIMEFORMAT"] = int(choice)

            if data["TIMEFORMAT"] == 24:
                data["HOUR"] = now.strftime("%H:%M")
        
            elif data["TIMEFORMAT"] == 12:
                data["HOUR"] = now.strftime("%I:%M %p")

        OptionMenuVar = ct.StringVar(value=24) 
        TimeFormatHourOptionMenu = ct.CTkOptionMenu(master=SettingsFrame, values=["24", "12"], command=ChooseTimeFormat, variable=OptionMenuVar)
        TimeFormatHourOptionMenu.pack()

        #Size of the window
        SizeLabel = ct.CTkLabel(master=SettingsFrame, text="Size of the window:")
        SizeLabel.pack()

        WidthEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=data["WIDTH"])
        WidthEntry.pack()

        HeightEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=data["HEIGHT"])
        HeightEntry.pack()
        
        def CustomTitlesBox():
            if checkVar.get() == "on":
                data["CUSTOMTITLES"] = "YES"
            else:
                data["CUSTOMTITLES"] = "NO"

            with open(ConfigPath, "w") as f:
                json.dump(data, f, indent=4)

        CustomTitlesLabel = ct.CTkLabel(master=SettingsFrame, text="Custom titles?")
        CustomTitlesLabel.pack()

        checkVar = ct.StringVar(value="on")
        CustomTitlesCheckBox = ct.CTkCheckBox(master=SettingsFrame, text="CustomTitles", command=CustomTitlesBox, variable=checkVar, onvalue="on", offvalue="off")
        CustomTitlesCheckBox.pack()

        ButtonsWidth = ct.CTkLabel(master=SettingsFrame, text="Buttons width")
        ButtonsWidth.pack()

        ButtonsWidthEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=data["BUTTONSWIDTH"])
        ButtonsWidthEntry.pack()

        #Replace "if"s with cleaner code in the future!!
        def newData():
            if TimeFormatDateEntry.get().strip() and TimeFormatDateEntry.get() != data["DATE"]:
                data["DATE"] = TimeFormatDateEntry.get()

            TimeFormat = TimeFormatHourOptionMenu.get().strip()
            if TimeFormat and TimeFormat.isdigit() and int(TimeFormat) != int(data["TIMEFORMAT"]):
                data["TIMEFORMAT"] = int(TimeFormat)

            if WidthEntry.get().strip() and WidthEntry.get() != data["WIDTH"]:
                data["WIDTH"] = WidthEntry.get()

            if HeightEntry.get().strip() and HeightEntry.get() != data["HEIGHT"]:
                data["HEIGHT"] = HeightEntry.get()


            buttonsWidth = ButtonsWidthEntry.get().strip()
            if buttonsWidth and buttonsWidth.isdigit() and int(buttonsWidth) != int(data["BUTTONSWIDTH"]):
                data["BUTTONSWIDTH"] = int(buttonsWidth)

            with open(ConfigPath, "w") as f:
                json.dump(data, f, indent=4)

            reloadSettings()

        ConfirmButton = ct.CTkButton(master=SettingsFrame, text="Save", command=newData)
        ConfirmButton.pack(pady=5)

        BackButton = ct.CTkButton(master=SettingsFrame, text="Back", command=lambda: Settings.backToMain(SettingsFrame, MainFrame))
        BackButton.pack(pady=2)

        Window.mainloop()

    @staticmethod
    def backToMain(SettingsFrame, MainFrame):
        """Go back to the main Frame"""
        SettingsFrame.pack_forget()
        MainFrame.pack(fill="both", expand=True)
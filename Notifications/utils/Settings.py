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
            config = json.load(f)

        #Time format
        TimeFormatDateLabel = ct.CTkLabel(master=SettingsFrame, text="Time format:")
        TimeFormatDateLabel.pack()

        TimeFormatDateEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=config["DATE"])
        TimeFormatDateEntry.pack(pady=5)

        TimeFormatHourLabel = ct.CTkLabel(master=SettingsFrame, text="Time format (24/12 hours)")
        TimeFormatHourLabel.pack()

        def ChooseTimeFormat(choice):
            now = datetime.datetime.now()

            config["TIMEFORMAT"] = int(choice)

            if config["TIMEFORMAT"] == 24:
                config["HOUR"] = now.strftime("%H:%M")

            elif config["TIMEFORMAT"] == 12:
                config["HOUR"] = now.strftime("%I:%M %p")

        SegmentedButtonVar = ct.StringVar(value=24) 
        TimeFormatHourSegmentedButton = ct.CTkSegmentedButton(
            master=SettingsFrame, 
            values=["24", "12"], 
            command=ChooseTimeFormat, 
            variable=SegmentedButtonVar
        )
        TimeFormatHourSegmentedButton.pack()

        #Size of the window
        SizeLabel = ct.CTkLabel(master=SettingsFrame, text="Size of the window:")
        SizeLabel.pack()

        WidthEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=config["WIDTH"])
        WidthEntry.pack()

        HeightEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=config["HEIGHT"])
        HeightEntry.pack()
        
        def CustomTitlesBox():
            if checkVar.get() == "on":
                config["CUSTOMTITLES"] = "YES"
            else:
                config["CUSTOMTITLES"] = "NO"

            with open(ConfigPath, "w") as f:
                json.dump(config, f, indent=4)

        CustomTitlesLabel = ct.CTkLabel(master=SettingsFrame, text="Custom titles?")
        CustomTitlesLabel.pack()


        if config["CUSTOMTITLES"] == "YES":
            checkVar = ct.StringVar(value="on")
        else:
            checkVar = ct.StringVar(value="off")

        CustomTitlesCheckBox = ct.CTkCheckBox(
            master=SettingsFrame, 
            text="CustomTitles", 
            command=CustomTitlesBox, 
            variable=checkVar, 
            onvalue="on", 
            offvalue="off"
        )
        CustomTitlesCheckBox.pack()

        ButtonsWidth = ct.CTkLabel(master=SettingsFrame, text="Buttons width")
        ButtonsWidth.pack()

        ButtonsWidthEntry = ct.CTkEntry(master=SettingsFrame, placeholder_text=config["BUTTONSWIDTH"])
        ButtonsWidthEntry.pack()

        #Replace "if"s with cleaner code in the future!!
        def newData():
            if TimeFormatDateEntry.get().strip() and TimeFormatDateEntry.get() != config["DATE"]:
                config["DATE"] = TimeFormatDateEntry.get()

            TimeFormat = TimeFormatHourSegmentedButton.get().strip()
            if TimeFormat and TimeFormat.isdigit() and int(TimeFormat) != int(config["TIMEFORMAT"]):
                config["TIMEFORMAT"] = int(TimeFormat)

            if WidthEntry.get().strip() and WidthEntry.get() != config["WIDTH"]:
                config["WIDTH"] = WidthEntry.get()

            if HeightEntry.get().strip() and HeightEntry.get() != config["HEIGHT"]:
                config["HEIGHT"] = HeightEntry.get()


            buttonsWidth = ButtonsWidthEntry.get().strip()
            if buttonsWidth and buttonsWidth.isdigit() and int(buttonsWidth) != int(config["BUTTONSWIDTH"]):
                config["BUTTONSWIDTH"] = int(buttonsWidth)

            with open(ConfigPath, "w") as f:
                json.dump(config, f, indent=4)

            reloadSettings()

        ConfirmButton = ct.CTkButton(
            master=SettingsFrame, 
            text="Save", 
            command=newData
        )
        ConfirmButton.pack(pady=5)

        BackButton = ct.CTkButton(
            master=SettingsFrame, 
            text="Back", 
            command=lambda: Settings.backToMain(SettingsFrame, MainFrame)
        )
        BackButton.pack(pady=2)

        Window.mainloop()

    @staticmethod
    def backToMain(SettingsFrame, MainFrame):
        """Go back to the main Frame"""
        SettingsFrame.pack_forget()
        MainFrame.pack(fill="both", expand=True)
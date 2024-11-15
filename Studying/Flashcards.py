import customtkinter as ct
import json
import os

BasePath = os.path.dirname(os.path.abspath(__file__))
JSONPath = os.path.join(BasePath, "flashcards.json")

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

Window = ct.CTk()
Window.geometry("500x300")
Window.resizable(False, False)
Window.title("  Notification Program") 

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)


class Flashcard:
    def __init__(self, flashcardName="", name="", answer="", hints="", time=None):
        self.flashcardName = flashcardName
        self.name = name
        self.answer = answer
        self.time = time
        self.hints = hints


    def add(self, flashcardName="", name="", answer="", hints="", time=None):
        flashcardJSON = {
            "name":name,
            "answer":answer,
            "hints":hints,
            "time":time
        }

        if os.path.exists(JSONPath):
            with open(BasePath + "\\flashcards.json", "r") as f:
                try:
                    data = json.load(f)
                except:
                    data = {}
        else:
            data = {}

        data[flashcardName] = flashcardJSON

        with open(JSONPath, "w") as f:
            json.dump(data, f, indent=4)

        Window.mainloop()

    def show(self, flashcardName):
        if os.path.exists(JSONPath):
            with open(JSONPath, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print("Error reading the JSON file - no changes made")
                    return
        else:
            print("Flashcards file does not exist.")
            return
        
        """
        print(f"What will be the name of the flashcard: {flashcardName}")
        print(f"Name: {data[flashcardName]['name']}")
        print(f"Answer: {data[flashcardName]['answer']}")
        print(f"Hints: {data[flashcardName]['hints']}")
        print(f"How much time (s): {data[flashcardName]['time']}")
        """

    def edit(self, flashcardName):
        ...


    def remove(self, flashcardName):
        if os.path.exists(JSONPath):
            with open(JSONPath, "r") as f:
                try:
                    data = json.load(f) 
                except json.JSONDecodeError:
                    print("Error reading the JSON file - no changes made")
                    return
        else:
            print("Flashcards file does not exist.")
            return

        if flashcardName in data:
            del data[flashcardName] 
            print(f"{flashcardName} has been removed!")

            with open(JSONPath, "w") as f:
                json.dump(data, f, indent=4)
        else:
            print(f"No: '{flashcardName}' found duh.")

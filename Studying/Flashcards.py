import json
import os

BasePath = os.path.dirname(os.path.abspath(__file__))
JSONPath = os.path.join(BasePath, "flashcards.json")

class Flashcard:
    def __init__(self, flashcardName="", name="", answer="", hints=""):
        self.flashcardName = flashcardName
        self.name = name
        self.answer = answer
        self.hints = hints

    def add(self, flashcardName="", name="", answer="", hints=""):
        flashcardJSON = {
            "name":name,
            "answer":answer,
            "hints":hints,
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

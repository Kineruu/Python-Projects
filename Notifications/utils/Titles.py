import random
import json

class Titles:
    def __init__(self, JSONPath):
        self.JSONPath = JSONPath

    def randomTitle(self):
        with open(f"{self.JSONPath}", "r") as f:
            TitleData = json.load(f)

        TitleDict = TitleData[0]

        return random.choice(list(TitleDict.values()))

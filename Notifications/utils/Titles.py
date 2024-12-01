import random
import json

class Titles:
    @staticmethod
    def randomTitle(Path):
        with open(Path) as f:
            TitleData = json.load(f)

        TitleDict = TitleData[0]
        
        return random.choice(list(TitleDict.values()))

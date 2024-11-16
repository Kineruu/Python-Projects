from Flashcards import Flashcard
from random import choice
import json
import os

flashcard = Flashcard()

BasePath = os.path.dirname(os.path.abspath(__file__))
JSONPath = os.path.join(BasePath, "flashcards.json")


print("""
    Hello, welcome to flashcards program.
    What would you like to do today?
"""
)

print("Use flashcards (1), Add (2), edit (3), remove (4), list all flashcards (5)\n")

usersChoice = int(input("Pick one: "))

match usersChoice:
    case 1:
        with open(JSONPath, "r+") as f:
            data = json.load(f)
        randomFlashcard = choice(list(data))
        
        
        print(data[randomFlashcard]["name"])

        usersGuess = input("Answer?: ")
        if usersGuess == data[randomFlashcard]["answer"]:
            print("You got it right!")
        else:
            print("You got it wrong :/")

    case 2:
        flashcardName = input("What will be the name of the flashcard: ")
        name = input("Name: ")
        answer = input("Answer: ")
        hints = input("Hints: ")
        flashcard.add(flashcardName=flashcardName, name=name, answer=answer, hints=hints)
    
    case 3:
        with open(JSONPath, "r+") as f:
            data = json.load(f)
        whichOne = input("Which one?: ")
        list(data)
    
    case 4:
        whichOne = input("Which one?: ")
        flashcard.remove(whichOne)
    
    case 5:
        with open(JSONPath, "r+") as f:
            data = json.load(f)
        print(list(data))
import customtkinter as ct
from random import choice
import os

BasePath = os.path.dirname(os.path.abspath(__file__))

class Flashcard:
    def __init__(self, flashcardName="", name="", answer="", hints="", time=None):
        self.flashcardName = flashcardName
        self.name = name
        self.answer = answer
        self.time = time
        self.hints = hints        
        
        self.number = None
        #self.cards = []


    def add(self, flashcardName, name, answer, hints, time):
        ...

    def show(self, flashcardName):
        ...

    def edit(self, flashcardName):
        ...

    def remove(self, flashcardName):
        ...  


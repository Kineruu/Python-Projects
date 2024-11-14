import customtkinter as ct
from random import choice
import os

BasePath = os.path.dirname(os.path.abspath(__file__))

class Flashcard:
    def __init__(self, name="", answer="", hint="", time=None):
        self.name = name
        self.answer = answer
        self.time = time
        self.hint = hint        
        
        self.number = None
        self.cards = []


    def add(self, name, answer, time):
        ...

    def show(self, flashcardNumber):
        ...

    def edit(self, flashcardNumber):
        ...

    def remove(self, flashcardNumber):
        ...  


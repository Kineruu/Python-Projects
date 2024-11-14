import customtkinter as ct
from random import choice
import json
import os

BasePath = os.path.dirname(os.path.abspath(__file__))

# I have no idea how I'll do it

class Flashcard:
    def __init__(self, name="", answer="", time=None):
        self.name = name
        self.answer = answer
        self.time = time
        self.cards = []
        self.number = None

    def add(self, name, answer):
        ...

    def show(self, flashcardNumber):
        ...

    def remove(self, flashcardNumber):
        ...  
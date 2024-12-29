from clipboard import paste
import customtkinter as ct

# Wait what's the point of that when I can just use the paste() function directly
# In the file? 

# I guess I'll just have it here for now because main.py is still my main file to use and it uses
# This file I guess

class Paste:
    @staticmethod
    def PasteTitle(TitleEntry):
        """Paste whatever you have in your clipboard to the TitleEntry box"""
        UserPaste = paste()
        TitleEntry.delete(0, ct.END)
        TitleEntry.insert(0, UserPaste)


    @staticmethod
    def PasteContent(ContentEntry):
        """Paste whatever you have in your clipboard"""
        UserPaste = paste()
        ContentEntry.delete(0, ct.END)
        ContentEntry.insert(0, UserPaste) 

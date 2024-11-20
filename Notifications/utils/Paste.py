from clipboard import paste
import customtkinter as ct

class Paste:
    @staticmethod
    def PasteTitle(TitleEntry):
        """Paste whatever you have in your clipboard to the TitleEntry box"""
        UserPaste = paste()
        TitleEntry.delete(0, ct.END)
        TitleEntry.insert(0, UserPaste)

    @staticmethod
    def PasteContent(ContentEntry):
        """Paste whatever you have in your clipboard to the ContentEntry box"""
        UserPaste = paste()
        ContentEntry.delete(0, ct.END)
        ContentEntry.insert(0, UserPaste) 

from clipboard import paste
import customtkinter as ct

class Paste:
    @staticmethod
    def PasteTitle(TitleEntry):
        UserPaste = paste()
        TitleEntry.delete(0, ct.END)
        TitleEntry.insert(0, UserPaste)

    @staticmethod
    def PasteContent(ContentEntry):
        UserPaste = paste()
        ContentEntry.delete(0, ct.END)
        ContentEntry.insert(0, UserPaste) 

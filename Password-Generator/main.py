from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice
from clipboard import copy

import customtkinter as ct

#* Creating the main window
Window = ct.CTk()
Window.geometry("250x200")
Window.resizable(False, False)
Window.title("Password")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

#* Password generator itself
CharactersToPickFrom = ascii_lowercase + ascii_uppercase + digits + punctuation
GeneratedPassword = ""

#* The text at the top
MainLabel = ct.CTkLabel(master=Frame, text="Your new password:").pack()

#* Creating space where the generated password will be
NewPassword = ct.CTkLabel(master=Frame, text="")
NewPassword.pack()

#* Asking the user for the password length
HowLongLabel = ct.CTkLabel(master=Frame, text="Length:")
HowLongLabel.place(x=80, y=50)

#* User enters the value here
HowLongPassoword = ct.CTkEntry(master=Frame, placeholder_text="15", width=35, height=10)
HowLongPassoword.place(x=135, y=53.25)

#* Generating the password itself
def GeneratedPasswordFunction():
    global GeneratedPassword
    #* Password is set to "" because later we'll edit the string
    GeneratedPassword = "" 

    #* Most important piece of code right here
    for x in range(int(HowLongPassoword.get())):
        GeneratedPassword += choice(CharactersToPickFrom)
        copy(GeneratedPassword)

    #* We set password to **** to provide safety incase somebody would be even using this on stream or something
    NewPassword.configure(text="*******************************")

#* The button to generate the password
GeneratePassordButton = ct.CTkButton(master=Frame, text="Create", command=GeneratedPasswordFunction, width=90, height=30)
GeneratePassordButton.place(x=80, y=80)

#* Incase you want to see the password
def ShowPassword():
    NewPassword.configure(text=GeneratedPassword)

ShowButton = ct.CTkButton(master=Frame, text="Show", command=ShowPassword, width=10, height=10)
ShowButton.place(x=80, y=115)

#* Or incase you won't want to see it anymore
def HidePassword():
    NewPassword.configure(text="*******************************")

HideButton = ct.CTkButton(master=Frame, text="Hide", command=HidePassword, width=10, height=10)
HideButton.place(x=132, y=115)

#* I don't think I'm able to make user able to copy the password by hand, so I have to copy it automatically to the clipboard
CopyLabel = ct.CTkLabel(master=Frame, text="The password is automatically\n copied to the clipboard.")
CopyLabel.place(x=40, y=145)

#* Keeping the window alive
Window.mainloop()
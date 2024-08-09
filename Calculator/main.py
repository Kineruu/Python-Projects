import simpleeval
import customtkinter as ct
import math

Window = ct.CTk()
Window.geometry("500x300")
Window.resizable(False, False)

Window.title("Calculator")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

def Calc(Equations):
    try:
        Equations.replace("^", "**")
        return simpleeval.simple_eval(Equations)
    except Exception as e:
        return e

EquationEntry = ct.CTkEntry(master=Frame, placeholder_text="Type your equation here", width=230)
EquationEntry.place(x=10, y=10)

def CE():
    EquationEntry.delete(0, ct.END)
    #EquationEntry.insert(0, ct.END)

DeleteAll = ct.CTkButton(master=Frame, text="CE", command=CE, width=100)
DeleteAll.place(x=250, y=10)

def sqrtdef():
    current_text = EquationEntry.get()
    if current_text and current_text[-1].isdigit():
        last_digit = int(current_text[-1])
        return last_digit
    return None

def square(): 
    LastDigit = sqrtdef()
    if LastDigit != None:
        Result = math.sqrt(LastDigit)
        EquationEntry.delete(0, ct.END)
        EquationEntry.insert(0, EquationEntry.get()[:-1] + str(Result))

def SquareTwo():
    LastDigit = sqrtdef()
    if LastDigit != None:
        Result = math.pow(LastDigit, 2)
        EquationEntry.delete(0, ct.END)
        EquationEntry.insert(0, EquationEntry.get()[:-1] + str(Result))


SquareButton = ct.CTkButton(master=Frame, text="SQRT", command=square, width=100)
SquareButton.place(x=214, y=48)



def Division(): EquationEntry.insert(ct.END, "/")
DivisionButton = ct.CTkButton(master=Frame, text="/", command=Division, width=100)
DivisionButton.place(x=316, y=48)

def PowerTwo(): EquationEntry.insert(ct.END, "HELLO")
PowerTwoButton = ct.CTkButton(master=Frame, text="^2", command=SquareTwo, width=100)
PowerTwoButton.place(x=112, y=48)

def nine(): EquationEntry.insert(ct.END, "9")
NineButton = ct.CTkButton(master=Frame, text="9", command=nine, width=100)
NineButton.place(x=214, y=80)

def eight(): EquationEntry.insert(ct.END, "8")
EightButton = ct.CTkButton(master=Frame, text="8", command=eight, width=100)
EightButton.place(x=112, y=80)

def seven(): EquationEntry.insert(ct.END, "7")
SevenButton = ct.CTkButton(master=Frame, text="7", command=seven, width=100)
SevenButton.place(x=10, y=80)

def multiply(): EquationEntry.insert(ct.END, "*")
MultiplyButton = ct.CTkButton(master=Frame, text="*", command=multiply, width=100)
MultiplyButton.place(x=316, y=80)

def six(): EquationEntry.insert(ct.END, "6")
SixButton = ct.CTkButton(master=Frame, text="6", command=six, width=100)
SixButton.place(x=214, y=112)

def five(): EquationEntry.insert(ct.END, "5")
FiveButton = ct.CTkButton(master=Frame, text="5", command=five, width=100)
FiveButton.place(x=112, y=112)

def four(): EquationEntry.insert(ct.END, "4")
FourButton = ct.CTkButton(master=Frame, text="4", command=four, width=100)
FourButton.place(x=10, y=112)

def minus(): EquationEntry.insert(ct.END, "-")
PlusButton = ct.CTkButton(master=Frame, text="-", command=minus, width=100)
PlusButton.place(x=316, y=112)


def three(): EquationEntry.insert(ct.END, "3")
ThreeButton = ct.CTkButton(master=Frame, text="3", command=three, width=100)
ThreeButton.place(x=214, y=144)

def two(): EquationEntry.insert(ct.END, "2")
TwoButton = ct.CTkButton(master=Frame, text="2", command=two, width=100)
TwoButton.place(x=112, y=144)

def one(): EquationEntry.insert(ct.END, "1")
OneButton = ct.CTkButton(master=Frame, text="1", command=one, width=100)
OneButton.place(x=10, y=144)

def plus(): EquationEntry.insert(ct.END, "+")
PlusButton = ct.CTkButton(master=Frame, text="+", command=plus, width=100)
PlusButton.place(x=316, y=144)


def zero(): EquationEntry.insert(ct.END, "0")
ZeroButton = ct.CTkButton(master=Frame, text="0", command=zero, width=100)
ZeroButton.place(x=112, y=176)

def plusandminus(): EquationEntry.insert(ct.END, "-")
PlusAndMinusButton = ct.CTkButton(master=Frame, text="-", command=plusandminus, width=100)
PlusAndMinusButton.place(x=10, y=176)

def dot(): EquationEntry.insert(ct.END, ".")
MinusButton = ct.CTkButton(master=Frame, text=".", command=dot, width=100)
MinusButton.place(x=214, y=176)

def GetEquationEntry():
    result = Calc(EquationEntry.get())
    EquationEntry.delete(0, ct.END)
    EquationEntry.insert(0, result)
    return EquationEntry.get()

EquationButton = ct.CTkButton(master=Frame, text="=", command=GetEquationEntry, width=100)
EquationButton.place(x=316, y=176)



Window.mainloop()
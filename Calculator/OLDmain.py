import simpleeval
import customtkinter as ct
import math
import re

#* Creating the window
Window = ct.CTk()
Window.geometry("500x400")
Window.resizable(False, False)
Window.title("Calculator")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

#* Width and height of the buttons
ButtonsWidth = 100
ButtonsHeight = 40


CalcEntry = ct.CTkEntry(master=Frame, placeholder_text="2 + 2", width=250, height=40)
CalcEntry.place(x=10, y=10)

#* Calculating function
def calc(Equations):
    try:
        Equations.replace("^", "**")
        Equations = re.sub(r'(\d)\(', r'\1*(', Equations)

        return simpleeval.simple_eval(Equations, functions={
            "sqrt":math.sqrt,
            "log":logFunction,
            "sin":math.sin, 
            "cos":math.cos, 
            "tan":math.tan,
        })
    
    except Exception as e:
        return e

def CalcButtonFunction():
    result = calc(CalcEntry.get())
    CalcEntry.delete(0, ct.END)
    CalcEntry.insert(0, result)
    return CalcEntry.get()

CalcButton = ct.CTkButton(master=Frame, text="=", command=CalcButtonFunction, width=ButtonsWidth, height=ButtonsHeight)
CalcButton.place(x=265, y=10)

#* x^3
def root3():
    CalcEntry.insert(ct.END, "**3")

Root3Button = ct.CTkButton(master=Frame, text="x^3", command=root3, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
Root3Button.place(x=10, y=60)

#* x^Y
def rootY():
    CalcEntry.insert(ct.END, "**Y")

RootYButton = ct.CTkButton(master=Frame, text="x^Y", command=rootY, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
RootYButton.place(x=115, y=60)

#* sqrt(x)
def sqrt():
    CalcEntry.insert(ct.END, "sqrt()")
    CalcEntry.icursor(CalcEntry.index(ct.END) - 1)
    CalcEntry.select_range(CalcEntry.index(ct.END) - 1, CalcEntry.index(ct.END))

SqrtButton = ct.CTkButton(master=Frame, text="√", command=sqrt, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
SqrtButton.place(x=220, y=60)

#* x^2
def root2():
    CalcEntry.insert(ct.END, "**2")

Root2Button = ct.CTkButton(master=Frame, text="x^2", command=root2, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
Root2Button.place(x=325, y=60)

#* LogFunction
def logFunction(value, base=math.e):
    if base == 10:
        return math.log10(value)
    return math.log(value)

#* log
def log():
    CalcEntry.insert(ct.END, "log()")
    CalcEntry.icursor(CalcEntry.index(ct.END) - 1)  
    CalcEntry.select_range(CalcEntry.index(ct.END) - 1, CalcEntry.index(ct.END)) 

LogButton = ct.CTkButton(master=Frame, text="log", command=log, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
LogButton.place(x=10, y=105)

#* sin
def sin():
    CalcEntry.insert(ct.END, "sin()")
    CalcEntry.icursor(CalcEntry.index(ct.END) - 1) 
    CalcEntry.select_range(CalcEntry.index(ct.END) - 1, CalcEntry.index(ct.END))

SinButton = ct.CTkButton(master=Frame, text="sin", command=sin, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
SinButton.place(x=115, y=105)

#* cos
def cos():
    CalcEntry.insert(ct.END, "cos()") 
    CalcEntry.icursor(CalcEntry.index(ct.END) - 1) 
    CalcEntry.select_range(CalcEntry.index(ct.END) - 1, CalcEntry.index(ct.END))

CosButton = ct.CTkButton(master=Frame, text="cos", command=cos, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
CosButton.place(x=220, y=105)

#* tan
def tan():
    CalcEntry.insert(ct.END, "tan()")  
    CalcEntry.icursor(CalcEntry.index(ct.END) - 1) 
    CalcEntry.select_range(CalcEntry.index(ct.END) - 1, CalcEntry.index(ct.END)) 

TanButton = ct.CTkButton(master=Frame, text="tan", command=tan, width=ButtonsWidth, height=ButtonsHeight, fg_color="green")
TanButton.place(x=325, y=105)

#* (
def leftBracket():
    CalcEntry.insert(ct.END, "(")

leftBracketButton = ct.CTkButton(master=Frame, text="(", command=leftBracket, width=ButtonsWidth, height=ButtonsHeight)
leftBracketButton.place(x=10, y=150)

#* )
def rightBracket():
    CalcEntry.insert(ct.END, ")")

rightBracketButton = ct.CTkButton(master=Frame, text=")", command=rightBracket, width=ButtonsWidth, height=ButtonsHeight)
rightBracketButton.place(x=115, y=150)

#* <-
def backspace(): 
    currentText = CalcEntry.get()
    if currentText: CalcEntry.delete(len(currentText) - 1)

backspaceButton = ct.CTkButton(master=Frame, text="<-", command=backspace, width=ButtonsWidth, height=ButtonsHeight, fg_color="red")
backspaceButton.place(x=220, y=150)

#* Erase everything
def clear(): CalcEntry.delete(0, ct.END)

clearButton = ct.CTkButton(master=Frame, text="Delete", command=clear, width=ButtonsWidth, height=ButtonsHeight, fg_color="red")
clearButton.place(x=325, y=150)

#* FIRST ROW
def seven(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "7")
sevenButton = ct.CTkButton(master=Frame, text="7", command=seven, width=ButtonsWidth, height=ButtonsHeight)
sevenButton.place(x=10, y=195)

def eight(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "8")
eightButton = ct.CTkButton(master=Frame, text="8", command=eight, width=ButtonsWidth, height=ButtonsHeight)
eightButton.place(x=115, y=195)

def nine(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "9")
nineButton = ct.CTkButton(master=Frame, text="9", command=nine, width=ButtonsWidth, height=ButtonsHeight)
nineButton.place(x=220, y=195)

def multiply(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "*")
multiplyButton = ct.CTkButton(master=Frame, text="*", command=multiply, width=ButtonsWidth, height=ButtonsHeight)
multiplyButton.place(x=325, y=195)

#* SECOND ROW
def four(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "4")
fourButton = ct.CTkButton(master=Frame, text="4", command=four, width=ButtonsWidth, height=ButtonsHeight)
fourButton.place(x=10, y=240)

def five(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "5")
fiveButton = ct.CTkButton(master=Frame, text="5", command=five, width=ButtonsWidth, height=ButtonsHeight)
fiveButton.place(x=115, y=240)

def six(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "6")
sixButton = ct.CTkButton(master=Frame, text="6", command=six, width=ButtonsWidth, height=ButtonsHeight)
sixButton.place(x=220, y=240)

def divide(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "/")
divideButton = ct.CTkButton(master=Frame, text="/", command=divide, width=ButtonsWidth, height=ButtonsHeight)
divideButton.place(x=325, y=240)

#* THIRD ROW
def one(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "1")
oneButton = ct.CTkButton(master=Frame, text="1", command=one, width=ButtonsWidth, height=ButtonsHeight)
oneButton.place(x=10, y=285)

def two(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "2")
twoButton = ct.CTkButton(master=Frame, text="2", command=two, width=ButtonsWidth, height=ButtonsHeight)
twoButton.place(x=115, y=285)

def three(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "3")
threeButton = ct.CTkButton(master=Frame, text="3", command=three, width=ButtonsWidth, height=ButtonsHeight)
threeButton.place(x=220, y=285)

def plus(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "+")
plusButton = ct.CTkButton(master=Frame, text="+", command=plus, width=ButtonsWidth, height=ButtonsHeight)
plusButton.place(x=325, y=285)

#* FOURTH ROW
def dot(): CalcEntry.insert(CalcEntry.index(ct.INSERT), ".")
dotButton = ct.CTkButton(master=Frame, text=".", command=dot, width=ButtonsWidth, height=ButtonsHeight)
dotButton.place(x=10, y=330)

def zero(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "0")
zeroButton = ct.CTkButton(master=Frame, text="0", command=zero, width=ButtonsWidth, height=ButtonsHeight)
zeroButton.place(x=115, y=330)

def pi(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "3.14")
piButton = ct.CTkButton(master=Frame, text="π", command=pi, width=ButtonsWidth, height=ButtonsHeight)
piButton.place(x=220, y=330)

def minus(): CalcEntry.insert(CalcEntry.index(ct.INSERT), "-")
minusButton = ct.CTkButton(master=Frame, text="-", command=minus, width=ButtonsWidth, height=ButtonsHeight)
minusButton.place(x=325, y=330)

Window.mainloop()
import simpleeval
import customtkinter as ct
import math
import re

Window = ct.CTk()
Window.geometry("500x400")
Window.resizable(False, False)
Window.title("Calculator")

Frame = ct.CTkFrame(master=Window)
Frame.pack(fill="both", expand=True)

CalcEntry = ct.CTkEntry(master=Frame, placeholder_text="2 + 2", width=250, height=40)
CalcEntry.place(x=10, y=10)

# Calculator Functions
def calc(expression):
    try:
        expression = expression.replace("^", "**")
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        return simpleeval.simple_eval(expression, functions={
            "sqrt": math.sqrt,
            "log": logFunction,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
        })
    except Exception as e:
        return e

def CalcButtonFunction():
    result = calc(CalcEntry.get())
    CalcEntry.delete(0, ct.END)
    CalcEntry.insert(0, result)

def logFunction(value, base=math.e):
    return math.log10(value) if base == 10 else math.log(value)

def insertFunction(name):
    CalcEntry.insert(ct.END, f"{name}()")
    CalcEntry.icursor(CalcEntry.index(ct.END) - 1)

def insertChar(char):
    CalcEntry.insert(ct.END, char)

def backspace():
    current_text = CalcEntry.get()
    if current_text:
        CalcEntry.delete(len(current_text) - 1)

def clear():
    CalcEntry.delete(0, ct.END)

#* Width and height of the buttons
ButtonsWidth = 100
ButtonsHeight = 40

buttons = [
    {"text": "=", "command": CalcButtonFunction, "x": 265, "y": 10},
    {"text": "x^3", "command": lambda: insertChar("**3"), "x": 10, "y": 60, "color": "green"},
    {"text": "x^Y", "command": lambda: insertChar("**Y"), "x": 115, "y": 60, "color": "green"},
    {"text": "√", "command": lambda: insertFunction("sqrt"), "x": 220, "y": 60, "color": "green"},
    {"text": "x^2", "command": lambda: insertChar("**2"), "x": 325, "y": 60, "color": "green"},

    {"text": "log", "command": lambda: insertFunction("log"), "x": 10, "y": 105, "color": "green"},
    {"text": "sin", "command": lambda: insertFunction("sin"), "x": 115, "y": 105, "color": "green"},
    {"text": "cos", "command": lambda: insertFunction("cos"), "x": 220, "y": 105, "color": "green"},
    {"text": "tan", "command": lambda: insertFunction("tan"), "x": 325, "y": 105, "color": "green"},

    {"text": "(", "command": lambda: insertChar("("), "x": 10, "y": 150},
    {"text": ")", "command": lambda: insertChar(")"), "x": 115, "y": 150},
    {"text": "<-", "command": backspace, "x": 220, "y": 150, "color": "red"},
    {"text": "Delete", "command": clear, "x": 325, "y": 150, "color": "red"},
]

numbers = [
    ("7", 10, 195), ("8", 115, 195), ("9", 220, 195), ("*", 325, 195),
    ("4", 10, 240), ("5", 115, 240), ("6", 220, 240), ("/", 325, 240),
    ("1", 10, 285), ("2", 115, 285), ("3", 220, 285), ("+", 325, 285),
    (".", 10, 330), ("0", 115, 330), ("π", 220, 330, lambda: insertChar("3.14")), ("-", 325, 330),
]

for button in buttons:
    color = button.get("color", None)
    ct.CTkButton(
        master=Frame,
        text=button["text"],
        command=button["command"],
        width=ButtonsWidth,
        height=ButtonsHeight,
        fg_color=color
    ).place(x=button["x"], y=button["y"])

for text, x, y, *cmd in numbers:
    command = cmd[0] if cmd else lambda t=text: insertChar(t)
    ct.CTkButton(
        master=Frame,
        text=text,
        command=command,
        width=ButtonsWidth,
        height=ButtonsHeight
    ).place(x=x, y=y)

Window.mainloop()
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter, ImageChops #AINTNOWAY
import numpy as np
import cv2
import os

# No clue if I'll use png or write a gui for it
# Imagine having 9x9 board with 3x3 subgrids using Entry boxes hahahahhahah
# That would be cruel, no?
# Who knows
# I'll probably just use a png and write a solver for it
# Will be quicker and less annoying to use Entry boxes

# I'll probably use a library for the png
# I'll probably use PIL for the png
# I'll probably use numpy for the solver
# I'll probably use tkinter for the gui
# I'll probably use pygame for the gui
# No I'm not going schizophrenic

# I'm just thinking out loud
# I'm not even thinking out loud
# I'm just typing out loud
# I'm not even typing out loud
# I'm just typing
# I'm not even typing
# I'm just pressing buttons
# I'm not even pressing buttons
# I'm just pressing keys
# I'm not even pressing keys
# I'm just pressing
# I'm not even pressing
# I'm just
# I'm not even
# I'm
# I'm not
# I

# I'm not even sure what I'm doing anymore
# Life MAN
# If you know you know those emotes
# om

# Do NOT ask why board.png is literally a blank white image
# It's just for testing alright?
# I'll probably use a library to generate a sudoku board
# I'll probably use a library to solve a sudoku board
# I'll probably use a library to display a sudoku board
# I'll probably use a library to do everything
# I'll probably use a library to do nothing
# Uhhh yeah

# 1000x1000 image size
# Yes I'll fix the path later

# Do I really want to use images or make the user write the numbers?
# Or allow both? Who knows?
# I'll see that in the future
# That future is coming soon
# Sooner that you think
# Sooner than I think
# Sooner than I think I think   # I'm not even sure what I'm doing anymore
# Life

# Should I add more features do this program?
# Like creating own sudoku boards instead of only solving them

class GUI:
    def __init__(self, width, height):
        self.title = "Sudoku"

        self.width = 1000
        self.height = 1000
        self.board_path = "board.png"
        self.checkExtension()
        self.board = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.line = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.lineDraw = ImageDraw.Draw(self.line)
        
    def drawBoard(self):
        w = round(self.board.width / 3)
        h = round(self.board.height / 3)

        sw = round(self.board.width / 9)
        sh = round(self.board.height / 9)

        for x in range(0, self.board.width, w):
            self.lineDraw.line((x, 0, x, self.board.height), fill=(0, 0, 0), width=10)
        for y in range(0, self.board.height, h):
            self.lineDraw.line((0, y, self.board.width, y), fill=(0, 0, 0), width=10)

        for x in range(0, self.board.width, sw):
            self.lineDraw.line((x, 0, x, self.board.height), fill=(0, 0, 0), width=5)
        for y in range(0, self.board.height, sh):
            self.lineDraw.line((0, y, self.board.width, y), fill=(0, 0, 0), width=5)

        self.line.show()

    def getBoard(self):
        self.board.show()
        return self.board

        """
        boardList = [
            0, 0, 0,   0, 0, 0,   0, 0, 0, #1
            0, 0, 0,   0, 0, 0,   0, 0, 0, #2
            0, 0, 0,   0, 0, 0,   0, 0, 0, #3

            0, 0, 0,   0, 0, 0,   0, 0, 0, #4
            0, 0, 0,   0, 0, 0,   0, 0, 0, #5
            0, 0, 0,   0, 0, 0,   0, 0, 0, #6

            0, 0, 0,   0, 0, 0,   0, 0, 0, #7
            0, 0, 0,   0, 0, 0,   0, 0, 0, #8
            0, 0, 0,   0, 0, 0,   0, 0, 0, #9
        ]
        """
        
        # To be honest I think just making a simple GUI in tkinter/other things would be easier
        # For me to maintain and for the user to use
        # I ain't using some weird libraries to do this
        # Like I don't want to do AI stuff too so no.
        # Tkinter it is I guess

        # Easyocr is taking way too long to load
        # Not worth it

    def checkExtension(self):
        if self.board.endswith(".png"):
            pass
        else:
            print("Invalid file extension. Please use a PNG file.")
            exit()


    def resizeBoard(self):
        if self.board.size != (1000, 1000):
            self.board = self.board.resize((1000, 1000))
        else:
            pass
        # :)

    def clearBoard(self):
        self.board = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.line = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.lineDraw = ImageDraw.Draw(self.line)
        self.drawBoard()

# WAIT I FORGOT I NEED TO SPLIT IT INTO MORE PIECES om
# 3 big lines and small ones too

def displayBoard(board):
    pass

def solveBoard(board):
    pass

# Get user's png - DONE
# Check if the file is a png - DONE
# Resize the png to 1000x1000 - DONE
# Get numbers and (hopefully) write them on the board - X
# Yeah I'll be using GUI for that
# Solve the board
# Display the board
# Profit


from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter, ImageChops #AINTNOWAY
import pytesseract

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

def getBoard(board):
    usersBoard = Image.open(board)
    numbers = []
    #print(pytesseract.image_to_string(usersBoard))
    # WHY PYTESSERACT ISN'T WORKING
    # ADJNAWIJUDNAWIJUNFGIAWUJNGIUAWBNIUABNJFNAJKDNAWIJUDNAWUIDNABWDJUIAWNDUJIAWNDUJIWNH

def checkExtension(board):
    if board.endswith(".png"):
        pass
    else:
        print("Invalid file extension. Please use a PNG file.")
        exit()

def resizeBoard(board):
    if board.size != (1000, 1000):
        board = board.resize((1000, 1000))
    else:
        pass
    # :)

def displayBoard(board):
    pass

def solveBoard(board):
    pass

# Get user's png - DONE
# Check if the file is a png - DONE
# Resize the png to 1000x1000 - DONE
# Get numbers and (hopefully) write them on the board
# Solve the board
# Display the board
# Profit

def imageDraw(board):
    #img = ImageDraw.Draw(board)
    w = round(board.width / 3)
    h = round(board.height / 3)
    line = Image.new("RGB", (board.width, board.height), (255, 255, 255))
    lineDraw = ImageDraw.Draw(line)
    for x in range(0, board.width, w):
        lineDraw.line((x, 0, x, board.height), fill=(0, 0, 0), width=10)
    for y in range(0, board.height, h):
        lineDraw.line((0, y, board.width, y), fill=(0, 0, 0), width=10)
    line.show()
    #print(w, h)

# I have no idea what I am doing
# Help

if __name__ == "__main__":
    sudokuBoard = str(input("Enter the path to the board: "))
    checkExtension(sudokuBoard)
    board = getBoard(sudokuBoard)
    imageDraw(board)
    solveBoard(board)
    
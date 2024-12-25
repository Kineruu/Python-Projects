from PIL import Image, ImageDraw, ImageTk
import customtkinter as ct
import os

class SudokuGUI:
    basePath = os.path.dirname(os.path.abspath(__file__))

    board = str(input("Enter the path to the board: "))

    def __init__(self, width, height):
        self.title = "Sudoku"

        self.width = width
        self.height = height
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
        print(sw, sh)


        for x in range(0, self.board.width, w):
            self.lineDraw.line((x, 0, x, self.board.height), fill=(0, 0, 0), width=10)
        for y in range(0, self.board.height, h):
            self.lineDraw.line((0, y, self.board.width, y), fill=(0, 0, 0), width=10)

        for x in range(0, self.board.width, sw):
            self.lineDraw.line((x, 0, x, self.board.height), fill=(0, 0, 0), width=2)
        for y in range(0, self.board.height, sh):
            self.lineDraw.line((0, y, self.board.width, y), fill=(0, 0, 0), width=2)



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

    def clearBoard(self):
        self.board = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.line = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.lineDraw = ImageDraw.Draw(self.line)
        self.drawBoard()

    def displayBoard(self, board):
        self.board_image = ImageTk.PhotoImage(self.board)
        self.canvas.create_image(0, 0, anchor='nw', image=self.board_image)


    def solveBoard(board):
        pass

    def main(self):
        self.root.mainloop()


if __name__ == "__main__":
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("blue")

    app = SudokuGUI(1000, 1000)
    app.main()


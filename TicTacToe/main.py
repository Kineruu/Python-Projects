from random import randint

boardJ = {
    "0": "-", "1": "-", "2": "-",
    "3": "-", "4": "-", "5": "-",
    "6": "-", "7": "-", "8": "-"
}

def displayBoard():
    board = f"""
    {boardJ["0"]} {boardJ["1"]} {boardJ["2"]}
    {boardJ["3"]} {boardJ["4"]} {boardJ["5"]}
    {boardJ["6"]} {boardJ["7"]} {boardJ["8"]}
    """
    print(board)

boardList = list(range(9))

def winningMoves(player):
    winConditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in winConditions:
        if all(boardJ[str(pos)] == player for pos in condition):
            return True
    return False

def playerMove():
    while True:
        try:
            userInput = int(input("Your turn (0-8): "))
            if userInput in boardList:
                boardJ[str(userInput)] = "O"
                boardList.remove(userInput)
                displayBoard()
                if winningMoves("O"):
                    print("You win!")
                    return True
                break
            else:
                print("You can't move there, try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
    return False

def botMove():
    while True:
        botMove = randint(0, 8)
        if botMove in boardList:
            boardJ[str(botMove)] = "X"
            boardList.remove(botMove)
            print("Bot's turn:")
            displayBoard()
            if winningMoves("X"):
                print("Bot wins!")
                return True
            break
    return False

def playGame():
    displayBoard()

    first_turn = randint(0, 1) 

    while boardList:
        if first_turn == 0:
            if playerMove():
                break
            first_turn = 1
        else:
            if botMove():
                break
            first_turn = 0 

        if not boardList:
            print("It's a draw!")
            break

playGame()
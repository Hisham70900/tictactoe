import random 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    global currentPlayer
    inp = int(input("Enter the number 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Invalid move or already occupied! Try again.")
        playerInput(board)

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]; return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]; return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]; return True
    

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]; return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]; return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]; return True
    

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]; return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]; return True
    


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("😐 It's a tie!")
        gameRunning = False

def checkWinner():
    global gameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        printBoard(board)
        print(f"🎉 The winner is {winner}!")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

def computer(board):
    global currentPlayer
    if currentPlayer == "O":
        position = random.randint(0, 8)
        while board[position] != "-":
            position = random.randint(0, 8)
        board[position] = "O"
        print("Computer placed O at position", position + 1)
        switchPlayer()



while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWinner()
    checkTie(board)
    if not gameRunning:
        break

    switchPlayer()
    computer(board)
    checkWinner()
    checkTie(board)

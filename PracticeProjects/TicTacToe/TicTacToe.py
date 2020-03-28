def printBoard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('- + - + -')
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('- + - + -')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])


def game():
    while True:
        theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
        turn = "X"
        winner = ""
        print("\nTIC TAC TOE")
        winner = gameLoop(theBoard, turn, winner)
        printBoard(theBoard)  # prints final board
        if winner == "":
            print("It's a draw!")
        else:
            print(winner + " won!")
        choice = input("Play again? (Y/N)")
        if choice.lower() != "y":
            break


def gameLoop(theBoard, turn, winner):
    for i in range(9):
        printBoard(theBoard)
        userEntry(theBoard, turn)
        values = list(theBoard.values())
        winner = checkifWin(values, winner)
        if winner != "":
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    return winner


def userEntry(theBoard, turn):
    while True:
        print("\nTurn for " + turn + ". Move on which space? (enter 'c' to see commands) ")
        move = input()
        if move.lower() == "c":
            print("commands are: ", end="")
            for key in theBoard:
                print(key + ", ", end="")
        elif move in theBoard.keys() and theBoard[move] == " ":
            theBoard[move] = turn
            break
        else:
            print("Please enter a valid location.")


def checkifWin(values, winner):
    for j in range(7):
        if j % 3 == 0 and values[j] == values[j + 1] == values[j + 2] != " ":  # checks rows for winner
            winner = values[j]
            break
        if j < 3 and values[j] == values[j + 3] == values[j + 6] != " ":  # checks columns for winner
            winner = values[j]
            break
        if values[0] == values[4] == values[8] != " ":  # checks top-left diagonal for winner
            winner = values[4]
            break
        if values[2] == values[4] == values[6] != " ":  # checks top-right diagonal for winner
            winner = values[4]
            break
    return winner


game()

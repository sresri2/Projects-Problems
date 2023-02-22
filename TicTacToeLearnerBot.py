"""
The following functionalities are present:
- Self-learning Tic-Tac-Toe Bot
- Saves any previously learning
- Option to reset learning
- Fully playable, Any person can play the Bot. 
- Ability to Learn while playing
"""

import pickle
import random
import math
def save(moves):
    filename = "ticTacToeMovesStorage.pk"
    with open(filename, 'wb') as save:
        pickle.dump(moves, save)
    return
def verifyWin(board,mover):
    cases = []
    if board[0]==board[1] and board[1]==board[2] and board[0]!="E" and board[0]==mover:
        cases.append(True)
    if board[3]==board[4] and board[4]==board[5]and board[4]!="E" and board[3]==mover:
        cases.append(True)
    if board[6]==board[7] and board[7]==board[8] and board[6]!="E" and board[6]==mover:
        cases.append(True)
    if board[0]==board[3] and board[3]==board[6] and board[0]!= "E" and board[0]==mover:
        cases.append(True)
    if board[1]==board[4] and board[4]==board[7] and board[1]!= "E" and board[1]==mover:
        cases.append(True)
    if board[2]==board[5] and board[5]==board[8] and board[2]!="E" and board[2]==mover:
        cases.append(True)
    if board[0]==board[4]and board[4]==board[8]and board[0]!= "E" and board[0]==mover:
        cases.append(True)
    if board[2]==board[4]and board[4]==board[6] and board[2]!="E" and board[2]==mover:
        cases.append(True)
    if True in cases:
        return True
    return False


def loadMovesStorage():
    filename = "ticTacToeMovesStorage.pk"
    with open(filename, 'rb') as load:
        movesStorage = pickle.load(load)
    return movesStorage

def generateMoves():
    moves = {}
    count = 0
    while count < 1000000:
        board = ["E","E","E","E","E","E","E","E","E"]
        available = [0,1,2,3,4,5,6,7,8]
        mover = "X"
        while True:
            chooseSpot = random.randint(0,len(available)-1)
            checkBoard = board.copy()
            checkBoard[available[chooseSpot]] = mover
            lastMove = None
            checkWinningMove = verifyWin(checkBoard,mover)
            if checkWinningMove:
                strBoard = "".join(board)
                moves[strBoard] = [available[chooseSpot]]
                prevMoveStr = "".join(prevBoard)
                moves[prevMoveStr] = [available[chooseSpot]]
                break
            
            elif "E" not in checkBoard:
                strBoard = "".join(board)
                moves[strBoard] = [available[chooseSpot]]
                break
            else:
                strBoard = "".join(board)
                if strBoard in moves:
                    if available[chooseSpot] not in moves[strBoard]:
                        moves[strBoard].append(available[chooseSpot])
                else:
                    moves[strBoard] = [available[chooseSpot]]
                prevBoard = board.copy()
                board[available[chooseSpot]] = mover
                lastMove = available[chooseSpot]
                del(available[chooseSpot])
            if mover == "X":
                mover = "O"
            else:
                mover = "X"
        count += 1
    return moves


def main():
    newGenerate = input("To Generate Moves Type 1. To Load Past Moves Generation Type 2. To reset MovesStorage Type 3: ")
    if newGenerate == "3":
        moves = {}
        save(moves)
        print("MovesStorage Reset")
    elif newGenerate == "2":
        moves = loadMovesStorage()
        if not moves:
            print("Loading unsuccessful. Check to make sure you have something saved.")
    elif newGenerate == "1":
        moves = loadMovesStorage()
        if not moves:
            moves = {}
            moves = generateMoves()
        else:
            moves.update(generateMoves())
        save(moves)

    play(moves)
    


def play(moves):
    print(moves)
    input("1 to Begin: ")
    board = ["E","E","E","E","E","E","E","E","E"]
    mover = "X"
    available = [0,1,2,3,4,5,6,7,8]
    while True:
        print(board[0:3])
        print(board[3:6])
        print(board[6:])
        print("\n \n")
        if mover == "X":
            play = input("Place your piece in an available position: ")
            while int(play) not in available:
                print("Position already taken. Try again.")
                play = input("Place your piece in an available position: ")
            board[int(play)] = mover
            available.remove(int(play))
            if verifyWin(board,mover):
                if prevOBoard != None:
                    moves["".join(prevOBoard)] = [int(play)]
                win = mover
                break
            elif "E" not in board:
                win = "DRAW"
                break

            mover = "O"
        else:
            moveCheck = "".join(board)
            if moveCheck in moves:
                play = None
                for i in moves[moveCheck]:
                    if i in available:
                        play = i
                if not play:
                    play = random.randint(0,len(available)-1)
                    play = available[play]
            else:
                play = random.randint(0,len(available)-1)
                play = available[play]
            prevOBoard = board.copy()
            board[play] = mover
            available.remove(play)
            if verifyWin(board,mover):
                win = mover
                break
            elif "E" not in board:
                win = "DRAW"
                break

            mover = "X"
    if win == "DRAW":
        print(win)
    else:
        print(win + " wins")
    print(board[0:3])
    print(board[3:6])
    print(board[6:])
    save(moves)

main()
    




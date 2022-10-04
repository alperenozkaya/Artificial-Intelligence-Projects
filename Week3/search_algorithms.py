"""
COMP450 Week-3 Search Algorithms
This code is about comptetition between Depth-First Search AI and Rule-Based AI systems on TicTacToe Game
"""

import random
from datetime import datetime


#Prints the given board to terminal
def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

#Method to determine winner
#Checks the current board and given letter while determining
def isWinner(board, letter):
    if board[7] == board[8] == board[9] == letter:  # across the top
        return True
    elif board[4] == board[5] == board[6] == letter:  # across the middle
        return True
    elif board[1] == board[2] == board[3] == letter:  # across the bottom
        return True
    elif board[1] == board[4] == board[7] == letter:  # down the left side
        return True
    elif board[2] == board[5] == board[8] == letter:  # down the middle
        return True
    elif board[3] == board[6] == board[9] == letter:  # down the right side
        return True
    elif board[7] == board[5] == board[3] == letter:  # diagonal
        return True
    elif board[1] == board[5] == board[9] == letter:  # diagonal
        return True
    else:
        return False

#Checks is the next move's space free.
#Returns boolean
def freeSpace(board,move):
    if board[move] == ' ':
        return True
    else:
        return False

#Does the given move
def makeAMove(board, letter, move):
    board[move] = letter

#Copies the board(dictionary) in the situation.
#This is for determining the next move by checking next probable moves.
def copyTheBoard(board):
    copiedBoard = board.copy()
    return copiedBoard

def isBoardFull(board):
    for i in board:
        if board[i] == ' ':
            return False
    return True

def findBestMove(board, xTurn):
    global playerLetter, computerLetter

    if not isBoardFull(board):
        if isWinner(board,playerLetter):
            return 1,-1
        elif isWinner(board,computerLetter):
            return -1,-1
        else:
            bestMove = -1
            result = -1 if xTurn else 1
            for i in range(1, 10):
                if not freeSpace(board, i):
                    continue

                board[i] = playerLetter if xTurn else computerLetter
                tempResult = (findBestMove(board, not xTurn))[0]
                board[i] = ' '

                if (xTurn & (tempResult > result)):
                    bestMove = i
                    result = tempResult
                elif (not xTurn) & (tempResult < result):
                    bestMove = i
                    result = tempResult

            return result, bestMove
    else:
        if isWinner(board, playerLetter):
            return 1,-1
        elif isWinner(board, computerLetter):
            return -1,-1
        else:
            return 0,-1


#The computer's move
#At first it checks can computer win, if it can, it does that move.
#If the user is going to win in next move, it prevents it by playing there.
#If noone is going to win in next move, try to take middle
#If middle is full take one of the mid of corners.
#If the middle corners are full take a corner
def getComputerMove(board,computerLetter,playerLetter):
    #This loop tries the every single free space for the next best move of computer
    for i in range(1,10):
        copiedBoard = copyTheBoard(board) #copy the board to try next moves
        if freeSpace(copiedBoard,i): #if space is free do the move as computer
            makeAMove(copiedBoard,computerLetter,i) #do the move on temporary board
            if isWinner(copiedBoard,computerLetter): #if that move gives you a win
                return i #choose that move

    # This loop tries the every single free space for the next best move of user
    # If user can win prevent it
    for i in range(1,10):
        copiedBoard = copyTheBoard(board)
        if freeSpace(copiedBoard,i):
            makeAMove(copiedBoard,playerLetter,i)
            if isWinner(copiedBoard,playerLetter):
                return i

    #Take the mid and break
    if theBoard[5] == ' ':
        return 5

    # Take one of the corners and break
    randomCornersList = [1,3,7,9]
    while len(randomCornersList) != 0:
        ran = random.choice(randomCornersList)
        if not freeSpace(theBoard,ran):
            randomCornersList.remove(ran)
        else:
            return ran

    #Take one of the mids of corners and break
    randomSidesList = [2,4,6,8]
    while True:
        ran = random.choice(randomSidesList)
        if not freeSpace(theBoard, ran):
            randomSidesList.remove(ran)
        else:
            return ran

playCount = 0 #Current number of rounds
totalNumberOfRounds = 999 #There will be 1000 rounds
playAgain = True #Is next round going to be played

#Count variables
playerWinCount = 0
computerWinCount= 0
tieCount = 0

#Time variables
totalTimeAlg = 0
totalTimeRule = 0
timerArrayRule = [0]*9
timerArrayAlg = [0]*9

print("Round: 1")

#Play dedicated number of matches(1000 match)
while playAgain:
    #Declare board and letters,
    # Rule based AI will always be X,
    # Depth First Search will always be O
    theBoard = {7: ' ', 8: ' ', 9: ' ',
                4: ' ', 5: ' ', 6: ' ',
                1: ' ', 2: ' ', 3: ' '}

    playerLetter = 'X'
    computerLetter = 'O'

    xTurn = True #Turn variable for Depth First AI
    turn = "player" #Turn variable for Rule based AI

    #In order to be fair each player will start equally numbers of time
    if playCount % 2 == 0:
        xTurn = True
        turn = 'player'
        print("Rule based will start")
    else:
        playerLetter = 'O'
        computerLetter = 'X'
        xTurn = False
        turn = 'computer'
        print("Search algorithm will start")


    timers = list() #To find each player used how much time for each move

    gameIsPlaying = True
    while gameIsPlaying:
        #Rule based AI's turn
        if xTurn == True and turn == "player":
            #This prints can be enabled to see how each round is going on
            # printBoard(theBoard)
            # print("\n")

            #Calculating total time spent for each round and move
            start = datetime.now()
            move = getComputerMove(theBoard, playerLetter, computerLetter)
            timers.append((int((datetime.now()-start).seconds*1000000+(datetime.now()-start).microseconds),"R"))#The R means rule based
            totalTimeRule += int((datetime.now()-start).seconds*1000000+(datetime.now()-start).microseconds)

            makeAMove(theBoard, playerLetter, move)

            #If there is a win or tie situation print it, increase counters and finish round
            #Else change turn variables to point other player's turn
            if isWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print(playerLetter,"is the winner\n")
                playerWinCount+=1
                gameIsPlaying = False
                # If there is no winner and board is full finish and write tie
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print("Its a tie\n")
                    tieCount+=1
                    break
                else:
                    turn = "computer"
                    xTurn = False

        #Depth First Search Algorithm AI's turn
        elif xTurn == False and turn == "computer":
            # This prints can be enabled to see how each round is going on
            # printBoard(theBoard)
            # print("\n")

            copyBoard = copyTheBoard(theBoard)

            #Time variables
            start = datetime.now()
            move = findBestMove(copyBoard, xTurn)[1]
            timers.append((int((datetime.now() - start).seconds * 1000000 + (datetime.now() - start).microseconds),"A"))#The A means rule based
            totalTimeAlg += int((datetime.now() - start).seconds * 1000000 + (datetime.now() - start).microseconds)

            makeAMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                printBoard(theBoard)
                print(computerLetter," is the winner\n")
                computerWinCount+=1
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print("Its a tie\n")
                    tieCount+=1
                    break
                else:
                    xTurn = True
                    turn = "player"

    #If there are not 1000 plays continue playing and store timers
    if playCount != totalNumberOfRounds:
        playCount+=1
        print("Round: ",playCount+1)

        for i in range(len(timers)):
            if((timers[i])[1] == "R"):
                timerArrayRule[i] += (timers[int(i)])[0]
            else:
                timerArrayAlg[i] += (timers[int(i)])[0]

        playAgain= True
    else:
        playAgain= False

print("Total Rounds: ", playCount)
print("Player Score: ",playerWinCount)
print("Computer Score: ",computerWinCount)
print("Tie : ",tieCount,"\n")


#Average time on each turn(not round) for Rule based algorithm
print("Rule Based")
for i in range(len(timerArrayRule)):
    timerArrayRule[i] = int(timerArrayRule[i])/(int((playCount)/2))
    if (i == 0):
        print("Average time of ", i + 1, "st move: ",timerArrayRule[i], " microseconds")
    elif(i ==1):
        print("Average time of ", i + 1, "nd move: ", timerArrayRule[i], " microseconds")
    elif (i == 2):
        print("Average time of ", i + 1, "rd move: ", timerArrayRule[i], " microseconds")
    else:
        print("Average time of ", i + 1, "th move: ", timerArrayRule[i], " microseconds")

#Average time on each turn for Depth First Search algorithm
print("\nSearch Algorithm")
for i in range(len(timerArrayRule)):
    timerArrayAlg[i] = int(timerArrayAlg[i])/((playCount)/2)
    if (i == 0):
        print("Average time of ", i + 1, "st move: ",timerArrayAlg[i], " microseconds")
    elif(i ==1):
        print("Average time of ", i + 1, "nd move: ", timerArrayAlg[i], " microseconds")
    elif (i == 2):
        print("Average time of ", i + 1, "rd move: ", timerArrayAlg[i], " microseconds")
    else:
        print("Average time of ", i + 1, "th move: ", timerArrayAlg[i], " microseconds")

print("\nTotal time cost of rule based search: ",totalTimeRule, " microseconds")
print("Total time cost of search algorithm based search: ",totalTimeAlg, " microseconds")
import random
import math

#Check and return all available moves for selected positions
def getAvailableMoves(board,pos):
    moves = list()
    if pos == 1:
        if not board[2] != '': moves.append(2)
        if board[3] == '' and board[2] == '': moves.append(3)
        if not board[4] != '': moves.append(4)
        if not board[5] != '': moves.append(5)
    elif pos == 2:
        if not board[1] != '': moves.append(1)
        if not board[3] != '': moves.append(3)
        if not board[4] != '': moves.append(4)
        if not board[5] != '': moves.append(5)
    elif pos == 3:
        if board[1] == '' and board[2] == '': moves.append(1)
        if not board[2] != '': moves.append(2)
        if not board[5] != '': moves.append(5)
    elif pos == 4:
        if not board[1] != '': moves.append(1)
        if not board[2] != '': moves.append(2)
        if not board[5] != '': moves.append(5)
    elif pos == 5:
        if not board[1] != '': moves.append(1)
        if not board[2] != '': moves.append(2)
        if not board[3] != '': moves.append(3)
        if not board[4] != '': moves.append(4)
    else:
        if not board[1] != '': moves.append(1)
        if not board[2] != '': moves.append(2)
        if not board[3] != '': moves.append(3)
        if not board[4] != '': moves.append(4)
        if not board[5] != '': moves.append(5)
    return moves

total = 0 #This is for node scores
copyTurn = 'player' #Checking current playing player
maxEvalPos = 0 #Best move's position


# Alpha beta pruning algorithm, it choses the fastest and reliable move
def minimax(board,posplayer,posai,depth,alpha,beta,ismax):
    #declaring variables
    global enemyLetter,playerLetter,total,copyTurn,maxEvalPos
    total = 0

    comT = getAvailableMoves(board,posai) #Available moves of computer
    humT = getAvailableMoves(board, posplayer) #Available moves of player

    if len(comT) == len(humT)== 0:
        if copyTurn == 'computer': #If both doesn't have any moves and next turn is computer's, its a lose of score
            total -= 1
            return total
        else:
            total += 1
            return total

    elif len(comT) == 0: #If pc doesn't have any moves, its a lose of score
        total -= 1
        return total
    elif len(humT) == 0: #If human doesn't have any moves, its a win of score
        maxEvalPos = comT[0]
        total += 1
        return total

    #If player is maximizing on tree
    if ismax:
        maxEval = -math.inf
        children = getAvailableMoves(board,posai) # All children nodes of selected node
        # Check every single child of Player moves and calculate scores
        for child in children:
            board[child] = enemyLetter # Put the letter for trying the move
            oldposai = posai # Hold old position to use it later
            posai = child # change ai's position to try new child
            copyTurn = 'player' # change playing player
            eval = minimax(board,posplayer,posai,depth-1,alpha,beta,False)
            posai = oldposai # after each evaluation give its first value to ai's pos again
            board[child] = '' # clear the move
            if eval > maxEval:
                maxEval = eval
                maxEvalPos = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    #This is for minimizing nodes
    else:
        minEval = math.inf
        children = getAvailableMoves(board, posplayer)
        for child in children:
            board[child] = playerLetter
            oldposplayer = posplayer
            posplayer = child
            copyTurn = 'computer'
            eval = minimax(board, posplayer, posai, depth - 1, alpha, beta, True)
            posplayer = oldposplayer
            board[child] = ''
            if eval < minEval:
                minEval = eval
            #minEval = min(minEval, eval)
            alpha = min(alpha, eval)
            if beta <= alpha:
                break
        return minEval

#Take the player's move till he/she choses a unfilled position.
def getPlayerMove(board):
    global playerLetter,lastHumPos,flag1
    while True:
        availables = getAvailableMoves(board, lastHumPos)
        printBoard(board)
        print("Your available moves are, ", availables)
        #This if is for win-lose-tie situations.
        if len(availables) == 0:
            flag1 = True
            break
        x = int(input("Where do you want to play to?\n"))
        if x in availables:
            board[x] = playerLetter
            lastHumPos= x #Last seen position of human
            break
        else:
            print("This place is full, select new one\n")

#Get computer's move, run the minimax
def getComputerMove(board):
    global enemyLetter,lastAiPos,flag2
    availables = getAvailableMoves(board, lastAiPos)
    print("\nComputer's available moves are, ", availables)
    # This if is for win-lose-tie situations.
    if len(availables) == 0:
        flag2 = True

    minimax(board,lastHumPos,lastAiPos, 5,-math.inf,math.inf,True)
    x = maxEvalPos
    lastAiPos = x #last seen position of ai, we are using this because minimax changes the value
    board[x] = enemyLetter
    print("Computer played to,[", x ,"]\n")


#Check if is board full to determine win lose, tie
def isBoardFull(board):
    for i in board:
        if board[i] == '':
            return False
    return True

def printBoard(board):
    list1 = [board[1],board[2],board[3]]
    list2 = [board[4],board[5]]
    print(list1)
    print(list2)



#Determining values
theBoard = {1:'',2:'',3:'',4:'',5:''}
isGamePlaying = True

playerLetter = 'X'
enemyLetter = 'O'
turn = 'player'

lastHumPos = None
lastAiPos = None

flag1= False
flag2= False

# These are for chosing starter
ran = random.randint(0, 1)
if ran == 1:
    playerLetter = 'O'
    enemyLetter = 'X'
    print("Computer Goes First")
    turn = 'computer'
else:
    print("Player Goes First")


while isGamePlaying:
    # If both players don't have any moves left
    if flag1 == flag2 == True:
        #Check if board is full, if not its a tie
        if isBoardFull(theBoard) == False:
            print("Tie")
            break
        # If board is full and last player played lastly its a win, else its a lose
        else:
            if turn == 'computer':
                print("Win")
                break
            else:
                print("Lose")
                break
    #If player doesn't have any moves but computer have
    elif flag1 == True and flag2 == False :
        #Check is there any possible move for ai
        availables = getAvailableMoves(theBoard, lastAiPos)
        if len(availables) == 0:
            flag2 = True
        #If there is a move for ai, its a lose for human
        else:
            print("Lose")
            break
    #If human starts from a corner he can win, middle is a lose or tie for human
    elif flag1 == False and flag2 == True:
        availables = getAvailableMoves(theBoard, lastHumPos)
        #This is for tie situation
        if len(availables) == 0:
            flag1 = True


    #Do moves
    if turn == 'player':
        print("Player's turn")
        getPlayerMove(theBoard)
        turn = 'computer'
    elif turn == 'computer':
        getComputerMove(theBoard)
        turn = 'player'


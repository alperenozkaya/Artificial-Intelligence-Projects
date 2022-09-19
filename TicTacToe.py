import random as rn

def main():
    grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']] # 3x3 grid

    usrInput = [0, 0]
    edges = [[0, 1], [1, 0], [1, 2], [2, 1]] # edges of the grid
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]] # corners of the grid

    printGrid(grid)

    print("Computer's turn")
    compSelection = [1, 1]
    playComp(compSelection, grid)

# first turn
    while True:
       print("Your turn. Please enter coordinates.")
       usrInput = input().split()
       usrInt = [int(x) for x in usrInput]
       usrInput = usrInt
       if (grid[usrInput[0]][usrInput[1]] != '-'):
           print("This tile is already used.")
           continue
       else:
           grid[usrInput[0]][usrInput[1]] = 'O'
           if (usrInput in edges):  # user selects an edge.
               ## Selects one of the furthest corners furthest from the selected edge.
               if usrInput == [1, 0]:
                   compSelection = corners[rn.choice([1, 3])]
               elif usrInput == [1, 2]:
                   compSelection = corners[rn.choice([0, 2])]
               elif usrInput == [0, 1]:
                   compSelection = corners[rn.choice([2, 3])]
               elif usrInput == [2, 1]:
                   compSelection = corners[rn.choice([0, 1])]
           elif (usrInput in corners):  # user selects a corner.
               ## Selects the opposite corner selected by the user.
               if usrInput == [0, 0]:
                   compSelection = [2, 2]
               elif usrInput == [0, 2]:
                   compSelection = [2, 0]
               elif usrInput == [2, 0]:
                   compSelection = [0, 2]
               elif usrInput == [2, 2]:
                   compSelection = [0, 0]
           break

    playComp(compSelection, grid)# plays the turn based on the decision made aboe
    printGrid(grid)


    while True:
        # Player's second turn
        print("Your turn, please enter coordinates.")
        usrInput = input().split()
        usrInt = [int(x) for x in usrInput]
        usrInput = usrInt
        if grid[usrInput[0]][usrInput[1]] != '-':
            print("This tile is already used.")
            continue
        else:
            grid[usrInput[0]][usrInput[1]] = 'O'
            printGrid(grid)

        if not checkGrid(grid): # if nothing is placed, sabotages player.
            if not blockPlayer(grid): # if nothing to sabotage, places a random X
                play_random(grid)


def printGrid(grid):# this function simply prints the grid and does nothing else.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = " ")
        print("")


def playComp(selected, grid): # this function places an X to the selected coordinate of the grid.
    grid[selected[0]][selected[1]] = 'X'
    printGrid(grid)

# checks the current grid and puts an X for the computer whenever sees 2 X's and a blank space in
# a row/ column/ diagonal line
def checkGrid(grid):
    # makes a horizontal search
    for i in range(3):
        counter = 0 # to count number o x's in a row
        for j in range(3):
            if grid[i][j] == 'O': # if an O is encountered, decrease counter
                counter -=1
            elif grid[i][j] =='X': # if an X is encountered, increase counter.
                counter +=1
        if counter == 2: # if there are 2 x's in a row and nothing else, fills the blank space.
            for j in range(3):
                if grid[i][j] == '-':
                    playComp([i, j], grid)
            return True

    # this bit does exactly the same thing with above, but with columns.
    for i in range(3):
        counter = 0
        for j in range(3):
            if grid[j][i] == 'O':
                counter -= 1
            elif grid[j][i] == 'X':
                counter += 1
            if counter == 2:
                for j in range(3):
                    if grid[j][i] == '-':
                        playComp([j, i], grid)
                return True

    # checks the diagonal line to try to draw the line as a last attempt.
    if grid[0][0] == 'X' and grid[2][2] == '-':
        playComp([2, 2], grid)
    elif grid[2][2] == 'X' and grid[0][0] == '-':
        playComp([0, 0], grid)
    elif grid[0][2] == 'X' and grid[2][0] == '-':
        playComp([2, 0], grid)
    elif grid[2][0] == 'X' and grid[0][2] == '-':
        playComp([0, 2], grid)
    else:
        return False # if nothing is placed, returns false.

    return True # if diagonal lining is successful, returns true.


# function that place x into an appropriate square to block
# the player's row
def blockPlayer(grid):
    # nested for loop to check rows
    for i in range(3):
        counter = 0
        for j in range(3):
            if grid[i][j] == 'X':
                counter -= 1
            elif grid[i][j] == 'O':
                counter += 1
            if counter == 2:
                for j in range(3):
                    if grid[i][j] == '-':
                        playComp([i, j], grid)
                return True
    # nested for loop to check columns
    for i in range(3):
        counter = 0
        for j in range(3):
            if (grid[j][i] == 'X'):
                counter -= 1
            elif (grid[j][i] == 'O'):
                counter += 1
            if (counter == 2):
                for j in range(3):
                    if grid[j][i] == '-':
                        playComp([j, i], grid)
                return True
    # statements to check possible diagonal rows
    if grid[0][0] == 'O' and grid[2][2] == '-':
        playComp([2, 2], grid)
    elif grid[2][2] == 'O' and grid[0][0] == '-':
        playComp([0, 0], grid)
    elif grid[0][2] == 'O' and grid[2][0] == '-':
        playComp([2, 0], grid)
    elif grid[2][0] == 'O' and grid[0][2] == '-':
        playComp([0, 2], grid)
    else:
        return False
    return True

# function to let AI keep playing after all possible win and
# lose conditions are exhausted (couldn't implement it properly)
def play_random(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '-':
                playComp([i, j], grid)

if __name__ == '__main__':
    main()

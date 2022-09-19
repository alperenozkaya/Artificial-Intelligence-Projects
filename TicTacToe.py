import random as rn

def main():
    grid = [['-','-','-'], ['-','-','-'], ['-','-','-']] # 3x3 grid

    usrInput = [0, 0]

    edges = [[0, 1], [1, 0], [1, 2], [2, 1]]
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]

    printGrid(grid)

    print("Computer's turn")
    compSelection = [1, 1]
    playComp(compSelection, grid)

    compLastTurn = []

    while(True):
        print("Your turn. Please enter coordinates.")

        usrInput = input().split()
        usrInt = [int(x) for x in usrInput]
        usrInput = usrInt
        if (grid[usrInput[0]][usrInput[1]] == 'X' or grid[usrInput[0]][usrInput[1]] == 'O'):
            print("This tile is already used.")
            continue
        else:
            grid[usrInput[0]][usrInput[1]] = 'O'

        printGrid(grid);

        if (usrInput in edges): #user selects an edge.
            compSelection = corners[rn.randint(0, 2)]
            if len(compLastTurn) == 0:
                playComp(compSelection, grid)
            else:
                compSelection[0] = compLastTurn[1]
                compSelection[1] = compLastTurn[0]

                if compSelection[0] == 0 and compSelection[1] == 0:
                    compSelection = [2, 2]

                elif compSelection[0] == 2 and compSelection[1] == 2:
                    compSelection = [0, 0]

                playComp(compSelection, grid)

        compLastTurn = compSelection
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = " ")
        print("")

def playComp(selected, grid):
    grid[selected[0]][selected[1]] = 'X'
    printGrid(grid)

if __name__ == '__main__':
    main()
import random
from copy import copy, deepcopy



def main():
    # '-' means the spot is not filled, while '/' indicates
    # the spot cannot be filled or already occupied
    grid = [['-', '-', '-'], ['-', '-', '/']]
    print_grid(grid)
    comp_last_position = [99, 99] # initial position

    print("Computer's turn")
    comp_last_position = computer_initial_play(grid, comp_last_position)
    print_grid(grid)

    while True:
        print("Your turn. Please enter coordinates.")
        usrInput = input().split()
        usrInt = [int(x) for x in usrInput]
        usrInput = usrInt
        if grid[usrInput[0]][usrInput[1]] != '-':
            print_grid()
            print("This tile is already used.")
            continue
        else:
            grid[usrInput[0]][usrInput[1]] = 'X'
        print_grid(grid)
        print("Computer's turn")
        play_comp(grid, comp_last_position)
        print_grid(grid)

        #print(comp_last_position)


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print("")


def play_comp(grid, comp_last_position): # agent randomly plays

    possible_spots = check_grid_status(grid, comp_last_position)
    #print(possible_spots)
    random_spot = random.randint(0, len(possible_spots) - 1)
    grid[possible_spots[random_spot][0]][possible_spots[random_spot][1]] = 'O'


def computer_initial_play(grid, comp_last_position): # initial agent play
    rand_position = (random.randint(0, 1), random.randint(0, 2))

    if grid[rand_position[0]][rand_position[1]] != '-':
        computer_initial_play(grid, comp_last_position)
        comp_last_position # to fix the error not used
    else:
        grid[rand_position[0]][rand_position[1]] = 'O'
        comp_last_position[0] = [rand_position[0]]
        comp_last_position[0] = [rand_position[1]]
        return comp_last_position


def check_grid_status(grid, last_position):
    boolean_grid = deepcopy(grid)
    for i in range(0, 2):
        for j in range(0, 3):
            if grid[i][j] == '-':
                boolean_grid[i][j] = True
            else:
                boolean_grid[i][j] = False
    print_grid(boolean_grid)
    #find_possible_spots(boolean_grid, last_position)

    possible_spots = [[], [], [], []]
    spot_counter = 0

    if last_position[0] == 0 and last_position[1] == 0:

        for i in range(1, 3):
            if boolean_grid[0][1] == False:
                boolean_grid[0][2] = False
    elif last_position[0] == 0 and last_position[1] == 2:
        boolean_grid[1][0] = False
        for i in range(2, 0):
            if boolean_grid[0][1] == False:
                boolean_grid[0][0] = False

    for i in range(0, 2):
        for j in range(0, 3):
            if boolean_grid[i][j] == True:
                possible_spots[spot_counter] = [i, j]
                spot_counter = spot_counter + 1
                #print(possible_spots)
                #print('')
            else:
                continue

    possible_spots = list(filter(None, possible_spots))
    #print(possible_spots)
    return possible_spots


if __name__ == '__main__':
    main()




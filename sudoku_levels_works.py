import os
import sys
import pickle
from copy import deepcopy
from grids import easy, medium, hard, win0, winwin
os.system("clear")

# original numbers color (lol, álmodik a nyomor)
cbegin = "\033[34m"
cend = "\033[0m"

# grid color
gbegin = "\033[90m"
gend = "\033[0m"

# error color
ebegin = "\033[91m"
eend = "\033[0m"

# original grid, not to be modified
grid0 = []

# second grid, zeros can be modified
grid = []

# row and column indexing
index_cap = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
index_small = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}

# error messages used
error1 = "\nThis number is already in that row."
error2 = "\nThis number is already in that column."
error3 = "\nOriginal board cannot be modified."
error4 = "\nNumber must be between 1 and 9."
error5 = "\nPlease enter a number from the list below."
error6 = "\nPlease enter either \"y\" or \"n\" after choosing save."
error7 = "\nPlease enter requested characters."
error8 = "\nThis number is already in that grid."


# middle part of long print line in print_sudoku
def long_line():
    return (" {} " + gbegin + "│" + gend + " {} " + gbegin + "│" + gend + " {} " + gbegin + "║" + gend)


# printing the original grid
def print_sudoku(board):
    print(gbegin + "\n    a   b   c   d   e   f   g   h   i  " + gend)
    print(gbegin + "  ╔" + ("═══╤═══╤═══╦"*2) + "═══╤═══╤═══╗" + gend)
    for i, row in enumerate(board):
            print((gbegin + "{} ║" + gend + (long_line())*3).format(*[x if x != 0 else " " for x in row]))
            if i % 3 == 2 and i < 8:
                print(gbegin + "  ╠" + ("═══╪═══╪═══╬"*2) + "═══╪═══╪═══╣" + gend)
            elif i == 8:
                print(gbegin + "  ╚" + ("═══╧═══╧═══╩"*2) + "═══╧═══╧═══╝" + gend)
            else:
                print(gbegin + "  ╟" + ("───┼───┼───╫")*2 + "───┼───┼───╢" + gend)


# printing a new grid after adding a new number
def grid_new(board):
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    num = int(input("Enter a number (1-9): "))
    os.system("clear")
    if num in board[int(index_cap[row_in]) - 1]:  # checking row
        print(ebegin + error1 + eend)
    elif num in [col[int(index_small[column_in])] for col in board]:  # checking column
        print(ebegin + error2 + eend)
    elif row_in in ["A", "B", "C"] and column_in in ["a", "b", "c"]:
        for grid1_1 in [board[0][1:4], board[1][1:4], board[2][1:4]]:
            if num in grid1_1:
                print(ebegin + error8 + eend)
    elif row_in in ["A", "B", "C"] and column_in in ["d", "e", "f"]:
        for grid1_2 in [board[0][4:7], board[1][4:7], board[2][4:7]]:
            if num in grid1_2:
                print(ebegin + error8 + eend)
    elif num > 0 and num < 10:  # checking if number is between 1 and 9
        if grid0[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] == 0:
            board[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] = num
        else:
            print(ebegin + error3 + eend)
    else:
        print(ebegin + error4 + eend)
    return board


# deleting a number
def grid_delete(board):
    print("\nDefine place for number to delete.")
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    if grid0[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] == 0:
        board[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] = 0
    else:
        print(ebegin + error3 + eend)
    os.system("clear")
    return board


# menu1 & menu2
while True:
    print(cbegin + """
  ____                _           _                _____       _
 / ___|   _   _    __| |   ___   | | __  _   _    |___ /      / |
 \___ \  | | | |  / _` |  / _ \  | |/ / | | | |     |_ \      | |
  ___) | | |_| | | (_| | | (_) | |   <  | |_| |    ___) |  _  | |
 |____/   \__,_|  \__,_|  \___/  |_|\_\  \__,_|   |____/  (_) |_|

    """ + cend)
    print("\nWelcome to the Sudoku Game!\nMenu:")
    print("[1] Print New Board")
    print("[2] Load Saved Game")
    try:
        action = int(input("\nWhat would you like to do? "))
        if action == 1:
            os.system("clear")
            print("\n[1] Easy")
            print("[2] Medium")
            print("[3] Hard")
            action2 = int(input("\nChoose a level! "))
            if action2 == 1:
                grid0 = easy
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
            elif action2 == 2:
                grid0 = medium
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
            elif action2 == 3:
                grid0 = hard
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
            elif action2 == 4:
                grid0 = win0
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
        elif action == 2:
            os.system("clear")
            file = "saved_sudoku.pickle"
            with open(file, "rb") as f:
                grid0 = pickle.load(f)
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
        else:
            os.system("clear")
            print(ebegin + error5 + eend)
    except ValueError:
        os.system("clear")
        print(ebegin + error5 + eend)


# menu3
while True:
    if grid == winwin:  # winning
        print(cbegin + """
     __        __  ___   _   _   _
     \ \      / / |_ _| | \ | | | |
      \ \ /\ / /   | |  |  \| | | |
       \ V  V /    | |  | |\  | |_|
        \_/\_/    |___| |_| \_| (_)

    """ + cend)
        break
    else:
        print("\n[1] Add number")
        print("[2] Delete number")
        print("[3] Save game")
        print("[4] Exit game")
        try:
            action3 = int(input("\nWhat would you like to do? "))
            try:
                if action3 == 1:
                    grid = grid_new(grid)
                    print_sudoku(grid)
                elif action3 == 2:
                    grid = grid_delete(grid)
                    print_sudoku(grid)
                elif action3 == 3:
                    file = "saved_sudoku.pickle"
                    with open(file, "wb") as f:
                        pickle.dump(grid, f)
                    saving = input("Are you sure you want to save and quit? (y/n)")
                    if saving == "y":
                        os.system("clear")
                        print("Sudoku game saved!\n")
                        break
                    elif saving == "n":
                        os.system("clear")
                        print_sudoku(grid)
                    else:
                        os.system("clear")
                        print(ebegin + error6 + eend)
                        print_sudoku(grid)
                elif action3 == 4:
                    break
                else:
                    os.system("clear")
                    print(ebegin + error5 + eend)
                    print_sudoku(grid)
            except ValueError:
                os.system("clear")
                print(ebegin + error7 + eend)
                print_sudoku(grid)
        except ValueError:
            os.system("clear")
            print(ebegin + error5 + eend)
            print_sudoku(grid)

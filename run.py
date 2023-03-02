from random import randint


HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [[" "] * 8 for x in range(8)]


char_to_num = {
    "A": 0, "B": 1,
    "C": 2, "D": 3,
    "E": 4, "F": 5,
    "G": 6, "H": 7
    }


def print_board(board):
    print("    A B C D E F G H")
    print("    ---------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Please enter a ship row 1-8: ")
    while row not in "12345678":
        print("Please enter a valid row")
        row = input("Please enter ship row 1-8: ")
    column = input("Please enter a ship column A-H: ").upper()
    while column not in "ABCDEFGH":
        print("Please enter a valid column: ")
        column = input("Please enter a ship column A-H: ").upper()
    return int(row) - 1, char_to_num[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
TURNS = 10
while TURNS > 0:
    print("Welcome to battleships")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-":
        print("You already guessed that")
    elif HIDDEN_BOARD[row][column] == "X":
        print("Congrats --- You have a hit")
        GUESS_BOARD[row][column] = "X"
        TURNS -= 1
    else:
        print("YOU MISSED")
        GUESS_BOARD[row][column] = "-"
        TURNS -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congrats, You sunk all the battleships")
        break
        print("You have " + str(TURNS) + "turns remaining")
    if TURNS == 0:
        print("Games Over you ran out of turns.")
        break


import random
import time

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("battleship_leaderboard")


class welcome_screen():

    def __init__(self):
        pass

    print("-----------------------------------------")
    print("          Welcome to Battleship          ")
    print("-----------------------------------------\n")
    print("                                         \n")
    print("                                         ")
    print("             |    |    |                 ")
    print("            )_)  )_)  )_)                ")
    print("           )___))___))___)               ")
    print("          )____)____)_____)              ")
    print("        _____|____|____|______           ")
    print("--------\                    /-----------")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("      ^^^^      ^^^^     ^^^    ^^       ")
    print("^^^^^     ^^^^      ^^^     ^^^^^    ^^^^")
    time.sleep(2)
    while True:
        name = input("Enter name here: \n")
        if not name.isalpha():
            print("Invalid Input. Please use letters for your name")
        else:
            break
        print(f"Welcome to the game of Battleships {name} ")

    def display_menu(self):
        print("What would you like to do?")
        print("1. Play Game")
        print("2. Read Rules")
        print("3. Look at Leaderboard")

    def handle_choice(self, choice):
        if choice == "1":
            print("Loading Game", end="")
            for choice in range(15):
                time.sleep(.5)
                print(".", end="", flush=True)
            self.run_game()
        elif choice == "2":
            self.read_rules()
            input("Press Enter to Return to menu \n")
            self.display_menu()
            self.get_choice()
        elif choice == "3":
            self.look_at_leaderboard()
            input("Press Enter to Return to menu \n")
            self.display_menu()
            self.get_choice()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to try again \n")
            self.display_menu()
            self.get_choice()

    def get_choice(self):
        choice = input("Enter your choice (1, 2, or 3): \n")
        self.handle_choice(choice)

    def run_game(self):
        print("Loading Complete...")
        time.sleep(2)

    def read_rules(self):
        with open("rules.txt", "r") as f:
            print(f.read())

    def look_at_leaderboard(self):
        leaderboard_1 = SHEET.worksheet("leaderboard_1")
        data = leaderboard_1.get_all_values()
        print(data)


menu = welcome_screen()
menu.display_menu()
menu.get_choice()


class GameBoard:

    def __init__(self, board):
        self.board = board

    def get_char_to_num():
        char_to_num = \
            {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return char_to_num

    def print_board(self):
        print("  A B C D E F G H")
        print("  ---------------")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for create_ships in range(5):
            self.x_row, self.y_column = random.randint(0, 7),\
                random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7),\
                     random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        while True:
            try:
                x_row = input("Please enter a ship row 1-8: \n")
                while x_row not in "12345678":
                    print("Please enter a valid row")
                    x_row = input("Please enter ship row 1-8: \n")

                y_column = input("Please enter a ship column A-H: \n").upper()
                while y_column not in "ABCDEFGH":
                    print("Please enter a valid column: ")
                    y_column = input("Please enter a ship column A-H: \n")\
                        .upper()

                return int(x_row) - 1, GameBoard.get_char_to_num()[y_column]

            except (ValueError, KeyError):
                print("Not a valid input")

    def count_hit_ships(self):
        hit_count = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_count += 1
        return hit_count


class RunGame():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    # starts the game with 10 available turns
    TURNS = 10
    while TURNS > 0:
        GameBoard.print_board(user_guess_board)
        GameBoard.print_board(computer_board)
        # gets the Users input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        # checks if the guess is not a duplicated selection
        while user_guess_board.board[user_x_row][user_y_column] == "-" or \
                user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You guess those spaces already")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # Check to see for a Hit or miss from your guess
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk 1 of my battleships!!!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed my battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit all my battleships!!")
            break
        else:
            TURNS -= 1
            print(f"You have {TURNS} turns remaining")
            if TURNS == 0:
                print("Game Over - No turns left")
                GameBoard.print_board(user_guess_board)
                break


def main_game_run():
    welcome_screen()
    RunGame()


main_game_run()

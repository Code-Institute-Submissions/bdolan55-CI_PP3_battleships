import random
import time
import colorama
from colorama import Fore
import gspread
from google.oauth2.service_account import Credentials
colorama.init(autoreset=True)

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
    print(Fore.RED + "          Welcome to Battleship          ")
    print("-----------------------------------------\n")
    print("                                         \n")
    print("                                         ")
    print("             |    |    |                 ")
    print("            )_)  )_)  )_)                ")
    print("           )___))___))___)               ")
    print("          )____)____)_____)              ")
    print("        _____|____|____|______           ")
    print("        \                    /           ")
    print(Fore.BLUE + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(Fore.BLUE + "      ^^^^      ^^^^     ^^^    ^^       ")
    print(Fore.BLUE + "^^^^^     ^^^^      ^^^     ^^^^^    ^^^^")
    time.sleep(.5)
    while True:
        name = input(Fore.GREEN + "Enter name here: \n")
        if not name.isalpha():
            print(Fore.RED + "Invalid Input. Please use letters for your name")
        else:
            break
        print(f"{Fore.GREEN}Welcome to the game of Battleships {name} ")

    def display_menu(self):
        print(Fore.WHITE + "What would you like to do?")
        print("1. Play Game")
        print("2. Read Rules")
        print("3. Look at Leaderboard")

    def handle_choice(self, choice):
        if choice == "1":
            print(Fore.YELLOW + "Loading Game", end="")
            for choice in range(1):
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
            print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to try again \n")
            self.display_menu()
            self.get_choice()

    def get_choice(self):
        choice = input("Enter your choice (1, 2, or 3): \n")
        self.handle_choice(choice)

    def run_game(self):
        print(Fore.GREEN + "\nLoading Complete!! \n")
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

    @staticmethod
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
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7),\
                random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7),\
                     random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        # while True:
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
            print(Fore.RED + "Not a valid input")
            return self.get_user_input()

    # def get_comp_guess(self):
    #     x_row, y_column = random.randint(0, 7), random.randint(0, 7)
    #     return x_row, y_column

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
    # Battleship.create_ships(user_guess_board)
    # starts the game with 10 available turns
    TURNS = 10
    while TURNS > 0:
        GameBoard.print_board(user_guess_board)
        # gets the Users input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        # checks if the guess is not a duplicated selection
        while user_guess_board.board[user_x_row][user_y_column] == "-" or \
                user_guess_board.board[user_x_row][user_y_column] == "X":
            print(Fore.YELLOW + "You guess those spaces already")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # Check to see for a Hit or miss from your guess
        if computer_board.board[user_x_row][user_y_column] == "X":
            print(Fore.GREEN + "You sunk 1 of my battleships!!!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print(Fore.RED + "You missed my battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print(Fore.GREEN + "You hit all my battleships!!")
            break
        else:
            TURNS -= 1
            print(f"{Fore.BLUE}You have {TURNS} turns remaining")
            if TURNS == 0:
                print(Fore.RED + "Game Over - No turns left")
                GameBoard.print_board(user_guess_board)
                break
        # # Computers turn   
        # print("Now its the computers turn....")
        # comp_x_row, comp_y_column = Battleship.get_comp_guess(computer_board)
        # print(f"Computer Guessed Row {comp_x_row+1},column {comp_y_column}")

        # if user_guess_board.board[comp_x_row][comp_y_column] == "X":
        #     print("The computer sunk 1 of your Battleships!!")
        #     # computer_board.board[comp_x_row][comp_y_column] == "X"
        #     GameBoard.print_board(user_guess_board)
        #     Battleship.get_user_input(object)
            
        # else:
        #     print("The Computer missed your Battleship")
        #     computer_board.board[comp_x_row][comp_y_column] = "-"
        #     GameBoard.print_board(user_guess_board)
        #     Battleship.get_user_input(object)

        # if Battleship.count_hit_ships(user_guess_board) == 5:
        #     print("You hit all my ships!!")
        #     break

        # elif Battleship.count_hit_ships(computer_board) == 5:
        #     print("The computer hit all your ships!!")
        #     break
        

def main_game_run():
    welcome_screen()
    RunGame()


if __name__ == "__main__":

    main_game_run()

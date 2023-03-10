# Function of the Game and code was inspired and altered
# from https://www.youtube.com/watch?v=alJH_c9t4zw by Knowledge Mavens
"""
Python inbuilt random module to make reandom selection and import colorama
for color on text
"""
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


class WelcomeScreen():
    """
    Welcome screen class containing the menu choice functions,
    Rules function and Leaderboard function.

    """
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
    print("       /                    /            ")
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
        """
        Function to print Menu for game in sequence for the choice function
        to handle the player decision.
        """
        print(Fore.WHITE + "What would you like to do?")
        print("1. Play Game")
        print("2. Read Rules")
        print("3. Look at Leaderboard")

    def handle_choice(self, choice):
        """
        This function displays Game Menu.
        The function takes in a choice parameter, which is a string
        representing the user's choice of action.
        """
        if choice == "1":
            print(Fore.YELLOW + "Loading Game", end="")
            for choice in range(5):
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
        """
        Function handles the player input and relays input to
        handle choice function
        """
        choice = input("Enter your choice (1, 2, or 3): \n")
        self.handle_choice(choice)

    def run_game(self):
        """
        Function runs a loading message to terminal when player
        chooses run Game handle choice function
        """
        print(Fore.GREEN + "\nLoading Complete!! \n")
        time.sleep(2)

    def read_rules(self):
        """
        Function runs the rules.txt file and displays
        the rules to the terminal
        """
        with open("rules.txt", "r") as f:
            print(f.read())

    def look_at_leaderboard(self):
        """
        Function runs sends a request to the leaderboard Gsheet linked
        and loads the leaderboard into the terminal for player to view.
        """
        leaderboard_1 = SHEET.worksheet("leaderboard_1")
        data = leaderboard_1.get_all_values()
        print(data)


menu = WelcomeScreen()
menu.display_menu()
menu.get_choice()


class GameBoard:
    """
    GameBoard class is conatins the functions and methods to
    to build the GameBoard/Grid.
    """
    def __init__(self, board):
        self.board = board

    @staticmethod
    def get_char_to_num():
        """
        Method that returns a dictionary that maps the column letters
        of the Gameboard (A-H) to their corresponding
        numbers (0 to 7).
        """
        char_to_num = \
            {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return char_to_num

    def print_board(self):
        """
        Prints the Game board to the console. The method prints the column
        letters on the first row, and then prints each row of the Game
        board, separated by pipes (|) and with the row number printed
        at the beginning of each row. .
        """
        print("  A B C D E F G H")
        print("  ---------------")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """
    Handles the functions to randomly place ships throughout the game and
    handles the players input choice.
    """
    def __init__(self, board, x_row, y_column):
        self.board = board
        self.x_row = x_row
        self.y_column = y_column

    def create_comp_ships(self):
        """
        Randomly places computer ships locations on the board by generating
        random row and column values until a valid position is found.
        The position is marked on the board with an "O" character.
        """
        for i in range(10):
            x_row, y_column = random.randint(0, 7),\
                random.randint(0, 7)
            while self.board[x_row][y_column] == "O":
                x_row, y_column = random.randint(0, 7),\
                     random.randint(0, 7)
            self.board[x_row][y_column] = "O"
        return self.board

    def create_ships(self):
        """
        Randomly places players ships on the board by generating
        random row and column values until a valid position is found.
        The position is marked on the board with an "." character.
        """
        for i in range(10):
            self.x_row, self.y_column = random.randint(0, 7),\
                random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == ".":
                self.x_row, self.y_column = random.randint(0, 7),\
                     random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "."
        return self.board

    def get_user_input(self):
        """
        Prompts the user to enter a row and column for their attack,
        validates the input, and returns the corresponding row and
        column indices on the board.
        """
        while True:
            try:
                x_row = input("Please enter a ship row 1-8: \n")
                while x_row not in "12345678" and x_row != "":
                    print("Please enter a valid row")
                    x_row = input("Please enter ship row 1-8: \n")

                y_column = input("Please enter a ship column A-H: \n").upper()
                while y_column not in "ABCDEFGH" and y_column != "":
                    print("Please enter a valid column: ")
                    y_column = input("Please enter a ship column A-H: \n")\
                        .upper()

                if x_row != "" and y_column != "":
                    return int(x_row) - 1,\
                         GameBoard.get_char_to_num()[y_column]

            except (ValueError, KeyError):
                print(Fore.RED + "Not a valid input")

    @staticmethod
    def get_computer_input():
        """
        Generates and returns random row and column for a computer attack.
        """
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        return row, col

    def count_hit_ships(self):
        """
        Returns the number of user ships that have been hit
        and marked with an "X" on the board..
        """
        hit_count = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_count += 1
        return hit_count


class RunGame():
    """
    The Run game handles the above classes and functions and
    enables the game play of the Game Battleships. Starts the game with
    10 available turns. Prints the blank users guess game board to terminal,
    Prompts the user to input there guess in row and column, Checks if the
    input has been entered before and then prints back to terminal if it is
    a hit or miss and how many turns remain. It then does the same above
    randomly for the computers guess and prints to terminal if the computer
    has hit or miss any of the players ships. After both the player and
    computer have guessed it will print the current score to the terminal and
    repeat the above until all turns are gone or all ships are hit. After
    all turns have been taken a Game Over message will appear and shows
    the final scores of the game for both player and computer.
    """
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    player_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    Battleship.create_comp_ships(user_guess_board)
    # starts the game with 10 available turns
    TURNS = 10
    while TURNS > 0:
        GameBoard.print_board(player_guess_board)
        # gets the Users input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        # checks if the guess is not a duplicated selection
        while user_guess_board.board[user_x_row][user_y_column] == "-" or \
                user_guess_board.board[user_x_row][user_y_column] == "X":
            print(Fore.YELLOW + "You guess those spaces already")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # Check to see for a Hit or miss from your guess
        if user_guess_board.board[user_x_row][user_y_column] == "O":
            print(Fore.GREEN + "You have sunk 1 of the computers battlesips")
            user_guess_board.board[user_x_row][user_y_column] = "X"
            player_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print(Fore.RED + "You missed the computer battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
            player_guess_board.board[user_x_row][user_y_column] = "-"
        # check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 10:
            print(Fore.GREEN + "You hit all Computers battleships!!")
            break
        else:
            TURNS -= 1
            print(f"{Fore.BLUE}You have {TURNS} turns remaining")
            if TURNS == 0:
                print("--------------------------------------")
                print(Fore.RED + "       Game Over - No turns left")
                print("--------------------------------------")
                print(" ")
                print("Player with the most Ship Hits wins!!!")
                print(" ")
                score_1 = Battleship.count_hit_ships(user_guess_board)
                print(Fore.GREEN + "Player Score: " + str(score_1))
                score_2 = Battleship.count_hit_ships(computer_board)
                print(Fore.GREEN + "Computer Score: " + str(score_2))
                print("")
                print("See loactions of the Players missed ships below!")
                print("")
                GameBoard.print_board(user_guess_board)
                print('')
                print("To play again Click the Run progran button above!!")
                break

        # Computer's turn
        print(Fore.GREEN + "------------------------------")
        print(Fore.GREEN + "  Now its the Computers turn  ")
        print(Fore.GREEN + "------------------------------")
        computer_x_row, computer_y_column = Battleship.get_computer_input()
        print(f"Computer guessed \
             {computer_x_row + 1}{chr(computer_y_column + 65)}")

        while computer_board.board[computer_x_row][computer_y_column] == "-"\
                or computer_board.board[computer_x_row][computer_y_column]\
                == "X":
            # print(Fore.RED + "I already guessed that!")
            computer_x_row, computer_y_column = Battleship.get_computer_input()
        if computer_board.board[computer_x_row][computer_y_column] == ".":
            print(Fore.RED + "I hit one of the Players battleships!")
            computer_board.board[computer_x_row][computer_y_column] = "X"
            score_1 = Battleship.count_hit_ships(user_guess_board)
            print(Fore.GREEN + "Player Score: " + str(score_1))
            score_2 = Battleship.count_hit_ships(computer_board)
            print(Fore.GREEN + "Computer Score: " + str(score_2))
            # check for win or lose
        elif Battleship.count_hit_ships(computer_board) == 10:
            print(Fore.RED + "Game Over - Computer hit all your battleships!")
            GameBoard.print_board(computer_board)
            break
        else:
            print(Fore.YELLOW + "I missed the players battleships!")
            computer_board.board[computer_x_row][computer_y_column] = "-"
            score_1 = Battleship.count_hit_ships(user_guess_board)
            print(Fore.GREEN + "Player Score: " + str(score_1))
            score_2 = Battleship.count_hit_ships(computer_board)
            print(Fore.GREEN + "Computer Score: " + str(score_2))


def main_game_run():
    """
    Runs both the Welcome screen class and Run Game class in
    order of appearance for correct sequence.
    """
    WelcomeScreen()
    RunGame()


if __name__ == "__main__":

    main_game_run()

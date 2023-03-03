import random

LENGTH_OF_SHIPS = [5, 4, 3, 3, 2]


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
        try:
            x_row = input("Please enter a ship row 1-8: ")
            while x_row not in "12345678":
                print("Please enter a valid row")
                x_row = input("Please enter ship row 1-8: ")

            y_column = input("Please enter a ship column A-H: ").upper()
            while y_column not in "ABCDEFGH":
                print("Please enter a valid column: ")
                y_column = input("Please enter a ship column A-H: ").upper()
            return int(x_row) - 1, GameBoard.get_char_to_num()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
        return self.get_user_input()

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


if __name__ == "__main__":
    RunGame()

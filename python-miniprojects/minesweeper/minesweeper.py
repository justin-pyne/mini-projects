import random

# create a board object to represent a game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()

        # init a set to track uncovered locations
        self.dug = set() # (row, col) tuples in this set

    def make_new_board(self):

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col]  == '*':
                # we already planted a bomb at this location
                continue
            else:
                board[row][col] = '*'
                bombs_planted += 1

        return board
    
    






#play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if the location is a bomb, show game over
    # Step 3b: if the location is not a bomb, dig recursively until each square is at least next to a bomb.
    # Step 4: repeat steps 2 and 3 until there are no more spots -> WIN!
    pass




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

        board = 







#play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if the location is a bomb, show game over
    # Step 3b: if the location is not a bomb, dig recursively until each square is at least next to a bomb.
    # Step 4: repeat steps 2 and 3 until there are no more spots -> WIN!
    pass


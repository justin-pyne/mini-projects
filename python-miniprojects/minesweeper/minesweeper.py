import random

# create a board object to represent a game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()
        self.assign_values_to_board()

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
    
    def assign_values_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_neighbor_bombs(r, c)

    def get_neighbor_bombs(self, row, col):
        
        num_neighbor_bombs = 0

        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighbor_bombs += 1

        return num_neighbor_bombs
    
    def dig(self, row, col):
        # True if successful dig, False if hit bomb

        # Possibilities:
        # hit a bomb -> game over
        # dig at a location with neighboring bombs -> finish dig
        # dig at a location with no neighboring bombs -> recursively dig neighbors

        



#play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig


    # Step 3a: if the location is a bomb, show game over


    # Step 3b: if the location is not a bomb, dig recursively until each square is at least next to a bomb.


    # Step 4: repeat steps 2 and 3 until there are no more spots -> WIN!
    


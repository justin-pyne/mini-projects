class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] #a list of 1-9 represents the indicies on the board
        self.current_winner = None #keep track if someone wins

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            pass
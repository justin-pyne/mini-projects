from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] #a list of 1-9 represents the indicies on the board
        self.current_winner = None #keep track if someone wins

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        

    def available_moves(self):
        #logic without list comprehension:
        # moves = []
        # for (i, x) in enumerate(self.board):
        #     if x == " ":
        #         moves.append(i)
            
        return [i for (i, x) in enumerate(self.board) if x == " "]

    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        
        #check row
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([x == letter for x in row]):
            return True
        
        #check col
        col_ind = square%3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([x == letter for x in col]):
            return True

        #check diag
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([x == letter for x in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([x == letter for x in diagonal2]):
                return True
            
        return False #no winner yet


def play(game, x_player, o_player, print_game = True):
    if print_game==True:
        game.print_board_nums()
    
    letter = "X"

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter) == True:
            if print_game == True:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")
            
            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            
            letter = "O" if letter == "X" else "X"

    if print_game:
        print("It\'s a tie!")
    



if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
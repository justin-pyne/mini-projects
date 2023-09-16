import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        move = random.choice(game.available_moves())
        return move


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.availablemoves()) == 9:
            square = game.random.choice(game.available_moves())
        else:
            # use a minimax algorithm to get the best move
            square = self.minimax(game, self.letter)
        return square
    

    def minmiax(self, state, player):
        maxPlayer = self.letter()
        otherPlayer = 'O' if maxPlayer == 'X' else 'X'

        # base case
        if state.current_winner == otherPlayer:
            return {'position' : None,
                    'score' : 1 * (state.num_empty_squares() + 1) if otherPlayer == maxPlayer else -1 * (state.num_empty_squares() + 1)
                    }
        
        elif not state.empty_squares():
            return {'position' : None, 'score' : 0}
        
        # init dicts
        if player == maxPlayer:
            best = {}


    
    

    
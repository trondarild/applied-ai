from games import *

# 
# Properties:
# board -   a list of list containing the board state
# moves -   a list of (row,col) pairs giving legal moves for to_move
#           player on the current board
# utility-  a number giving the utility of the current board for 
#           the current player
class State (object) :
    def __init__(self):

        self.board = [   [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    ]
        self.moves = []
        self.to_move = 1     # the player to move
        self.utility = 0

class ReversiGame(Game):
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""
    


    def __init__(self):
        self.initial_board = [   [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,1,-1,0,0,0],
                        [0,0,0,-1,1,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                    ]
        self.gamestate = State()
        self.gamestate.board = self.initial_board
        self.initial = self.gamestate

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
        abstract

    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        # todo: with given move, do reversals etc and return the new state,
        #       remember to switch to_move
        abstract
            
    def utility(self, state, player):
        "Return the value of this final state to player."
        # abstract
        numerator = 0
        denominator = 0
        # naive utility: count number of pieces for each player
        # and return a fraction
        # TODO: add strategies like preferring stabile positions
        for i in range(0,8):
            for j in range(0,8):
                if state.board[i][j] == player: numerator += 1
                elif state.board[i][j] == -player: denominator += 1

        return numerator/denominator

    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        return not self.legal_moves(state)

    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move

    def display(self, state):
        "Print or otherwise display the state."
        print state

    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]

    def __repr__(self):
        return '<%s>' % self.__class__.__name__
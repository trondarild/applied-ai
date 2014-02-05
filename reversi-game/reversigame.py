
from copy import deepcopy

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

    def __repr__(self):
        "print out an ascii version of the board"
        "TODO"
        """
            | a | b | c | d | e | f | g | h |
            ---------------------------------
          1 | . | . | . | . | . | . | . | . |
            ---------------------------------
          2 | . | . | . | . | . | . | . | . |
            ---------------------------------
          3 | . | . | . | . | . | . | . | . |
            ---------------------------------
          4 | . | . | . | . | . | . | . | . |
            ---------------------------------
          5 | . | . | . | . | . | . | . | . |
            ---------------------------------
          6 | . | . | . | . | . | . | . | . |
            ---------------------------------
          7 | . | . | . | . | . | . | . | . |
            ---------------------------------
          8 | . | . | . | . | . | . | . | . |
            ---------------------------------
        """  
        retval = ''
        rowstr = ''
        pieces = {-1:'O', 0:' ', 1:'X'}
        sep = '   ---------------------------------\n'
        
        
        retval +='   | a | b | c | d | e | f | g | h |\n'
        retval += sep
        
        for i in range(0,8):
            rowstr = ' '+str(i+1)+ ' |'
            for j in range(0,8):
                rowstr += ' '+pieces[self.board[i][j]]+' |'

            retval += rowstr + '\n'
            retval += sep 

        return retval

    def copy_board(self,board):
        self.board = deepcopy(board)

class ReversiGame(Game):
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""
    
    def check_direction(self, position, state):
        "Check if there are valid_directions, if so,return all valid_directions."
        valid_directions = []
        x = position[0]
        y = position[1]
        # iterate 8 directions
        for delta_x in range(-1,2):
            for delta_y in range(-1,2):
                if delta_x or delta_y:
                    x2 = x + delta_x
                    y2 = y + delta_y
                    if state.board[y2][x2] == -state.to_move:
                        valid_directions.append((delta_x,delta_y))
                    else:
                        None # do nothing
        return valid_directions
            

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
        # iterate 64 positions over board
        state.moves = []
        for i in range(7):
            for j in range(7):
                if state.board[j][i] == 0:
                    position = (i,j)
                    valid_directions = self.check_direction(position, state)
                    if valid_directions:
                        for direction in valid_directions:
                            x = i + direction[0]
                            y = j + direction[1]
                            while x>=0 and x<=7 and y>=0 and y<=7:
                                if state.board[y][x] == state.to_move:
                                    state.moves.append((i,j))
                                    break
                                elif state.board[y][x] == -state.to_move:
                                    None # do nothing
                                else: # if blank
                                    break
                                x += direction[0]
                                y += direction[1]
        return state.moves


    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        # TODO seems to be missing out on second-order reversals. Could this be 
        #       recursive? Define internal recursive function which builds up a 
        #       list of all positions to be reversed, then iterate through that list?
        #       But must look ahead not back, so only consider directions that are 180 deg
        next_state = State()
        next_state.copy_board(state.board)
        next_state.board[move[1]][move[0]] = state.to_move
        valid_directions = self.check_direction(move,state)
        if valid_directions:
            for direction in valid_directions:
                # move one step ahead in valid direction
                col = move[0] + direction[0] # x
                row = move[1] + direction[1] # y
                reversallist = [] # ls
                while (col in range(8)) and (row in range(8)): #x>=0 and x<=7 and y>=0 and y<=7:
                    # if reached a piece which is same as self, start going through reversal list
                    if state.board[row][col] == state.to_move:
                        # ..and set pieces to own colour
                        for (col,row) in reversallist:
                            # TODO but now this must be checked for higher order reversals!
                            next_state.board[row][col] = state.to_move
                        break
                    elif state.board[row][col] == -state.to_move:
                        # reached opposite colour, add this position to reversal list
                        reversallist.append((col,row))
                    else: # if blank
                        break
                    # update position
                    col += direction[0]
                    row += direction[1]
                # end while
            # end for
        # end if    
        next_state.moves = []
        next_state.to_move = -state.to_move
        return next_state

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

            
    def utility(self, state, player):
        "Return the value of this final state to player."
        # abstract
        numerator = 0
        denominator = 0
        # naive utility: count number of pieces for each player
        # and return a fraction
        # TODO: add strategies like preferring stable positions
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

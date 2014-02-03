class State (object) :
    board = [   [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ]
    moves = []
    to_move = 0
    utility = 0

    def __init__(self,player):

        self.board = [  [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,1,-1,0,0,0],
                        [0,0,0,-1,1,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                    ]
        self.moves = []
        self.to_move = player
        self.utility = 0

class ReversiGame:
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
        abstract
            
    def utility(self, state, player):
        "Return the value of this final state to player."
        abstract

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
from reversigame import *
start = State(1)
revg = ReversiGame()
#valid_directions = revg.check_direction((3,5),start)
legal_moves = revg.legal_moves(start)
print legal_moves

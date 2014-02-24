from reversigame import *
start = State()
revg = ReversiGame()
#valid_directions = revg.check_direction((3,5),start)
#legal_moves = revg.legal_moves(start)
#print legal_moves
#next = revg.make_move((3,5),start)
#print next.board
successors = revg.successors(start)
print len(successors)
for suc in successors:
	print suc[0] 
	print suc[1].board
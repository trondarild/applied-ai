from time import time
from utils import *
from reversigame import *
def reversi_alphabeta_search(game, state, starttime=0, maxtime=5):
	''' 
	Do a time limited alphabeta search on given game
	
	pseudocode (from russel and norman) :
	function reversi_alphabeta_search(state) returns move

		def cutoff_test(game, state, starttime, maxtime):
			terminal = game.is_terminal(state)
			timeout = time()-starttime >= maxtime
			return terminal or timeout 


		function maxvalue(game, state, starttime, maxtime, alpha, beta) returns a utility value
			# if a terminal state, return the value of that state
			if cutoff_test(game, state, starttime, maxtime) return utility(state)

			# not a terminal state
			v=-infinity

			for each move in state.moves do:
				# take the max of (v and do minvalue of (state resulting from doing move in given 
				# state))
				newstate = make_move(state, move)
				v = max(v, minvalue(newstate, alpha, beta))
				if v >= beta: return v
				alpha = max(alpha, v)
			return v

		function minvalue(game, state, starttime, maxtime, alpha, beta) returns a utility value:
			# if a terminal state, return its value
			if cutoff_test(game, state, starttime, maxtime) return utility(state)

			v=infinity
			for each move in state.moves do:
				newstate = make_move(state, move)
				v = min(v, maxvalue(newstate, alpha, beta))
				if v <= alpha: return v
				beta = min(beta, v)
			return v


		v = maxvalue(game, state, starttime, maxtime, -infinity, infinity)
		for move in state.moves()
			if utility(make_move(move, state)) == v
				return move
		
	'''

	# cutoff test with time check
	def cutoff_test(game, state, starttime, maxtime):
		terminal = game.terminal_test(state)
		timeout = (time()-starttime) >= maxtime
		return terminal or timeout 

	# max function
	def maxvalue(game, state, starttime, maxtime, alpha, beta):
		# check need to cut off recursion
		if cutoff_test(game, state, starttime, maxtime) :
			return game.utility(state, game.to_move(state))

		# not a terminal state
		v=-infinity

		for (m, s) in game.successors(state) :
			# newstate = game.make_move(move, state)
			v = max(v, minvalue(game, s, starttime, maxtime, alpha, beta))
			if v >= beta: return v
			alpha = max(alpha, v)
		return v

	# min function
	def minvalue(game, state, starttime, maxtime, alpha, beta):
		# check if need to cut off recursion
		if cutoff_test(game, state, starttime, maxtime):
			return game.utility(state, game.to_move(state))

		# not a terminal state
		v = infinity

		for (m, s) in game.successors(state):
			# newstate = game.make_move(move, state)
			v = min(v, maxvalue(game, s, starttime, maxtime, alpha, beta))
			if v <= alpha: return v
			beta = min(beta, v)
		return v

	# alphabeta search starts here
	v = maxvalue(game, state, starttime, maxtime, -infinity, infinity)

	# return the move which has the value of v
	retmove = (-1,-1)
	for (m, s) in game.successors(state):
		if game.utility(s, game.to_move(state)) == v:
			retmove = m
			break

	return retmove

	


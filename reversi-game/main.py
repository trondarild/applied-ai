from reversigame import *
from games import *
from time import time
from alphabeta import reversi_alphabeta_search

def reversi_query_player(game, state, maxtime):
    "Make a move by querying standard input."
    coldict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    def is_valid(inputstr):
    	# TODO
    	return True

    def translate_input(inputstr):
    	col = coldict[inputstr[:1]]
    	row = int(inputstr[1:])-1
    	return (col,row)

    game.display(state)
    usermove = num_or_str(raw_input('Your move (you are X)? '))
    # translate move of type [a-h][1-8]
    # TODO: check validity
    return translate_input(usermove)


# define reversi_alphabeta_player
def reversi_alphabeta_player(game, state, maxtime):
    starttime = time()
    return reversi_alphabeta_search(game, state, starttime, maxtime)

# define reversi_play_game
def reversi_play_game(game, maxtime, *players):
    "Play an n-person, move-alternating game."
    state = game.initial
    while True:
        for player in players:
            move = player(game, state, maxtime)
            state = game.make_move(move, state)
            # display game after human player, so computer to move
            # todo, add legal moves?
            if state.to_move == -1: game.display(state)
            if game.terminal_test(state):
                return game.utility(state, players[0])


def main():
    game = ReversiGame();
    # TODO ask for max time
    maxtime = int(raw_input("Max time for computer to spend on move in seconds: "))
    # TODO check if maxtime legal
    return reversi_play_game(game, maxtime, reversi_query_player, reversi_alphabeta_player)

if __name__ == "__main__":
	main()
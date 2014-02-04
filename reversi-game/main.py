from reversigame import *
from games import *

def reversi_query_player(game, state):
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

def main():
	game = ReversiGame();
	return play_game(game, reversi_query_player, alphabeta_player)

if __name__ == "__main__":
	main()
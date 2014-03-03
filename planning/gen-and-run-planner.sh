#!/bin/bash
echo "generating a $1 x $1 world with $1 wumpuses $1 pits and 1 gold..."

python generator.py -M $1 -N $1 -W $1 -P $1 -G 1 -F wumpus$1x$1-w$1p$1.pddl > wumpusviz$1x$1-w$1p$1.txt
echo "problem file written to  wumpus$1x$1-w$1p$1.pddl, visualization to wumpusviz$1x$1-w$1p$1.txt"

./ff -o wumpusworlddomain-square.pddl -f wumpus$1x$1-w$1p$1.pddl > ff-out-$1x$1-w$1p$1.txt
echo "ff output written to ff-out-$1x$1-w$1p$1.txt"

more wumpusviz$1x$1-w$1p$1.txt
more ff-out-$1x$1-w$1p$1.txt

echo "Done."


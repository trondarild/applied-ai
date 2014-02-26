(define (domain wumpusworld)
	(:types coordinate
	  direction
	  north south east west - direction
	  object
	  player wumpus arrow stench pit gold - object

	)
	(:requirements :strips)
	(:predicates (breeze ?x ?y)
					 (agent ?x ?y)
					 (gold ?x ?y)
					 (pit ?x ?y)
					 (stench ?x ?y)
					 (wumpus ?x ?y)
					 (visited ?x ?y)
					 (ok ?x ?y)
					 (direction ?x)
					 (limit ?x ?y)
					 (at ?what ?x ?y)
					 (adj ?x ?y ?i ?j)
					 (havearrow ?who)
					 (dead ?who)
					 ))

(:action move 
:parameters (?who ?x - coordinate ?y - coordinate ?i - coordinate ?j - coordinate)
:precondition (and (ok ?i ?j) (at ?who ?x ?y) (adj ?x ?y ?i ?j))
:effect (and (not (at ?who ?x ?y) (at ?who ?i ?j)) 

(:action takegold 
 :parameters (?who ?x - coordinate ?y - coordinate)
 :precondtion (and (at ?x ?y) (gold ?x ?y))
 :effect (not (gold ?x ?y)))

(:action isok 
 :parameters (?x - coordinate ?y - coordinate ?i - coordinate ?j - coordinate)
 :precondtion (and (at ?x ?y) (not (breeze ?x ?y)) (not (stench ?x ?y)))
 :effect (ok ?i ?j)
)

(:action shootarrow
 :parameters (?who ?x - coordinate ?y - coordinate ?i - coordinate ?j - coordinate)
 :precondition (and (havearrow ?who) (at ?who ?x ?y) (adj ?x ?y ?i ?j))
 :effect (and (not (havearrow ?who))
)


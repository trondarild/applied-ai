(define (domain wumpusworld)
	(:types coordinate
	  direction
	  north south east west - direction
	  object
	  player wumpus arrow stench pit gold - object

	)
	(:requirements :adl :typing)
	(:predicates 
					 (ok ?x ?y)
					 (breeze ?x ?y)
					 (pit ?x ?y)
					 (stench ?x ?y)
					 (wumpus ?x ?y)
					 (heading ?who ?dir)
					 (turnleft ?dir1 ?dir2)
					 (limit ?x ?y)
					 (at ?what ?x ?y)
					 (adj ?x ?y ?i ?j)
					 (adjdir ?x ?y ?i ?j ?dir)
					 (have ?who ?what)
					 (dead ?who)
					 ))

(:action move 
:parameters (?who ?x - coordinate ?y - coordinate ?i - coordinate ?j - coordinate)
:precondition (and (ok ?i ?j) (at ?who ?x ?y) (adj ?x ?y ?i ?j))
:effect (and (not (at ?who ?x ?y) (at ?who ?i ?j)) 

(:action take
 :parameters (?who - object ?what - object ?x - coordinate ?y - coordinate)
 :precondtion (and (at ?who ?x ?y) (at ?what ?x ?y))
 :effect (and (have ?who ?what) (not (at ?what ?x ?y))))

(:action isok 
 :parameters (?x - coordinate ?y - coordinate ?i - coordinate ?j - coordinate)
 :precondtion (and (at ?x ?y) (not (breeze ?x ?y)) (not (stench ?x ?y)))
 :effect (ok ?i ?j)
)

(:action shootarrow
 :parameters (	?who - object
 					?x - coordinate 
 					?y - coordinate 
 					?i - coordinate 
 					?j - coordinate 
 					?dir - direction)
 :precondition (and 	(have ?who ?what - arrow) 
 							(at ?who ?x ?y) 
 							(adj ?x ?y ?i ?j)
 							(heading ?who ?dir)
 							)
 :effect (and 	(not (havearrow ?who)
 			 (when (exist (?w - wumpus) (and (at ?w ?i ?j) (not (dead ?w))))
 			  (and (dead (?w)))
 )
)

(:action turn
 :parameter (?who - object ?from - direction ?to - direction)
 :precondition (heading ?who ?from)
 :effect (heading(?who ?to)
)




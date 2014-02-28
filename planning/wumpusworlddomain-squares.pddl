(define (domain wumpusworldsquare)
	;;(:requirements :adl :typing)
	(:types 
		coordinate - object
		square - object
	  
	  player wumpus arrow breeze stench pit gold - object
	)
	(:constants BREEZE - breeze
				PIT - pit
				WUMPUS - wumpus
	)
	(:predicates 
					 (at ?what ?square)
					 (adj ?square1 ?square2)
					 (have ?who ?what)
					 (danger ?square)
					 (alive ?who)
					 (pit ?square)
					 (breeze ?square)
					 (stench ?square)
					 (wumpus ?square)
					 )


(:action move 
:parameters (?who ?square1 ?square2)
:precondition (and 
					(not (danger ?square2)) 
					(at ?who ?square1) 
					(adj ?square1 ?square2)
					(alive ?who)
					(forall (?sq - square)
								(and
									(imply  (breeze ?square1)
												(pit ?square2)
									)
									(imply	(stench ?square1)
												(wumpus ?square2)	
									)
								)
					)

				)
:effect (and 
			(when (pit ?square2) (not (alive ?who)))
			(not (at ?who ?square1)) 
			(at ?who ?square2)
			;;(when (at WUMPUS ?square2) (not (alive ?who)))
			(when 	(exists (?w - wumpus) 
							(and (at ?w ?square2) (alive ?w))
					) 
					(not (alive ?who))

			)
		)		
)

(:action take
:parameters (?who ?what ?where)
:precondition (and
					(at ?who ?where)
					(at ?what ?where)

				)
:effect (and
				(have ?who ?what)
				(not (at ?what ?where))
		)
)


) ;; end define




(define (domain wumpusworldsquare)
	(:types 
		coordinate - object
		square - object
	  
	  player wumpus arrow stench pit gold - object

	)
	(:requirements :adl :typing)
	(:predicates 
					 (at ?what ?square)
					 (adj ?square1 ?square2)
					 (have ?who ?what)
					 (danger ?square)

					 )


(:action move 
:parameters (?who ?square1 ?square2)
:precondition (and (not (danger ?square2)) (at ?who ?square1) (adj ?square1 ?square2))
:effect (and 
			(not (at ?who ?square1)) 
			(at ?who ?square2)
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


)




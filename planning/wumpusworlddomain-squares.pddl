(define (domain wumpusworldsquare)
	;;(:requirements :adl :typing)
	(:types 
		coordinate - object
		square - object
	  
	  player wumpus arrow breeze stench pit gold - object
	)
	;;(:constants BREEZE - breeze
	;;			PIT - pit
	;;			WUMPUS - wumpus
	;;)
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
					(imply	(and (pit ?square1) (adj ?square1 ?square2))
								(breeze ?square2)
					)
					;;(imply	(and (wumpus ?square1) (adj ?square1 ?square2))
					;;			(stench ?square2)
					;;)
					(imply 
							(and (exists (?w - wumpus)
									(and 	(at ?w ?square1) 
											(alive ?w))
									)
									(adj ?square1 ?square2)
							)
							(stench ?square2)
					)
					(imply
						(or 	(stench ?square1) 
								(breeze ?square1)
						)
						(danger ?square2)
					)
				)
:effect 	(and 
				(when (pit ?square2) (not (alive ?who)))
				(not (at ?who ?square1)) 
				(at ?who ?square2)
				(when 	
					(exists (?w - wumpus) 
						(and 
							(at ?w ?square2) 
							(alive ?w)
						)
					) 
					(not (alive ?who))
				)
			)		
)


(:action take
:parameters (?who - player ?what ?where)
:precondition (and
					(at ?who ?where)
					(at ?what ?where)

				)
:effect (and
				(have ?who ?what)
				(not (at ?what ?where))
		)
)


(:action shoot 
:parameters (?who - player ?withwhat - arrow ?where - square ?victim - wumpus)
:precondition 	(and
						(have ?who ?withwhat)
						(at ?who ?where)
						(alive ?who)
						(alive ?victim)
						(exists 	(?sq - square)
									(and 
										(adj ?where ?sq)
										(at ?victim ?sq)
									)
						)
					)
:effect	(not (alive ?victim))
			
)

) ;; end define




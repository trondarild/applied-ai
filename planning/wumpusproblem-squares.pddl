(define (problem wumpusproblem)
  (:domain wumpusworldsquare)

  (:objects
   sq-1-1 sq-1-2 sq-1-3 sq-2-1 sq-2-2 sq-2-3 - square
   agent-1 - player
   the-gold - gold
   )

  (:init 
		(adj sq-1-1 sq-1-2) (adj sq-1-2 sq-1-1)
		(adj sq-1-2 sq-1-3) (adj sq-1-3 sq-1-2)
		(adj sq-2-1 sq-2-2) (adj sq-2-2 sq-2-1)
		(adj sq-2-2 sq-2-3) (adj sq-2-3 sq-2-2)
		(adj sq-1-1 sq-2-1) (adj sq-2-1 sq-1-1)
		(adj sq-1-2 sq-2-2) (adj sq-2-2 sq-1-2)
		(adj sq-1-3 sq-2-3) (adj sq-2-3 sq-1-3)
	 	(danger sq-1-2)
	 	(at agent-1 sq-1-1)
	 	(at the-gold sq-1-3)
	 	(not (have agent-1 the-gold))
	 
	)

  (:goal (and 
  				(have agent-1 the-gold) 
  				;;(at agent-1 sq-2-3) 
  				;;(not (dead agent-1))
  		)
  )


  )
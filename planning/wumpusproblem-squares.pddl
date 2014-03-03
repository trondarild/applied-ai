(define (problem wumpusproblem)
  (:domain wumpusworldsquare)

  (:objects
   sq-1-1 sq-1-2 sq-1-3 sq-2-1 sq-2-2 sq-2-3 - square
   agent-1 - player
   the-gold - gold
   the-breeze - breeze
   the-pit - pit
   wumpus-1 - wumpus
   wumpus-2 - wumpus
   the-arrow - arrow
   )

  (:init 
		(adj sq-1-1 sq-1-2) (adj sq-1-2 sq-1-1)
		(adj sq-1-2 sq-1-3) (adj sq-1-3 sq-1-2)
		(adj sq-2-1 sq-2-2) (adj sq-2-2 sq-2-1)
		(adj sq-2-2 sq-2-3) (adj sq-2-3 sq-2-2)
		(adj sq-1-1 sq-2-1) (adj sq-2-1 sq-1-1)
		(adj sq-1-2 sq-2-2) (adj sq-2-2 sq-1-2)
		(adj sq-1-3 sq-2-3) (adj sq-2-3 sq-1-3)
    ;;(pit sq-1-2)
    ;;(breeze sq-1-1)
    ;;(breeze sq-2-2)
    ;;(breeze sq-1-3)
    ;;(at the-pit sq-2-2)
    
    (at wumpus-1 sq-1-3)
    (alive wumpus-1)
    (at wumpus-2 sq-2-2)
    (alive wumpus-2)

    ;;(stench sq-1-1)
    ;;(stench sq-2-2)
    ;;(stench sq-1-3)

	 	(at agent-1 sq-1-1)
	 	(at the-gold sq-2-3)
	 	(not (have agent-1 the-gold))
    (alive agent-1)
    (have agent-1 the-arrow)
	 
	)

  (:goal (and 
  				(have agent-1 the-gold) 
  				(at agent-1 sq-1-1) 
  				(alive agent-1)

  		)
  )


  )
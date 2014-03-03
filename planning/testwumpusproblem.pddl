(define (problem wumpusproblem)
  (:domain wumpusworlddomain)

  (:objects
   ;;sq-1-1 sq-1-2 sq-1-3 sq-2-1 sq-2-2 sq-2-3 - square
   1 2 - coordinate
   the-gold - gold
   the-arrow - arrow
   agent-1 - player
   wumpus-1 - wumpus
   the-pit - pit
   the-smell - stench
   the-breeze - breeze
   north south east west - direction
   )

  (:init 
    ;;(adj sq-1-1 sq-1-2) (adj sq-1-2 sq-1-1)
	 ;;(adj sq-1-2 sq-1-3) (adj sq-1-3 sq-1-2)
	 ;;(adj sq-2-1 sq-2-2) (adj sq-2-2 sq-2-1)
	 ;;(adj sq-2-2 sq-2-3) (adj sq-2-3 sq-2-2)
	 ;;(adj sq-1-1 sq-2-1) (adj sq-2-1 sq-1-1)
	 ;;(adj sq-1-2 sq-2-2) (adj sq-2-2 sq-1-2)
	 ;;(adj sq-1-3 sq-2-3) (adj sq-2-3 sq-1-3)
	 (adj 1 1 1 2) (adj 1 2 1 1)
	 (adj 1 1 2 1) (adj 1 2 1 1)
	 (adj 2 1 2 2) (adj 2 2 2 1)
	 (adj 1 2 2 2) (adj 2 2 1 2)
	 
	 (pit 2 1)
	 (at the-gold 1 2)
	 (at agent-1 1 1)
	 (alive agent-1)
	 (have agent-1 the-arrow)
	 (at wumpus-1 2 2)
	 (alive wumpus-1))

  (:goal (and (have agent-1 the-gold) (at agent-1 sq-1-1) (alive agent-1)))
  )
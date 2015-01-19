init python:
    def chaseFunc( direction ):
        startTime = 0
        currentTime = 0
        # start a countdown for time limit
        startTime = renpygame.time.get_ticks()
        timeLimit = 1800 # pointer must reach the area in 1.8 seconds
        # 20 pixel area for each edge of screen
        left   = 20
        right  = 780
        top    = 20
        bottom = 580
        
        while True:
            event = renpygame.event.poll()
            
            #time check
            currentTime = renpygame.time.get_ticks() - startTime
            if currentTime > timeLimit:
                return False
                
            # if mouse is moved, check if area in given direction is reached
            # True means new function call from chase-label or successful completion of the chase
            elif event.type == pygame.MOUSEMOTION:
                if direction == 0:
                    if event.pos[1] <= top:
                        return True                
                if direction == 1:
                    if event.pos[0] >= right:
                        return True
                if direction == 2:
                    if event.pos[1] >= bottom:
                        return True
                if direction == 3:
                    if event.pos[0] <= left:
                        return True
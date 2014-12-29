python:
    def chaseFunc( direction ):
        
        startTime = pygame.time.get_ticks()
        timeLimit = 2000
        left   = 20
        right  = 780
        top    = 20
        bottom = 580
        x = y = 0
        running = 1
        #screen = pygame.display.set_mode((640, 400))

        while running:
            event = pygame.event.poll()
            
            #time check
            currentTime = pygame.time.get_tick() - starTime
            if currentTime > timeLimit:
                print "timelimit reached, quitting"
                return False
                
            #if event.type == pygame.QUIT:
            #    running = 0
            elif event.type == pygame.MOUSEMOTION:
                if direction == 0:
                    if event.pos(0) <= left:
                        return True                
                if direction == 1:
                    if event.pos(0) >= right:
                        return True                
                if direction == 2:
                    if event.pos(0) <= top:
                        return True                
                if direction == 3:
                    if event.pos(0) >= bottom:
                        return True                
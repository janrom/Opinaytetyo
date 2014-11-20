label joku:

    init python:
        
        import time
        
        # mouse event function
        def event(self, ev, x, y, st):
                    
            # if this border is shown atm
            if topBorderOn == True:
                # if mouse pointer is inside the 20 pixel area
                if y < topY:
                    # set the area flag true
                    onTop = True
                    # end clocking time
                    endTime = time.time()
                        
                if rightBorderOn == True:
                    if x > rightX:
                        onRight = True
                        endTime = time.time()
                                
                if bottomBorderOn == True:
                    if y > bottomY:
                        onBottom = True
                        endTime = time.time()
                            
                if leftBorderOn == True:
                    if x < leftX:
                        onLeft = True
                        endTime = time.time()
        
            # checks if player gets her mouse pointer on defined area in given time
            # on success jump to onSuccessLabel, on failure to onFailureLabel
            def chaseFunc():
                
                if randomValue == 0:
                    # start clocking time
                    startTime = time.time()
                            
                    # wait for users mouse motion
                    # user must get the pointer on the right area in this time
                    time.sleep( 2 )
                            
                    # calculate time difference
                    totalTime = endTime - startTime
                            
                    # if pointer reached the area in time,
                    # jump to on success label, otherwise on failure label
                    if onTop == True and totalTime < 1.0:
                        successEscape = True
                    else:
                        successEscape = False
                        
                    if randomValue == 1:
                        
                        startTime = time.time()
                        time.sleep( 2 )
                        endTime = time.time()
                        totalTime = endTime - startTime
                            
                        if onRight == True and totalTime < 1.0:
                            successEscape = True
                        else:
                            successEscape = False
                        
                    if randomValue == 2:
                        
                        startTime = time.time()
                        time.sleep( 2 )
                        endTime = time.time()
                        totalTime = endTime - startTime
                            
                        if onBottom == True and totalTime < 1.0:
                            successEscape = True
                        else:
                            successEscape = False
                        
                    if randomValue == 3:
                            
                        startTime = time.time()
                        time.sleep( 2 )
                        endTime = time.time()
                        totalTime = endTime - startTime
                            
                        if onLeft == True and totalTime < 1.0:
                            successEscape = True
                        else:
                            successEscape = False
    return
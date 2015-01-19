screen borderTop():
    mousearea:
        area ( 0, 0, 800, 20 )
        hovered Jump( "chase" )
    timer 1.2 action Jump( lblChaseFailure )
    
screen borderRight():
    mousearea:
        area ( 780, 0, 20, 600 )
        hovered Jump( "chase" )
    timer 1.2 action Jump( lblChaseFailure )

screen borderBottom():
    mousearea:
        area ( 0, 580, 800, 20 )
        hovered Jump( "chase" )
    timer 1.2 action Jump( lblChaseFailure )

screen borderLeft():
    mousearea:
        area ( 0, 0, 20, 800 )
        hovered Jump( "chase" )
    timer 1.2 action Jump( lblChaseFailure )

label chase:
    
    hide screen borderTop
    hide screen borderRight
    hide screen borderBottom
    hide screen borderLeft
    
    $result = True
    
    # store number preventing two same random numbers in row
    $lastRandom = 0
    
    # stuff for chase label
    $ chaseRounds = 15   # how many times border loop will run
    $ randomBorder = 0  # determines which border to show
        
    #chaseRounds is declared at start-label
    while chaseRounds > 0: 
            
        hide borderTop
        hide borderRight
        hide borderBottom
        hide borderLeft
        
        #pick new random value, pick it as long as new value is not same as last used one
        $newRandom = False
        while newRandom == False:
            # randomBorder is declared at start-label
            $randomBorder = renpy.random.randint ( 0 , 3 )
            if randomBorder != lastRandom:
                $lastRandom = randomBorder
                $newRandom = True
        
        # random value for picking which border image to show
        if randomBorder == 0: #top
            $ chaseRounds -= 1  
            show borderLeft
            show borderRight
            show borderBottom
            pause(0) # must use pause to show above borders
            python: # call the chase logic in chasePygame.rpy
                result = chaseFunc( randomBorder )                
            #show screen borderTop
                
        elif randomBorder == 1: #right
            $ chaseRounds -= 1  
            show borderLeft
            show borderTop
            show borderBottom
            pause(0)
            python:
                result = chaseFunc( randomBorder )                
            #show screen borderRight
        
        elif randomBorder == 2: #bottom
            $ chaseRounds -= 1  
            show borderLeft
            show borderTop
            show borderRight
            pause(0)
            python:
                result = chaseFunc( randomBorder )    
            #show screen borderBottom
        
        elif randomBorder == 3: #left
            $ chaseRounds -= 1  
            show borderTop
            show borderRight
            show borderBottom
            pause(0)
            python:
                result = chaseFunc( randomBorder )                
            #show screen borderLeft
        
        # if chaseFunc returns False (timelimit reached)
        # jump to according scene
        if result == False:
            if lblChaseFailure == 1:
                jump chaseFailureForestPeople
                
            if lblChaseFailure == 2:
                jump dialog1ChaseFailureCastle
                
            if lblChaseFailure == 3:
                jump dialog5ManLoseInnkeeper
            
    # if player completes all rounds
    # jump to label according to last stored number
    if lblChaseSuccess == 1:
        jump chaseSuccessForestPeople
        
    if lblChaseSuccess == 2:
        jump dialog1ChaseSuccessCastle
        
    if lblChaseSuccess == 3:
        jump dialog5ManWinsInnkeeper
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
      
    hide borderTop
    hide borderRight
    hide borderBottom
    hide borderLeft
    
    #chaseRounds is declared at start-label
    if chaseRounds > 0: 
        
        # randomBorder is declared at start-label
        $ randomBorder = renpy.random.randint ( 0 , 3 )
        
        # random value for picking which border image to show
        if randomBorder == 0:
            $ chaseRounds -= 1  
            show borderLeft
            show borderRight
            show borderBottom
            show screen borderTop
                
        elif randomBorder == 1:
            $ chaseRounds -= 1  
            show borderLeft
            show borderTop
            show borderBottom
            show screen borderRight
        
        elif randomBorder == 2:
            $ chaseRounds -= 1  
            show borderLeft
            show borderTop
            show borderRight
            show screen borderBottom
        
        elif randomBorder == 3:
            $ chaseRounds -= 1  
            show borderTop
            show borderRight
            show borderBottom
            show screen borderLeft
            
        pause
            
    # if player completes all rounds
    # jump to label according to last stored number
    if lblChaseSuccess == 1:
        jump chaseSuccessForestPeople
        
    if lblChaseSuccess == 2:
        jump dialog1ChaseSuccessCastle
        
    if lblChaseSuccess == 3:
        jump dialog5ManWinsInnkeeper

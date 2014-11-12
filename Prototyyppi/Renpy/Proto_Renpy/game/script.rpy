
image bg black = "images/backgrounds/black.png"

image landscape village = "images/scans/village.jpg"

image imgBorderTop = "images/borders/top.png"
image imgBorderRight = "images/borders/right.png"
image imgBorderBottom = "images/borders/bottom.png"
image imgBorderLeft = "images/borders/left.png"

define n = Character('Narrator', color="#ffffff")

init python:
    
    borderRunRounds = 8
    
    def borderRunCounter():
        
        global borderRunRounds
        
        if borderRunRounds > 0:
            borderRunRounds -= 1            
        
        if borderRunRounds == 0:
            Jump( "some_label" )
        else:
            Jump ( "borders_run" )
            
######################################################
# label start
######################################################
label start:

# images
scene bg black
show landscape village at top

screen scrBorderTop():
    mousearea:
        area ( 0, 0, 800, 20 )
        hovered Jump( "border_run" ) #borderRunCounter() #Jump( "border_run" )

screen scrBorderRight():
    mousearea:
        area ( 780, 0, 20, 600 )
        hovered Jump( "border_run" ) #borderRunCounter() #Jump( "border_run" )

screen scrBorderBottom():
    mousearea:
        area ( 0, 580, 800, 20 )
        hovered Jump( "border_run" ) #borderRunCounter() #Jump( "border_run" )

screen scrBorderLeft():
    mousearea:
        area ( 0, 0, 20, 800 )
        hovered Jump( "border_run" ) #borderRunCounter() #Jump( "border_run" )


######################################################
# python loop for border run, using mouse coordinates
######################################################
label border_run:
    
    # random value for picking which border image to show
    $randomValue = renpy.random.randint ( 0 , 3 )

    #$newRandom = False
    #while newRandom == False:
    #    $tempRandomValue = renpy.random.randint ( 0, 3 )
    #    if tempRandomValue != randomValue:
    #        $randomValue = tempRandomValue
    #        $newRandom = True 

    hide screen scrBorderTop
    hide screen scrBorderRight
    hide screen scrBorderBottom
    hide screen scrBorderLeft
        
    hide imgBorderTop
    hide imgBorderRight
    hide imgBorderBottom
    hide imgBorderLeft
    
    if randomValue == 0:
        show imgBorderTop
        show screen scrBorderTop
        
    if randomValue == 1:
        show imgBorderRight
        show screen scrBorderRight
    
    if randomValue == 2:
        show imgBorderBottom
        show screen scrBorderBottom
        
    if randomValue == 3:
        show imgBorderLeft
        show screen scrBorderLeft
        
# algorithm for border run
#loop start
#new int randomValue = random value 0 - 3
#show border right for 1 second
#	bool newRandom = false
#	while newRandom == false
#		new tempRandomValue = random value 0 - 3
#		if tempRandomValue == randomValue
#			continue
#		else newRandom == true
#	end while

#	if mouse reach right border
#		continue
#	else failed
#loop end

n "Aloituskuva kylän maisemasta"

label some_label:
    n "Some label"

return

#import random

image bg black = "images/backgrounds/black.png"

image landscape village = "images/scans/village.jpg"

image border top = "images/borders/top.png"
image border right = "images/borders/right.png"
image border bottom = "images/borders/bottom.png"
image border left = "images/borders/left.png"

define n = Character('Narrator', color="#ffffff")

######################################################
# label start
######################################################
label start:

# images
scene bg black
show landscape village at top

######################################################
# python loop for border run, using mouse coordinates
######################################################
# random value for picking which border image to show
$randomValue = renpy.random.randint ( 0 , 3 )

$rounds = 8

while rounds > 0:
    $newRandom = False
    while newRandom == False:
        $tempRandomValue = renpy.random.randint ( 0, 3 )
        if tempRandomValue != randomValue:
            $randomValue = tempRandomValue
            $newRandom = True        
    
    $mouseCoordinates = renpy.get_mouse_pos()
    $mouseX = mouseCoordinates[0]
    $mouseY = mouseCoordinates[1]
    
    $topBorderY = 20
    $rightBorderX = 780
    $bottomBorderY = 580
    $leftBorderX = 20
    
    #tähän laskuri joka nollataan joka kiesin alussa
    
    #tähän sisäinen looppi joka pyörii niin pitkään kunnes joko aika loppuu
    #tai hiiri viedään oikean reunuksen päälle
    
    $borderReached = False
    $timeUp = False
    
    while borderReached == False or timeUp == False:
        # show border based on random value
        if randomValue == 0:
            show border top
            if mouseY <= topBorderY and mouseY > 0:
                $borderReached = True
            
        if randomValue == 1:
            show border right
            if mouseX >= rightBorderX:
                $borderReached = True
            
        if randomValue == 2:
            show border bottom
            if mouseY >= bottomBorderY:
                $borderReached = True
                
        if randomValue == 3:
            show border left
            if mouseX <= leftBorderX and mouseX > 0:
                $borderReached = True        
            
    $rounds -= 1

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

return

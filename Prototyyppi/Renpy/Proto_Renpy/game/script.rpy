#import random

image bg black = "images/backgrounds/black.png"

image landscape village = "images/scans/village.jpg"

image border top = "images/borders/top.png"
image border right = "images/borders/right.png"
image border bottom = "images/borders/bottom.png"
image border left = "images/borders/left.png"

define n = Character('Narrator', color="#ffffff")

label start:

# images
scene bg black
show landscape village at top

# python loop for border run, using mouse coordinates
$ randomValue = renpy.random.randint ( 0 , 3 )
$ rounds = 8
while rounds > 0:
  $ newRandom = False
  while newRandom == False:
    $ tempRandomValue = renpy.random.randint ( 0, 3 )
    if tempRandomValue != randomValue:
      $ randomValue = tempRandomValue
      $ newRandom = True
  
  # show border based on random value
  if randomValue == 0:
    show border top
	# add mouse coordinate check for top border
	# add time limit for reaching that border
	# add those for every if-statements
  if randomValue == 1:
    show border right
  if randomValue == 2:
    show border bottom
  if randomValue == 3:
    show border left
  
  
  
  $ rounds -= 1

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

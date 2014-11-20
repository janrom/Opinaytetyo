init:
    image bg black = "images/backgrounds/black.png"
    image village = "images/scans/village.jpg"
    image village2 = "images/scans/village2.jpg"
    
    image unconscious = "images/scans/unconscious.jpg"
    
    image tree = "images/scans/tree.jpg"
    image tree2 = "images/scans/tree2.jpg"
    
    image woman = "images/scans/woman.jpg"

    image imgBorderTop = "images/borders/top.png"
    image imgBorderRight = "images/borders/right.png"
    image imgBorderBottom = "images/borders/bottom.png"
    image imgBorderLeft = "images/borders/left.png"

    define n = Character('Narrator', color="#ffffff")

screen scrBorderTop():
    mousearea:
        area ( 0, 0, 800, 20 )
        hovered Jump( "chase" )

screen scrBorderRight():
    mousearea:
        area ( 780, 0, 20, 600 )
        hovered Jump( "chase" )

screen scrBorderBottom():
    mousearea:
        area ( 0, 580, 800, 20 )
        hovered Jump( "chase" )

screen scrBorderLeft():
    mousearea:
        area ( 0, 0, 20, 800 )
        hovered Jump( "chase" )

label start:
    
    ##########################################################################################
    # stuff for chase label
    #
    $ chaseRounds = 5           # how many times chase algorithm will run
    $ randomValue = 0           # determines which border to show
    $ onSuccessLabel = ""       # name of label to jump from chase label, on success escape
    $ onFailureLabel = ""
    $ successEscape = False     # chaseFunc in chase.rpy return true if escape was success
    
    # truth if that border is shown atm
    $ topBorderOn = False
    $ rightBorderOn = False
    $ bottomBorderOn = False
    $ leftBorderOn = False
    
    # border values for chase areas
    $ topY = 20
    $ rightX = 780
    $ bottomY = 580
    $ leftX = 20
    
    # truth if mouse is on that 20 pixel area
    $ onTop = False
    $ onRight = False
    $ onBottom = False
    $ onLeft = False
    
    # for clocking time
    $ startTime = 0.0
    $ endTime = 0.0
    #
    ######################################################################################
  
    scene bg black
    
    n "This story happened generations ago"
    n "In the time when forests were wild and man was just a part of a nature"
    n "Before the man made himself a tyranny of the world"
    
label village:
    
    scene bg black
    show village at top
    
    n "After a long and weary travel, a man and a woman finally saw a landscape which entwined a little town in"
    n "They headed into inn and rent a room for a night"
    n "After a bath and a warm meal they fall into sleep"
    n "At the middle of the night, man suddenly awakes for a scream of her wife"
    n "He saws a punch of men in the room tiding the wife down"
    n "Husband charges towards the men"
    n "He fight hard and brave but there are just too many of them"
    n "They knock husband down and he falls in unconsciousness"
    

label unconscious:
    
    scene bg black
    show unconscious at top with fade 
    
    pause 3
    
label husbandAwakesInForest:
    
    scene bg black
    show village2 at top with fade
    
    n "Husband begins to gain his consciosness opening his eyes"
    n "He is badly beaten with his clothes ripped"
    n "He doesn't see his wife"
    n "He tries to find her and yell her name but he can't find her"
    n "From the hill he sees that same village down a valley"
    n "To other direction land is rising up towards a mountain"
    n "There's a old castle high on mountain side"
    
    menu:
        "He returns to village hoping his wife is still there alive":
            jump returnToVillage
            
        "He continues search his wife in the forest":
            jump searchForest
            
        "He starts climbing up to mountain side towards the castle":
            jump searchMountainSide
            
label returnToVillage:
    
    scene bg black
    show village at top
    
    n "When husband arrives in village, villagers starts gather around him"
    n "They are scared of his looks"
    n "Somebody starts to yell at him"
    n "Some other throws a rock towards him" 
    n "Others starts joining them, becoming more rude all the time"
    n "Husband tries to explain but nobody seems to understand him"
    n "Somebody charges him hitting with a pole"
    n "Husband fells on the ground getting a bleeding wound from the hit" 
    n "People are getting into rage"
    
    menu:
        "He rises from the ground and start to run from his life towards the forest":
            jump leaveTown
        
        "He rises from the ground and start to run deeper into village":
            jump findInn

label searchForest:
    
    scene bg black
    show tree at top
    
    n "He wanders to small glade, a huge old oak in the center"
    n "There are people gathered around the tree"
    n "They don't have clothes, a thick dirt covering their skin"
    n "They look like a people but their behauvior reminds more of a animal"
    n "Someone spots him and screams alarming the others"
    n "Everyone nails their eyes on husband, silent surrounds the glade"
    n "People starts to approach the husband"
    
    menu:
        "Fear hits him and he turns to run away in horror":
            $ onSuccessLabel = "playerEscapes"
            $ onFailureLabel = "playerGetCaught"
            jump chase
            
        "He can hear his heart bounding but he force himself to greet the people":
            jump greetForestPeople
            
label playerEscapes:
    n "He manage to escape from the people"
    
label playerGetCaught:
    n "They catch the man"

label searchMountainSide:
    
    scene bg black
    show mountain at top
    
    n "He search and climbs higher and higher"
    n "But he can't find his wife"
    n "He begin to be close to castle"
    n "He can see a intimitating figure of it"
    
label castleMan:

    scene bg black
    show castle at top
    
    n "He arrives at castle"
    n "Trying to find his wife without success"
    n "Suddenly he is aware of presens of somebody"
    n "Old man appears from shadows"
    n "He stares at husband with his sharp eyes in silence"
    
    # DIALOG 1       
        

label leaveTown:

    scene bg black
    show landscape forest2 at top
    
    n "People quit the chase after he reach the woods"
    n "They seems to be too afraid to continue"
    
    menu:
        "He tries to search his wife in the forest":
            jump searchForest
            
        "He start climbing on mountain side hoping to get better view":
            jump searchMountainSide
            
label findInn:
    
    scene bg black
    show village at top
    
    n "He manages to lost villagers who followed him"
    n "Finally he finds the inn on goes in"
    n "There's a inn keeper and he looks very suprised to see you"
    
    # DIALOG 5

label greetForestPeople:
    
    scene bg black
    show tree2 at top
    
    n "People gather around him, touching him and communicating with each other"
    n "They gather wood from old oak and build a big fire"
    n "They start dancing and singing wildly around a fire"
    n "Husband join the dance and they dance all night"
    n "Strong feeling begins to take a grip from husband, stronger and stronger"
    n "He start to feel a strong wilderness in you which grows higher in every moment"
    n "Dance goes wilder and wilder"
    n "At dawn the fire have turned to embers"
    n "Husband stands whole awake breathing fresh morning air into his lungs eagerly"
    n "The blood is rushing in his veins like never before"
    n "He have never been so awake, so full of life"
    n "His instincts have become supernatural"
    n "He feels stronger that never before"
    n "His eyes sharp as eagle's"
    n "Vigour as wolf"
    n "Smelling thousands of scents"
    n "Hearing even tiniest crack"
    n "He feels like a wildest animal, like a alpha wolf in the pack"
    n "He can smell the scent of his wife"
    n "As the scent comes in the rush of adreline hits in"
    n "He starts to run like a jaguar following that scent"
        
label village:
    
    scene bg black
    show village at top
    
    n "The scent leads him back to village"
    n "He follows the scent deeper"
    n "He hears and smells the villagers and avoids to encounter with them"
    n "Village dogs starts to bark and howl, horses goes uneasy, every animal senses a beast"
    n "Villagers starts to gather wondering what hits the animals"
    n "The scent leads him at small shed behind the inn"
    n "He force himself trough the door and sees his wife laying on the ground"
    n "Beaten and unconcsious"
    n "Husband hears voices outside the shed"
    n "Inn keeper rushes in with couple of men following him"
    
    menu:
        "Husband attacks them with rage caused by his beaten wife":
            jump attackInnKeeper
            
        # paeta raivopäissään yliluonnollisilla voimilla, jättäen vaimon? pois?
        "He escapes by jumping trough a window":
            jump chase
    
label attackInnKeeper:
    
    n "Straight away men sees husband's fierceful eyes, fear grips their heart"
    n "They rush out from the shed yelling and screaming for help"
    n "Husband charges after them"
    n "Men run onto street where other villagers have began to search the cause of making animals goes so nervous"
    n "They see the beastly husband chasing fellow villagers"
    n "Armed with pitchforks and tools they charge towards the husband"
    n "He fights wildly slaying many villagers but more keep coming and charging"
    n "Finally villagers manage to knock the husband on the ground and chain him up"
    n "Villagers gathers around him yelling and beating him with everything they got into their hands"
    
label blackness:

    scene bg black with dissolve
    
    pause 2
    
    n "In the shed woman starts to get conscious"
    n "She hear a lot of sceaming and yelling, dogs barking and howling"
    n "She rises and leaves the shed"
    n "Just before voices are starting to approach"
    n "She slips into shadows of alley"
    n "People appears from corner rushing into shed"
    n "Yelling all things she can't understand"
    n "Husband nowhere to be seen"
    n "All alone in the darkness"

label playAsWoman:

    scene bg black
    show woman at top with fade
    
    pause 3
    
    n "She sneaks in the shadows of alley towards the voices coming from street"
    n "On the street she sees her husband lying on the ground in chains"
    n "He is beaten up and bloody"
    n "There are also bodies lying on the ground"
    n "Villagers have gathered around and they look furious, yelling and pointing to husband"
    n "A man is talking loudly, trying to calm them"
    n "While she follows the happening, trying figuring out how to safe her husband, a old woman comes to ally"
    n "Lady spots her and freeze in fear, looking at her nervously"
    
    menu:
        "She attacks to woman before she makes an alarm":
            jump attackOldWoman
            
        "She scares the woman and tries to escape":
            jump castleWomanEscape
            
        "She try to calm her hoping that woman is friendly":
            jump oldWoman
            
label attackOldWoman:
    
    n "She charge towards the old woman"
    n "Woman tries to turn and run away, screaming out loud"
    n "Wife catch her, knocking her down and beating her desperately"
    n "During the struggle, she hear a lots of voices from people approaching quickly "
    n "Old woman screams even louder than before and she can't get her quiet"
    n "She realizes escaping is too late now"
    n "People rushing to the alley and charging to wife"
    n "Quickly they tide her down and drag her to the street next to her husband"
    n "Old woman is lead there all bloody and badly beaten"
    n "People get more furious looking to be in rage"
    n "They drag the man and the woman violently onto quickly build bonfire tiding them on to poles"
    n "They light up the bonfire and flames starts to rise, licking both of them"
    n "Pain rises towards unbearable state"
    n "They scream, they beg for mercy but no one listens"
    n "They burn at the stake, together"
    n "The end"
    
label castleWomanEscape:
    
    n "Running away for her life he manage to get out of village"
    n "She just keeps running ending up to castle"
    n "There she finds an old man"
    
    #DIALOG 2 with 
    
label oldWoman:
    
    n "Fear in the old woman's eyes start to change to warm and kind"
    n "She smiles at you, goes to the door, opens it and waves to wife to follow her inside"
    n "Inside she show drawings from village history"
    n "There are drawings of villagers and people which seems to live in forest"
    n "There seems to be hostility between them"
    n "Woman draws a small map leading to a castle"
    n "She gives an amulet to the wife and points the castle on map"
    n "Wife try to explain that she need help to rescue her husband"
    n "Woman just points to map and show the direction"
    n "Without better plan, wife decide to go to that castle" 
    
label castleWoman:
    
    scene bg black
    show castle at top
    
    n "She takes the map and the amulet and leaves"
    n "She finds the castle and an old man in there" 
    
    # DIALOG 2
 
label chase:
   
    if chaseRounds > 0:
    
        hide screen scrBorderTop
        hide screen scrBorderRight
        hide screen scrBorderBottom
        hide screen scrBorderLeft
        
        hide imgBorderTop
        hide imgBorderRight
        hide imgBorderBottom
        hide imgBorderLeft
        
        $ topBorderOn = False
        $ rightBorderOn = False
        $ bottomBorderOn = False
        $ leftBorderOn = False
        
        $ onTop = False
        $ onRight = False
        $ onBottom = False
        $ onLeft = False
        
        $ randomValue = renpy.random.randint ( 0 , 3 )
        
        # random value for picking which border image to show
        if randomValue == 0:
            $ chaseRounds -= 1  
            show imgBorderTop
            $ topBorderOn = True
            call joku
                
        elif randomValue == 1:
            $ chaseRounds -= 1  
            show imgBorderRight
            $ rightBorderOn = True
            call joku
        
        elif randomValue == 2:
            $ chaseRounds -= 1  
            show imgBorderBottom
            $ bottomBorderOn = True
            call joku
        
        elif randomValue == 3:
            $ chaseRounds -= 1  
            show imgBorderLeft
            $ leftBorderOn = True
            call joku
        
        # if player doensn't manage to get mouse pointer on right area in time
        if successEscape == False:
            jump $ onFailureLabel
            
        # label seems to need a something to pause, pause command or text string etc. 
        # otherwise it just skip the label
        pause
    
    # if player completes all rounds
    jump $ onSuccessLabel
        
        
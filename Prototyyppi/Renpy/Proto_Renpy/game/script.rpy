python:
    import renpygame # this pygame implementation uses renpygame-module
    import renpygame as pygame
    from renpygame.locals import * # renpygame import-style for pygame
    pygame.init() #this turns pygame 'on'
    
init:    
    image black = "#000000"
    image village = "images/scans/village.jpg"
    image village2 = "images/scans/village2.jpg"
    image mountain = "images/scans/mountain.jpg"
    image mountain2 = "images/scans/mountain2.jpg"
    image castle = "images/scans/castle.jpg"
    image unconscious = "images/scans/unconscious.jpg"
    image tree = "images/scans/tree.jpg"
    image tree2 = "images/scans/tree2.jpg"
    image nature = "images/scans/oneWithNature.jpg"
    image woman = "images/scans/woman.jpg"
    image man = "images/scans/man.jpg"

    image borderTop = "images/borders/top.png"
    image borderRight = "images/borders/right.png"
    image borderBottom = "images/borders/bottom.png"
    image borderLeft = "images/borders/left.png"

    define n = Character( 'Narrator', color="#ffffff" )
    define om = Character( 'Old man', color="#00ff00" )
    define vl = Character( 'Village leader', color="#ff0000" )
    define ik = Character( 'Innkeeper', color="#0000ff" )
    define h = Character( 'Husband', color="#00ffff" )
    define w = Character( 'Wife', color="#ff00ff" )
    define ow = Character( 'Old woman', color="#ffff00" )
            
label start:
    ################################################################################################
    # global variable
    
    play music "audio/music/Tribal Ritual.wav" loop fadein 3.0
        
    # stuff for chase label
    $ chaseRounds = 5   # how many times border loop will run
    $ randomBorder = 0  # determines which border to show
    
    # defines next label to go depending if chase was success or not
    $ lblChaseSuccess = ""
    $ lblChaseFailure = ""    
    
    # dialog category anwers
    # categories determines which story branch is selected
    # the number presents how many times player needs to select that category answer to be activated
    # ie. player answer 2 time from help category, then helping branch of story is selected
    # 2 = default, 1 = weighting in that category
    $ dialogAttack = 2
    $ dialogJoin = 2
    #$ dialogHelp = 2 not in use atm
    
    # story flags
    $ manInBeastForm = False    
    $ womanHaveAmulet = False
    
    ###############################################################################################
    scene black
    
    n "Let me tell you a story which happened here a long time ago"
    n "The story is about a wandering couple who looked a shelter from a local village inn"    
    
label villageStart:
    
    scene black
    show village at top with dissolve
    
    pause 1
    
    n "After a long and weary travel, a man and a woman finally saw a landscape which entwined a little village in"
    n "They headed into inn and rent a room for a night"
    n "After a bath and a warm meal they fall into sleep"
    n "At the middle of the night, man suddenly awakes for a scream of her wife"
    n "He saws a punch of men in the room tiding the wife down"
    n "Husband charges towards the men"
    n "He fight hard and brave but there are just too many of them"
    n "They knock husband down and he falls in unconsciousness"
    

label unconsciousHusband:
    
    scene black
    show unconscious at top with dissolve 
    
    pause 1
    
label husbandAwakesInForest:
    
    scene black
    show village2 at top with dissolve
    
    pause 1
    
    n "Husband begins to gain his consciousness opening his eyes"
    n "He is badly beaten with his clothes ripped"
    n "He doesn't see his wife"
    n "He tries to find her and yell her name but he can't find her"
    n "From the hill he sees that same village down a valley"
    n "To other direction land is rising up towards a mountain"
    n "There's a old castle high on mountain side"
    
    menu:
        "He returns to village hoping his wife is still there alive":
            jump husbandReturnVillage
            
        "He continues search his wife in the forest":
            jump husbandSearchForest
            
        "He starts climbing up to mountain side towards the castle":
            jump husbandSearchMountainSide
            
label husbandReturnVillage:
    
    scene black
    show village at top with dissolve
    
    pause 1
    
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
            jump husbandLeaveTown
        
        "He rises from the ground and start to run deeper into village":
            jump husbandFindInn

label husbandSearchForest:
    
    scene black
    show tree at top with dissolve
    
    pause 1
    
    n "He wanders to small glade, a huge old oak in the center"
    n "There are people gathered around the tree"
    n "They don't have clothes, a thick dirt covering their skin"
    n "They look like a people but their behauvior reminds more of a animal"
    n "Someone spots him and screams alarming the others"
    n "Everyone nails their eyes on husband, silent surrounds the glade"
    n "People starts to approach the husband"
    
    menu:
        "Fear hits him and he turns to run away in horror":
            # refers to first jump labels from chase label
            $ lblChaseSuccess = 1
            $ lblChaseFailure = "chaseFailureForestPeople"
            play music "audio/music/Dominate loop.wav" loop
            jump chase
            
        "He can hear his heart bounding but he force himself to greet the people":
            jump husbandGreetForestPeople
            
label chaseSuccessForestPeople:
    
    stop music fadeout 4.0
    play music "audio/music/Tribal Ritual.wav" loop fadein 4.0
    
    scene black
    show castle at top with dissolve
    
    pause 1
    
    n "He run for his life through the forest"
    n "Finally he thinks he lost the chasers"
    n "He stops to take a breath and looks around him"
    n "There's a castle rising in front of him"
    n "He decide to go in"
    n "He see a old man standing in hallway, like he was waiting him"
        
    $ dialogAttack = 1 # set dialog weight for attacking
    jump dialog1
    
    
label chaseFailureForestPeople:
    
    stop music fadeout 4.0
    play music "audio/music/Tribal Ritual.wav" loop fadein 4.0
    
    scene black with dissolve
    
    pause 1
       
    n "They are just too quick for him"
    n "They bring him down"
    n "People speaks and yells frantically to him and to each other"
    n "Husband can't understand what they are saying"
    n "He just lay on the ground waiting for the last hit taking his life away"
    n "But for his suprise people lift him up and start to push him forward"
    n "They begin to climb up to mountain"
    
label husbandIsTakenToCastle:
    
    scene black
    show castle at top with dissolve
    
    pause 1
    
    n "They arrive at the very old castle covered by vegetation"
    n "They go in and there's a old man sitting in the room"    
    
    $ dialogJoin = 1 # set dialog weight for joining
    jump dialog1

label husbandSearchMountainSide:

    scene black
    show mountain at top with dissolve
    
    pause 1
    
    n "He search and climbs higher and higher"
    n "But he can't find his wife"
    n "He begin to be close to castle"
    n "He can see a intimitating figure of it"
    
label husbandCastleOldMan:

    scene black
    show castle at top with dissolve
    
    pause 2
    
    n "He arrives at castle"
    n "Trying to find his wife without success"
    n "Suddenly he is aware of presens of somebody"
    n "Old man appears from shadows"
    n "He stares at husband with his sharp eyes in silence"
    
    jump dialog1
        

label husbandLeaveTown:

    scene black
    show village2 at top
    
    n "People quit the chase after he reach the woods"
    n "They seems to be too afraid to continue"
    
    menu:
        "He tries to search his wife in the forest":
            jump husbandSearchForest
            
        "He start climbing on mountain side hoping to get better view":
            jump husbandSearchMountainSide
            
label husbandFindInn:
    
    scene black
    show village at top
    
    n "He manages to lost villagers who followed him"
    n "Finally he finds the inn and goes in"
    n "There's a innkeeper and he looks very suprised to see you"
    
    jump dialog5

label husbandGreetForestPeople:
    
    scene black
    show tree2 at top with dissolve
    
    pause 1
    
    n "People gather around him, touching him and communicating with each other"
    n "They gather wood from old oak and build a big fire"
    n "They start dancing and singing wildly around a fire"
    n "Husband join the dance and they dance all night"
    n "Strong feeling begins to take a grip from husband, gettting stronger and stronger"
    n "He start to feel a strong wilderness in him which grows higher in every moment"
    n "Dance goes wilder and wilder"

label husbandChangeToBeast:

    scene black with dissolve
    n "At dawn the fire have turned to embers"    
    
label beast:
    scene black with dissolve
    show man at top
    
    $ manInBeastForm = True
    
    pause 1
    
    n "Husband stands whole awake breathing fresh morning air into his lungs eagerly"
    n "The blood is rushing in his veins like never before"
    n "He have never been so awake, so full of life"
    n "His instincts have become sharp as a predator's"
    n "Smelling thousands of scents"
    n "Hearing even tiniest crack"
    n "He feels like a wildest animal"
    n "He can smell the scent of his wife"
    n "A rush of adreline hits him"
    n "He starts to run like a jaguar following that scent"
        
label villageBeast:
    
    scene black
    show village at top
    
    n "The scent leads him back to village"
    n "He follows it deeper into village"
    n "He hears and smells the villagers and avoids to encounter with them"
    n "Village dogs starts to bark and howl, horses goes uneasy, every animal senses a beast"
    n "Villagers starts to gather wondering what hits the animals"
    n "The scent leads him at small shed behind the inn"
    n "He force himself trough the door and sees his wife laying on the ground"
    n "Beaten and unconcsious"
    n "Husband hears voices outside the shed"
    n "innkeeper rushes in with couple of men following him"
    n "Husband attacks them with his beastly rage"
    
    jump attackInnKeeper

label attackInnKeeper:
    
    n "As men sees husband's fierceful eyes, fear grips their heart"
    n "They rush out from the shed yelling and screaming for help"
    n "Husband charges after them"
    n "Men run onto street where other villagers have began to search what is causing the nervousness of animals"
    n "They see the beastly husband chasing fellow villagers"
    n "Armed with pitchforks and tools they charge towards the husband"
    n "He fights wildly slaying many villagers but more keep coming and charging"
    n "Finally villagers manage to knock the husband on the ground and chain him up"
    n "Villagers gathers around him yelling and beating him with everything they have at their hands"
    
label blackness:

    scene black with dissolve
    
    pause 1
    
    n "In the shed woman is starting to get conscious"
    n "She hear a lot of sceaming and yelling, dogs barking and howling"
    n "She rises and leaves the shed"
    n "Just before voices are starting to approach"
    n "She slips into shadows of alley"
    n "People appears from corner rushing into shed"
    n "Yelling all things she can't understand"
    n "Husband nowhere to be seen"
    n "All alone in the darkness"

label playAsWoman:

    scene black
    show woman at top with fade
    
    pause 5
    
label playAsWoman2:
    
    scene black
    show village at top with dissolve
    
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
    
    scene black
    show village at top with dissolve
    
    n "She charge towards the old woman"
    n "Woman tries to turn and run away, screaming out loud"
    n "Wife catch her, knocking her down and beating her desperately"
    n "During the struggle, she hear a lots of voices from people approaching quickly "
    n "Old woman screams even louder than before and she can't get her quiet"
    n "She realizes escaping is too late now"
    n "People rushing to the alley and charging to wife"
    n "Quickly they tide her down and drag her to the street next to her husband"
    n "Old woman is lead there all bloody and beaten"
    n "People get more furious when they see her condition"
    n "They drag the man and the woman violently onto quickly build bonfire, tiding them onto poles"
    n "They light up the bonfire and flames start to rise, licking both of them"
    n "Pain rises towards unbearable state"
    n "They scream, they beg for mercy but no one listens"
    n "They burn at the stake, together"
    
    n "The end"
    return
    
label castleWomanEscape:
    
    scene black with dissolve
    
    n "Running away for her life, she manage to get out of the village"
    n "She continue running until she's too tired to go on"
    n "When she looks around her she sees an old castle rising on mountainside above her"
    n "She decide to go explore it"
        
    jump dialog2
    
label oldWoman:
    
    scene black 
    show village at top
    
    n "Fear in the old woman's eyes start to change to warmth and kindness"
    n "She smiles at her, goes to the door, opens it and waves to follow her inside"
    n "Inside she starts to speak her about village history"
    n "There have been violence and fear building up among the years"
    n "A long time ago there was a man living in a castle nearby"
    n "He worshipped nature and lived among the animals"
    n "His methods were peaceful but looked odd for outsider"
    n "Some villagers were against his ways"
    n "Some were interested"
    n "Stories from the man growth and got wilder"
    n "Affecting more to villagers"
    n "Seperating them more"
    n "At the end some villagers left to castle and never came back"
    n "Villagers who stayed started to see castle as evil place where were practiced dark arts"
    n "They began to fear the place and the forest"
    n "Warning their children never to go there"
    n "Or a forest beast takes them"
    n "Old woman tells that she was one of the villagers who went into the castle"
    n "They practiced the lifestyle of the man"
    n "And together they learned how to become one with the forest"
    n "Merging to it"
    n "Learning from nature's harmony between all living"
    n "From cycle of death and birth"
    n "Studying the animalistic side inside them"
    n "Learning sincerity from their sincerity"
    n "From their presence in every moment"    
    n "And finally they released their inner animal free"
    n "Later woman returned to village and continued her living and practising in quiet"
    n "He tells to wife to go to castle and seek help from there"
    n "She gives an amulet to wife telling to give it to old man living there"
    n "It will get him convinced and to help her"
    n "Without better plan, wife decide to go to that castle" 
    
    $ womanHaveAmulet = True
    jump dialog2    

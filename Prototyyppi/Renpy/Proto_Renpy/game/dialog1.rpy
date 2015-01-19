label dialog1:
    
    n "For suprise he start to speak in common language"
    n "He asks what he can do for the man?" 
    
    menu:
        "Man wonders who is he?":
            $ dialogJoin -= 1
            jump dialog1Join1
        
        "He beg for help rescuing his wife from the village":
            #$ dialogHelp -= 1 not in use atm
            jump dialog1Help1
        
        "He thinks it's an ambush and escapes from the castle":
            jump dialog1Escape
        
        "He look at the old man suspiciously, wondering if he's one of the chasers":
            $ dialogAttack -= 1
            jump dialog1Attack1
        
label dialog1Join1:
    
    n "Old man tells about the castle and it's late owner"
    n "Owner were practising somekind of nature livingstyle"
    n "He lived with animals, becoming one of them in the end"
    n "Old man tells that he and the people in the forest were following that knowledge"
    n "Leaving civilation behind"
    n "And becoming one with the nature again"
    n "Old man says he was free to join them"
    
    if dialogJoin == 0:
        
        n "In desperation, too weary to fight on, he decides to join in hope of peace and safety for himself"
        jump dialog1Join3
    
    menu:
        "He wondered why would he join them":
            $ dialogJoin -= 1
            jump dialog1Join2
        
        "He promise if they can save her wife, they both will join them":
            #$ dialogHelp -= 1 not in use atm
            jump dialog1Help2
        
        "Man becomes angry: first they chase him and now they try to lure him in somekind of cult":
            $ dialogAttack -= 1
            jump dialog1Attack1
        
label dialog1Join2:
    
    n "Old man tells how they live in harmony with nature"
    n "How they learn from nature and animals"
    n "How the lifestyle leaves the greed and anger behind"
    n "Joining not seperating"
    
    if dialogJoin == 0:
        
        n "In desperation, too weary to fight on, he decides to join in hope of peace and safety for himself"
        jump dialog1Join3
    
    menu:
        "Man decide to join them":
            jump dialog1Join3
        
        "He decide escape to village thinking if villagers will release his wife in change of this information":
            jump dialog1Escape
        
        "He decide to attack, ending all these dark arts":
            jump dialog1Attack2
        
label dialog1Join3:
    
    n "Old man starts a ceremony"
    n "Husband feels his instincts growing stronger"
    n "His senses getting sharper"
    n "He can feel every moment like it's a water around him"
    n "He join to pulse of nature"
    
label dialog1OneWithNature:
    
    scene black with dissolve
    show nature at top with dissolve
    
    pause 1
    
    n "The end"
    return

label dialog1Help1:
    
    n "Old man tells that they don't interfere with civilized world if they don't have to"
    
    menu:
        "He promise if they can save her wife, they both will join them":
            jump dialog1Help2
        
        "He threaten the old man by killing him if they won't help him":
            jump dialog1Attack2
        
label dialog1Help2:
    
    n "Old man tells that they help their own people"
    n "So if one is captured in village they are willing to help"
    
    $ dialogJoin = 0 # promised to join. not in use atm in story
    
    jump dialog1Help3
    
label dialog1Help3:
    
    n "Old man calls people to castle and tells the situation to people"
    n "They leave to village"
    
    jump dialog3
    
label dialog1Attack1:
    
    n "Old man tells that he is one of the forest people, who chased him"
    n "He tells that the people sees him as their leader"
    n "But he thinks there have been misunderstanding because they don't want no harm to anyone"
    
    if dialogAttack == 0:
        
        "He only hears that the old man is their leader"
        "He must be behind the chase"
        "If he's the leader, by killing him they will leave him alone"
        "He laughs hysterically when attacking the old man"
        
        jump dialog1Attack2
    
    menu:
        
        "Husband explains that his wife is captured by some villagers and he's seeking help for rescuing her":
            jump dialog1Help1
        
        "He have heard enough of lies from this devious old man, it's time to end it!":
            jump dialog1Attack2
    
label dialog1Escape:
    
    scene black
    show village at top with dissolve
    
    n "Man runs back to village"
    n "People capture him and bring him to village leader"
    n "Man tells everything about the castle, the old man and the people who chased him"
    n "Leader tells about the castle and a dark forces of nature living there"
    n "By hearing there's just a old man and a punch of wild unarmed people they decide to march there"
    n "They take wife and husband with them, promisin to release them if all this is true and the evil can be defeated"
    
    jump dialog4
    
label dialog1Attack2:
    
    n "Man attacks to old man"
    n "Old man evades from attack with great agility"
    n "Hes behaviour changes more animalistic"
    
    if manInBeastForm == True:
            
        n "They both fight like a beasts"    
        n "With a fierce and vigour of lions"
        n "They roar and hit each other savagely"
        n "But like an older tigers gets defeated from their younger contenders eventually"
        n "The old man is getting weary and losing his strength"
        n "Man knocks old man down and bites his teeth to old man's throath"
        n "Biting until old man won't fight back anymore"
        n "Until he just lay on the floor still"
        n "Man rises from the floor blood dropping from his teeth"
        n "The eyes like a predator's he have become one of them"
        n "People have heard the fighting sounds and are gathering inside the castle seeing what have happened"
        n "They see the predator"
        n "Looking at them with hungry eyes"
        n "Attacking them with a great roar"
        n "Fighting against them like a wildest beast"
        n "Until getting one wound too deep to carrying on the fighting"
        n "The predator, former husband, lays on the floor next to the old man"
        n "And takes his last breath"

        scene black with dissolve
        pause 2
        
        n "The end"
        return
        
    else:
        
        n "Staight away he attacks to old man he sees his agility and strength"
        n "Old man fight like a tiger and he doesn't have a change to survive"
        n "He turns away and start running from his life, trying to get back to village"
        
        $ lblChaseSuccess = 2
        $ lblChaseFailure = 2
        play music "audio/music/Dominate loop.wav" loop
        jump chase
        
label dialog1ChaseFailureCastle:
    
    stop music fadeout 4.0
    play music "audio/music/Tribal Ritual.wav" loop fadein 4.0
    
    scene black with dissolve

    n "Other people join the chase"
    n "Man run for his life, as hard as he can"
    n "But he gets a hit which brings him down"
    n "An instant people are all over him"
    n "Like animals attacking the wounded prey"
    n "They bite, claw and hit him"
    n "Suddenly a loud yell stops them"
    n "The old man comes above the man"
    n "Rises him up saying \"We don't kill living, even if it's hostile towards us\""
    n "\"Let him go\""
    n "\"Maybe he learns a lesson about respecting life\""
    n "Then they leave"
    
label dialog1ChaseFailureCastle2:
    
    scene black
    show village at top with dissolve

    n "Man beaten badly but still able to return to village"
    n "With no more thoughts in his mind than returning to his love one"
    n "Villagers sees the beaten, savage looking man"
    n "Some yelling to him, some hitting him"
    n "Man continues deeper in village, ignoring the villagers"
    n "Villagers are gathering around him blocking his way"
    n "Dogs are barking ready to attack him in any time"
    n "A strong voice coming from behing of people they let a man come through"
    n "He's the village leader"
        
    jump dialog6
    
label dialog1ChaseSuccessCastle:
    
    stop music fadeout 4.0
    play music "audio/music/Tribal Ritual.wav" loop fadein 4.0
    
    scene black with dissolve
    
    n "He runs as fast as he can trough the forest"
    n "More people joins to chase him"
    n "But he is too fast for them"
    n "At the edge of village chasers gives up"
    n "Husband is safe from them"
    n "When he stop to take a breath, he looks around him"
    n "Seeing lot's of villagers watching him suspiciously"
    n "He looks at himselft and sees that his clothes are all ripped, he's bloody and covered in dirt"
    n "People are starting to yell at him but he doesn't understand them"
    n "They surround him and start acting agressive towards him"
    n "A strong voice coming from behing of people they let a man come through"
    n "He's the village leader"
    
    jump dialog6
        
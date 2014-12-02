label dialog1:
    
    scene black
    show castle at top
    
    n "For suprise he start to speak in common language"
    n "He asks what he can do for the man?" 
    
    menu:
        "Man wonders who is he?":
            $ dialogJoin -= 1
            jump join1
        
        "He beg for help rescuing his wife from the village":
            $ dialogHelp -= 1
            jump help1
        
        "He thinks it's a ambush and escapes from the castle":
            jump escape
        
        "He look at the old man suspiciously, wondering if he's one of the chasers":
            $ dialogAttack -= 1
            jump attack1
        
label join1:
    
    n "Old man tells about the castle and it's late owner"
    n "Owner were practising somekind of nature living"
    n "He lived with animals, becoming one of them in the end"
    n "Old man tells that he and the people in the forest were following that knowledge"
    n "Leaving civilation behind"
    n "And becoming one with the nature again"
    n "Old man says he was free to join them"
    
    if dialogJoin == 0:
        
        n "In desperation, too weary to fight on, he decides to join in hope of peace and safety for himself"
        jump join3
    
    menu:
        "He wondered why would he join them":
            $ dialogJoin -= 1
            jump join2
        
        "He promise if they can save her wife, they both will join them":
            $ dialogHelp -= 1
            jump help2
        
        "Man becomes angry: first they chase him and now they try to lure him in somekind of cult":
            $ dialogAttack -= 1
            jump attack2
        
label join2:
    
    n "Old man tells how they live in harmony with nature"
    n "How they learn from nature and animals"
    n "How the lifestyle leaves the greed and desire behind"
    n "Joining not seperating"
    
    if dialogJoin == 0:
        
        n "In desperation, too weary to fight on, he decides to join in hope of peace and safety for himself"
        jump join3
    
    menu:
        "Man decide to join them":
            jump join3
        
        "He decide escape to village thinking if villagers will release his wife in change of this information":
            jump escape
        
        "He decide to attack, ending all this dark arts":
            jump attack3
        
label join3:
    
    n "Old man starts a ceremony"
    n "Husband feels his instincts growing stronger"
    n "His senses getting sharper"
    n "He can feel every moment like it's a water around him"
    n "He join the pulse of nature"
    
    n "The end"
    return

label help1:
    
    n "Old man tells that they don't interfere with civilized world if they don't have to"
    
    if dialogHelp == 0:
        
        n "She gives the amulet to old man"
        n "She sees a tear coming from his eye"
        n "She hear him saying to himself \"I own this for her\""
        n "Old man focus himself and says that they will help her"
        
        jump help3
    
    menu:
        "He promise if they can save her wife, they both will join them":
            jump help2
        
        "He threaten the old man by killing him if they won't help him":
            jump fightOldMan
        
label help2:
    
    n "Old man tells that they help their own people"
    n "So if one is captured in village they are willing to help"
    
    $ dialogJoin = 0 # promised to join
    
    jump help3
    
label help3:
    
    n "Old man calls people to castle and tells the situation to people"
    n "They leave to village"
    
    jump dialog3
    
label attack1:
    
    n "Old man tells that he is one of the forest people, which chased him"
    n "He tells that the people sees him as their leader"
    n "But he thinks there have been misunderstanding because they don't want no harm to anyone"
    
    if dialogAttack == 0:
        
        "He only hears that the old man is their leader"
        "He must be behind the chase"
        "If he's the leader by killing him they will leave him alone"
        "He laughs hysterically when attacking the old man"
        
        jump fightOldMan
    
    menu:
        
        "Husband says there's his wife in the village which is about to getting harmed anytime now, will they help prevent it":
            jump help1
        
        "He have heard enough of lies from this devious old man, it's time to end it!":
            jump fightOldman
    
label escape:
    
    n "Man runs back to village"
    n "People capture him and bring him to village leader"
    n "Man tells everything about the castle, the old man and the people who chased him"
    n "Leader tells about the castle and a powerful, feared man who lives there"
    n "By hearing there's just a old man and a punch of wild unarmed people they decide to march there"
    n "They take wife and husband with them, promisin to release them if all this is true and the evil can be defeat"
    
    jump dialog4
    
label fightOldMan:
    
    n "Man attacks to old man"
    n "Old man evades from attack with great agility"
    n "Hes behaviour changes more animalistic"
    
    if manInBeastForm == True:
            
        n "They both fight like a beasts"    
        n "With a fierce and vigour of a tigers"
        n "They roar and hit on each other savagely"
        n "But like a older tigers gets defeated from their younger contenders eventually"
        n "The old man is getting weary and losing his strength"
        n "Man knocks old man down and bites his teeth to old man's throath"
        n "Biting until old man won't fight back anymore"
        n "Until he just lay on the floor still"
        n "Man rises from the floor blood dropping from his teeth"
        n "The eyes like a predators he have become one of them"
        n "People have heard the fighting sounds and are gathering inside the castle seeing what have happened"
        n "They see the predator"
        n "Looking at the with hungry eyes"
        n "Attacking them with great roar"
        n "Fighting like a wildest beast"
        n "Until getting one wound too deep to carrying on the fighting"
        n "The predator, former husband, lays on the floor next to the old man"
        n "And take his last breath"
        
        n "The end"
        return
        
    else:
        
        n "Staight away he attacks to old man he sees his agility and strength"
        n "Old man fight like a tiger and he doesn't have a change to survive"
        n "He turns away and start running from his life, trying to get back to village"
        
        $ lblChaseSuccess = 2
        $ lblChaseFailure = "chaseFailureCastle"
        
        jump chase
        
label chaseFailureCastle:
    
    n "Other people join the chase"
    n "Man run for his life, as hard as he can"
    n "But he gets a hit which brings him down"
    n "And instant people are all over him"
    n "Like animals attacking the wounded prey"
    n "They bite, claw and hit him"
    n "Suddenly a loud yell stops them"
    n "The old man comes above the man"
    n "Rises him up saying \"Maybe we act like a animals but we have a free will of a human\""
    n "\"And we have choosed to respect all living\""
    n "\"You can go freely\""
    n "\"And I hope you respect us and leave us alone\""
    n "Then they leave"
    n "Man beaten badly but still able to return to village"
    n "With no more thoughts in his mind than returning to his love one"
    n "Villagers sees the beaten, savage looking man"
    n "Some yelling to him, some hitting him"
    n "Man continues deeper in village"
    n "Villagers are gathering around him blocking his way"
    n "Dogs are barking ready to attack him in any time"
    n "A strong voice coming from behing of people they let a man come through"
    n "He's a village leader"
    
    $ chaseRounds = 5
    jump dialog6
        
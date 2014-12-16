label dialog4:

	scene black
    show mountain2 at top with dissolve
     
    menu:
        "Husband points to old man and yells to villagers \"There's your which! The root of all evil! Slay him and you'll be free!\"":
            jump dialog4Attack
        
        "You can both live side by side! There is no need for bloodshed!":
            jump dialog4Negotiation
        
label dialog4Attack:
    
    n "Husband's words rises villagers anger into rage"
    n "They charge againts the forest people"
    n "Both side hits and yells"
    n "It's a bloody and cruel fight"
    n "Fueled with fear and hatred"
    n "Corpses laying around the ground"
    n "Village leader and old man killing each other"
    n "Only man and woman standing still"
    n "Looking the bloody mess around them"
    n "They take each other by hand and starts walking back to village"
    n "Thinking of warm bath, hot meal and a bed back in village inn"    
    n "What a vacation they wandered"
    
    scene black with dissolve
    pause 2
    
    n "The end"
    return
    
label dialog4Negotiation:
    
    n "Village leader turn on husband looking angry"
    vl "It's you who caused this mess!"
    vl "I told the innkeeper to take care of you two straight away"
    vl "But ofcourse he had to let his lust getting into his brain"
    vl "You strangers are nothing but a menace everytime"
    vl "I suggest we end this now like we should have done straight away you arrived"
    h "But..."
    om "He attacked me once already"
    om "I too think we get the peace and harmony back when these two are dealt"
    n "People gathers around of the man and woman"
    n "Man looked at his wife"
    h "I warned you about these trips to backcountry but you just had to see some simple country living"
    n "People charged on the couple"
    n "Leaving behind nothing but a tale told by a fire"
    
    scene black with dissolve
    pause 2
    
    n "The end"
    return
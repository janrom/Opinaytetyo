label dialog5:
    
    n "Husband is relieved to see innkeeper"
    h "What is this madness?! First our room is attacked, then I wake up in the middle of forest beaten up and when I come back to village people acts hostile against me"
    h "And my wife, where is she?!"
    ik "It's suprise to see you..."
    ik "So you were attacked last night? I was asleep and didn't hear anything"
    ik "I thought you were still in your room"
    
    menu:
        
        "Why you are suprised to see me? You sure have noticed something related to attack":
            jump suspicious
        
        "Well let's check the room if she's still there":
            jump room
        
        
label suspicious:
        
    ik "Well coming through the front door looking like a one of those damn beasts in the forest"
    ik "I expected you to be still in the room"
    ik "I haven't noticed anything unusual"
    n "For a moment he looks nervous trying to get hold on himself"
    h "Why I don't believe you... You're nervous about something. Are you holding something from me?"
    n "innkeeper gives a husband an evil eye"
    ik "Well you're right. We were careless not to bury you deep"
    ik "But you're wife was just too tempting to waste time on you"
    h "What a hell..."
    ik "Yes it was us. And don't worry you're wife is still alive"
    ik "But that doesn't matter much to you"
    ik "Because you're about to take your last breath"
    n "Innkeeper takes a big knife under a desk and attacks towards the husband"
        
    $ lblChaseSuccess = 3
    $ lblChaseFailuer = "manLoseInnkeeper"
    
    jump chase
        
label room:
    
    n "Husband rushes the stairs upstairs where their room is"
    n "He opens the door and finds the room to be empty and cleaned up"
    h "What a hell! Why's the room is cleaned up?"
    h "Where is she?!"
    n "He still wonders why the room is cleaned when a hard punch hit onto his head"
    n "He fell to the floor fading into unconsciousness"
    n "Still faintly hearing innkeepers voice"
    ik "Don't worry. I'll take care of you're wife"
    n "Last thing the husband hears is the evil laughter coming from innkeeper"
    
    n "The end"
    return
    
label manWinInnkeeper:
    
    n "Husband manages to avoid innkeeper's attack"
    n "By the force of his swinging blade missing the target the innkeeper lose his balance, just enough that husband manage to hit him on the neck and bringing him down"
    n "Husband strugles the innkeeper forcing to tell where is his wife"
    n "Innkeepers struggles for his life but when his about to choke cries"
    ik "Shed backyard..."
    n "Husband release his grip and rushes to the backyard"
    n "He sees the shed and force himself trough the door"
    n "He finds his wife lying on the floor unconcsious" 
    n "She looks beaten"
    n "He tries to wake her up but she's too weak to respond"
    n "He takes her onto his arms and carry her away"
    n "Away from this cursed place"
    
    n "The end"
    return
    
label manLoseInnkeeper:
    
    n "Husband cannot avoid the swing of innkeepers blade"
    n "Blade bites his flesh causing an agoning pain"
    n "Bringing husband down on his knees"
    n "Innkeeper looks at him with his eyes wide open"
    n "Laughing from satisfaction"
    n "As he sinks his blade into husbands heart"
    
    n "The end"
    return
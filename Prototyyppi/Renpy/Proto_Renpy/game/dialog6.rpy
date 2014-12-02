label dialog6:
    
    vl "\"Why are you coming here like a savage scaring people?\""
    
    menu:
        "I come to get my wife back from those who took her":
            jump peaceful1
        
        "Give my wife back you savages!":
            jump hostile1
        
        "Let's make a deal. Give my wife back and I give you their leader":
            jump offer1
        
label peaceful:

    vl "What are you talking about, who took your wife?"
    h "Men attacked us in the inn last night, they attacked into our room and took my wife!"
    vl "Let's head to inn to get this clear"
    n "They arrive to inn where they find the innkeeper"
    v "This man is claiming staying here last night with his wife and they were attacked, do you know this man?"
    ik "I don't know him! The man is obviously one of those savages living in forest!"
    h "He is lying!"
    vl "So you are saying they didn't stay here last night?"
    ik "I'm sure of it. You can check the rooms all are empty at the moment"
    n "They check every room but all seems clean and unused"
    n "With no evidence and people remaining silent if they have seen the couple"
    n "Village leader believes his fellow villager the innkeeper" 
    n "Last thing the husband sees is a big smile with arrogant eyes on innkeepers face when he looks at him"
    n "Then a rage hits the husband, a pure rage"
    n "He attacks to innkeeper"
    n "People force the husband off from the innkeeper"
    ik "See, he's a savage! Look at that beast!"
    n "And so in fear and hatred villagers beat the beast to death"
    n "Last thing in his mind: is his wife safe, is she alive?"
    
    n "The end"
    return
    
label hostile:

    n "More villagers join attacking him"
    n "Man yells and curses them but they just get more furious"
    n "Nobody stops them and they beat the man to death"
   
    n "The end"
    return
    
label offer:

    vl "If you lead us to him we let your wife go"
    n "So they all know about his wife"
    n "But he leave that thought alone"
    n "Being releaved hearing his wife is alive"
    n "They make the deal and man sees his wife again"
    n "The moment of rejoin is left brief villagers forcing husband to show the way"
    n "People have gathered all kind of tools for weapons and lit torches for lighting the way"
    n "They march to castle"
    n "Villagers believe it's cursed place and none have been there before"
    n "They see strange looking people standing at front of the castle"
    n "Some villager yells \"Look! Beasts are there like we've warned\""
    n "They get nervous and scared, the lynch mood is changing into fear"
    n "Village leader steps front"
    vl "Now it's time to end this curse and living in fear! Let us lay the beasts!"
    n "Someone walks from the crowd standing front of castle"
    n "The old man. He begin to speak"
    om "We have lived alone, meaning harm to no one, hoping us left alone in peace"
    om "But feared that won't last. The time has come to make a solution for this"
    n "\"The only solution is you burnt at the stake!\" yells some villager"
    
    jump dialog4
    
    
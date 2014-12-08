label dialog2:
    
    scene black
    show castle at top with dissolve
    
    pause 1
    
    n "The castle looks very old"
    n "It's covered with vegetation"
    n "There's a lots of birds and small animals coming and going"
    n "Old man is standing near the gate feeding the animals"
    n "He spots the woman and wonders who is she"
    n "Wife explains about the villagers and her captured husband"
    n "She begs for help to help her rescuing her husband"
    
    if womanHaveAmulet == True:
        n "Old man sees an amulet on wife's chest"
        n "He recognise it and asks where she got it"
        n "She tell him about an old lady and how she guide her to this place"
        n "Old man seems to fade in memories"
        n "A drop of tear appears to corner of his eye"
        om "For old time sakes I will help you"
        
        n "Old man gathers people around and they travel to village"
        
        label dialog2Village:
            
            scene black
            show village at top with dissolve
            pause 1
    
            n "When they arrive they see all villagers gathered on village square"
            n "At center of the square, husband is tied on the pole which is placed on big pile of woods"
            n "Husband seems badly beaten"
            n "When villagers sees forest people coming, they get alarmed thinking they've came for revence"
            n "Old man talks to them saying they have came in peace"
            n "They don't seem hostile so villagers calms down a bit, staying suspicious still"
            vl "Why have you come here?"
            om "This woman came to seek help for rescuing her husband"
            w "What have you done to him!"
            n "Wife cries as she rushes to her husband"
            vl "That creature is a vile beast trying to kill our villagers!"
            w "He's no beast! He just tried to safe me from my capturers!"
            vl "Which capturers are you talking about?"
            w "The innkeeper captured me with his henchmen and tried to kill my husband!"
            ik "That is a lie! I have never seen those people"
            
            n "Old lady appears from crowd she's the one giving the amulet to wife"
            ow "I met this woman at a back alley of the inn"
            ow "I know she's telling a truth and inn keeper is lying"
            vl "How you know that?"
            ow "Because I sense the truth in people's heart"
            ik "Bah! She's a which! A conspirator with those forest beasts!"
            n "Old man comes up to old woman"
            om "I'm so glad to see you again, I've missed you"
            om "She can truly sense the truth in other's heart"
            om "We both gain that ability when living in the woods"
            om "But she chose to go back living in society"
            om "I'm glad you still have the sense"
            ow "I've keeped my heart open like we learned my dear friend"
            ik "You see! They both are whiches!"
            vl "You have to prove your words old lady"
            ow "Follow me to shed, there we can find proofs"
            n "So they leave to shed at backyard of the inn"
            n "They find a shed with front door smashed in"
            n "Inside they find a signs of fighting"
            n "There are blood and pieces from wifes clothes"
            n "People are still suspicious"
            n "Old woman and old man speaks to inn keeper and little by little he breaks"
            n "He hangs his head in shame and with breaking voice he tells about what happened that night"
            
            n "They were drunk sitting at inn"
            n "The couple only customers in their room"
            n "They talked about the couple"
            n "Wondering who they were and where have they come"
            n "In rising drunkenness"
            n "In rising desire towards wife"
            n "In rising jealousness towards husband"        
            n "Bitter towards their own lives"
            n "Their anger growing into blinding rage"
            n "Desire growing into blinding lust"
            n "Before they knew they were charging into room"
            n "Attacking against terrified husband and wife"
            n "Beating them unconscious"
            n "They locked wife in the shed and took husband into woods"
            n "They beat husband in intention to kill him"
            n "But as their drunkness were wearing off their rage was too"
            n "Hits changing less severe"
            n "They left husband lying on the ground and returned to inn"
            n "They went to shed but now their lust and anger had changed into confusion"
            n "Confusion and anger raising towards the deeds they'd done"
            n "Wife starting to get her consciousness back"
            n "Not knowing what to do, a fear getting into them"
            n "A wave of frustration rising, they fed it in each other"
            n "Suddenly starting to hit her until she didn't move"
            n "They left the shed and locked the door"
            n "Returning into their homes"
            n "Numb and tired"
            n "Afraid of the dawn"
            
            pause 2
            
            n "At next day they were too afraid to go check wife or husband, if they even knew where they had left him"
            n "They just tried to ignore all what had happened"
            n "Hoping the problem would solve by itself"
            n "Cleaning the room and continuing on their everyday lives"
            n "Man stopped his talking still hanging his head low"
            n "People heard the story and were shocked of what they have done"
            n "But still they sensed a remorse in the inn keeper and his partners in crime"
            w "There is none irreversible happened"
            w "I can forgive you"
            n "Husband still tied on the pole seemed not to feel exactly same way"
            n "People agreed that those men should meet consequences of their actions"
            n "With the lead of old woman and old man they started to teach that sensibility of heart to those men and all who was willing to learn"
            n "The couple stayed with them finding themselves becoming more attached to them and their arising kindness"
            
            scene black with dissolve
            pause 2
            
            n "The end"
            return
    
    else: 
        n "Old man tells that they don't interfere with civilized world if they don't have to"
        n "A man comes to old man and speaks to him in language she doesn't understand"
        n "Old man listens and thinks something awhile"
        om "It seems that there have been a stranger participated one of our ritual"
        om "He have got affected and left into village"
        om "Consequences can be unpredictable for those who doesn't hold the knowledge how to control them"
        om "So it seems that we have already interfered and now have to deal with the consequences"
        n "Old man gathers people around and they leave to village"
        
        label dialog2village2:
            
            scene black
            show village at top with dissolve
            pause 1            
        
            n "When they arrive, villagers are about to lit a bonfire the husband on it"
            n "Villagers get scared of the arrivals"
            n "Old man tries to calm them down telling they're came in peace"
            n "Wife rushes to her husband trying to untide him"
            n "The air is full of tension, ready to set in flames in anytime"
            vl "Why have you came here? Is this beast one of you?"
            om "We have come here to aid this woman to safe her husband"
                    
            w "He's no beast! He just tried to safe me from my capturers!"
            vl "Which capturers are you talking about?"
            w "The innkeeper captured me with his henchmen and tried to kill my husband!"
            ik "That is a lie! I have never seen those people"
            n "Old man tries to calm everyone down"        
            n "But villagers are in a heat of burning the beast of forest"
            n "And now the beast's minions have arrived to safe him"
            n "Someone throws a torch into bonfire"
            n "Flames starting arise immediatelly"
            n "Another torch is thrown"
            n "Wife cry for help"
            n "Forest people tries to prevent villagers for throwing the torches"
            n "And so the tension itself burst into flames"
            n "Swallowing all into blinding rage"
            n "Fighting against each other"
            n "No one listens when old man tries to calm them down"
            n "A rage overcoming reason"
            n "People killing each other"
            
            scene black with dissolve
            pause 2
            
            n "The end" 
            return
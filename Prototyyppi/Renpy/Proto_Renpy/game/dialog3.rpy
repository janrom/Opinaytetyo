label dialog3:
    
    scene black
    show village at top
    
    n "A boy playing near the village suddenly sees a man coming from a forest, then another"
    n "After a while there are dozens of people all approaching the village"
    n "They are naked covered in dirt"
    n "They remind him of animals"
    n "Boy get scared and runs into village yelling \"The beasts of forest are coming to kill us!\""
    n "Villagers gather around the boy wondering what he means"
    n "At the time forest people enters into village and they all see them"
    n "All hell breaks loose: people scream in fear, yell in anger or run everywhere trying to hide or find something for a weapon"
    n "Village leader appears to calm down people and trying to communicate with those wild looking people"
    n "The old man comes from among the forest people and they start a conversation"
    
    vl "Why have you came here? I assume you are those living in the forest?"
    om "You are right. We came on reguest of this man, pointing on husband"
    om "We don't mean to scare anybody or interfere your lives but this man came to seek help for rescuing his wife from this village"
    vl "I have never seen that man. Who are you?"
    h "Me and my wife came to this village last night and we stayed in village inn"
    h "In the middle of the night a punch of men attacked in our room"
    h "They knocked me unconsious and left in the forest"
    h "I haven't seen my wife since"
    vl "I see. So you believe someone in our village kidnapped her"
    vl "Well I can assure you we are all decent people and won't do such a crime"
    ik "And I can assure you that there were no couples staying my inn last night"
    h "You are lying! Sure someone have seen us?!"
    n "A tension between people in both sides is very tense"
    n "All are silent like waiting a feather to drop and fighting to start"
    n "All of them remains silent"
    om "So someone is lying here"    
    n "\"It's him!\" both the man and innkeeper yells to each other"
    n "Villagers and forest people starts to yell to each other"    
    n "Village leader and old man manage to calm them down"
    n "They agree to search the inn if wife can be found"
    n "Husband can't but follow the crowd"
    n "They search the inn but all rooms looks clean and unoccupied"
    n "Innkeeper tells that there's no one staying in at the moment"
    n "Village leader and old man looks to husband and tells that there's nothing more they can do"
    n "People from each group starts to accuse each other from kidnapping"
    n "Tension is about to burst into flames"
    
    menu:
        "Husband tries to convince others that innkeeper is lying and hidin something":
            jump dialog3Accuse
        
        "He runs out starting desperatelly seek and yell wifes name":
            jump dialog3Seek
        
        "The tension of people and desperation from losing his wife, the husband attacks against the innkeeper":
            jump dialog3Attack
        
label dialog3Accuse:
    
    n "Old man believes the husband have no reason to make up such accusation"
    om "Why would he accuse that man otherwise which he clearly doesn't know"
    n "Village leader is furious to them still keep accusing his fellow villager after he proofed that the inn is empty"
    vl "You come here with these man-beasts accusing an innocent man!"
    n "That gives a last spark which explodes the tension into furious fight"
    n "The fight is hard and is over quickly"
    n "Leaving behind a lot of corpses from both sides, the husband among them"
    n "Rest of people continuing their living in their style"
    n "Gaining nothing but a story to warn their children about a danger lurking nearby"
    
    scene black with dissolve
    pause 2
    
    n "The end"    
    return
    
label dialog3Seek:
    
    n "The husband runs to backyard leaving people yell to each other"
    n "He starts to yell his wife name"
    n "He yells and yells sliding into desperation"
    n "Dropping into his knees"
    n "A bitter tears runs on his face"
    n "Sounds are fading away"
    n "Only a faint sound of his wife calling him"
    n "A soft memory of her voice warming him"
    n "His eyes quickly spreads wide open"
    n "He can actually hear her voice!"
    n "He sees a shed next to him"
    n "Rushes on the door and brakes the door in"
    n "His wife is laying on the floor"
    n "Bloody and beaten but still alive"
    n "He kneel down next to her and close her into his arms"
    h "Finally I found you my love"
    n "He burst into tears of joy"
    ik "So you finally managed to find her"
    ik "That's too bad for both of your sakes"
    n "innkeeper rises his shovel"
    n "And starts hitting them until they both lays on the floor silent"
    n "Both holding each other"
    n "Finally together"
    
    scene black with dissolve
    show woman at left with dissolve
    show man at right with dissolve
    
    pause 2
    
    n "The end"
    return
    
label dialog3Attack:
    
    n "By attacking against innkeeper the husband launches a total mayhem"
    n "Everybody attacking against each other"
    n "With a furious rage husband crushes the innkeepers skull"
    n "Blood spraying on husband covering him all over"
    n "A loud sound caused by that crushed skull stops people from fighting"
    n "They all see a man covered in blood looking at them with his mad eyes"
    n "A smile on his face caused by a lunatic satisfaction he got by killing that liar"
    n "A revenge for his wife"
    n "People starts to run out of the room in hysteria"
    n "Leaving the husband alone"
    n "He take a one last look of the bastard who caused all that misery to him"
    n "He sees a key on a string hanging on the innkeepers chest"
    n "It must had been hidden under his shirt"
    n "Husband takes the key and leaves the room"
    n "He walks outside and sees a shed on the backyard"
    n "He sees the key on his hand and walks to shed"
    n "Put the key on the lock and opens it"
    n "Inside he sees his wife lying on the floor unconscious"
    n "All numb from the bloodbath and sudden reunion with his wife"
    n "He lift her onto his arms"
    n "And start walking away from the village"
    n "Leaving only a blood droppings behind"
    
    scene black with dissolve
    pause 2
    
    n "The end"
    return
    
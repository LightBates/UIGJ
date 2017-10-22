label EndScene:
    
    if HasBaby and Crowd:
        scene bgFaerie
        show crowdt
        with Fade(1.0, 1.0, 1.0)
        "A violent rustling erupts around you, the tide of noise stopping you in your tracks."
        "A crowd of figures flow forth from the trees and the brush, an elegant wave of shapes that envelops you and Glen in its center."
        "You press close to one another, back to back, Glen clutching the baby and you gripping your knife."
        Cr "\"Our child,\" they say as one."
        "Glen pulls the baby nearer to their chest."
        Cr "\"You have found our child. You have brought her back.\""
        H "\"Your child?\""
        Cr "\"Stolen,\" the chorus says, pained. \"Torn away, then hidden from our view.\""
        "The crowd stretches out their hands and one body steps forth from the herd."
        Cr "\"She must return home.\""
        "Glen looks at you, question in their eyes, brows furrowed."
        menu:
            "Give them the baby":
                $ renpy.notify("Pacifism +1")
                "You nod at Glen. The strange swarm does seem to care deeply for the child, and things that belong to this wild forest should not be removed."
                "Glen nods back."
                "They ease the infant into the arms of the awaiting figure."
                Cr "\"Thank you\" the crowd murmurs." 
                "The rustling roars around you once again and you snap your hands up to cover you ears against it."
                "Soon enough, they are all gone. You take Glen’s hand."
            "Fight Back":
                $ renpy.notify("Violence +1")
                "You have no way to be certain that the child belongs to this eerie assemblage."
                "And even then, being absorbed into this anonymous mass seems a ghoulish fate."
                "You won’t let them. You brandish your knife and swipe at the figure in front of Glen. It hisses and sinks back into the swarm."
                "You stab at the next that approaches, and the next, and the next, but there are so many and only one of you."
                "They overtake you in a roar of rustling."
                "When the sound subsides and the tide recedes, the child is gone."
                "You help Glen to their feet and hug them tightly."
    
    if ( math.fabs(empathy) > math.fabs(pacifism)):
        if empathy > 0:
            jump Empathy
        else:
            jump Apathy
    elif ( math.fabs(empathy) < math.fabs(pacifism)):
        if pacifism > 0:
            jump Pacifism
        else:
            jump Violence
    else: 
        if  renpy.random.randint(0,1) < 1:
            if empathy >= 0:
                jump Empathy
            else:
                jump Apathy
        else:
            if pacifism >= 0:
                jump Pacifism
            else:
                jump Violence
    
    
          
    ###Might need rework compared to all the other endings
label Apathy:
    scene bgFaerie
    with Fade(1.0, 1.0, 1.0)
    "And suddenly, a room."
    "You’re not sure how you know it’s a room- the landscape still stretches for interminable miles in every direction- but you feel the confines."
    "You and Glen."
    "The forest is an illusion."
    "These walls are an illusion."
    "Whichever, doesn’t matter, leads to the same place. In front of you, a ring."
    "Fungus split and seeping like open sores. Delicate flowers intertwined, fragrant petals stained. The fairy ring."
    "If you step inside, there’s no going back, but already, there is no exit."
    "You look at Glen. Glen looks at you."
    "You step, together." 
    "..."
    "Nothing, at first, but then a breeze"
    "The wind carries a melody that may have once been familiar, but now you’re too distant to know why."
    "Too distant to know anything anymore."
    "Nothing matters. There is no horror, no specter they can bring before you that will bring fear or hesitation into your heart."
    "Nothing in this forest has fazed you, and nothing ever will."
    "Even if you are to wander here forever. Even if Glen is to waste away beside you, their hand slipping from yours one last time."
    "Their weight will fall to the ground and off of your shoulders, forever."
    return

label Empathy:
    scene bgFaerie
    with Fade(1.0, 1.0, 1.0)
    "And suddenly, a room."
    "You’re not sure how you know it’s a room- the landscape still stretches for interminable miles in every direction- but you feel the confines."
    "You and Glen."
    "The forest is an illusion."
    "These walls are an illusion."
    "Whichever, doesn’t matter, leads to the same place. In front of you, a ring."
    "Fungus split and seeping like open sores. Delicate flowers intertwined, fragrant petals stained. The fairy ring."
    "If you step inside, there’s no going back, but already, there is no exit."
    "You look at Glen. Glen looks at you."
    "You step, together." 
    "..."
    "Nothing, at first, but then, a breeze."
    "It picks up out of nowhere, stirring the leaves and making the circle dance."
    "The rustle of the foliage sounds like whispers, sliding over and sluicing through each other."
    "They’re harsh enough to catch, to illicit the jerk of your head, but no matter how hard you listen, you can’t make out the words."
    show glen at left
    with dissolve
    "Glen starts to shake beside you, at first as though with a chill, but ever and ever harsher, until they’re convulsing in place, body bending unnaturally."
    show harper at right
    with dissolve
    H "\"Glen! GLEN!\""
    "You move to reach out to them, but find yourself rooted in place, vines grown over your ankles."
    "There are no thorns to bite into your flesh, but enough movement chafes them against your skin and causes it to itch and burn."
    hide glen
    show glenchange at left
    with dissolve
    "Glen’s hood falls back to show their sharp face, their eyes turned milky white, their mouth agape as an ill moan grates out of it."
    "It seems to scrape down their throat, something half beast, with their gaze turned toward the canopy."
    "Something in your memory flickers, like a zoetrope dancing across your mind."
    hide glenchange
    hide harper
    with dissolve
    G "\"It’s not- I don’t think I’m right, Harper.\""
    H "\"What does that mean?\""
    G "\"I’m not the way I should be.\""
    "And there’s a translucence to their skin, green veins feathering out along their temples."
    "Just for a second, just in a trick of the light. But it’s not the first time. And it’s not the only thing."
    "Their eyes catching the lantern and throwing a glare."
    "Their love for meat best when it’s extra bloody and the way their teeth can shred."
    H "\"Well there’s nothing to be done about it, nothing that should. You are Glen, as you are, and someone we all treasure.\""
    "Glen’s gaze is far away, their mind cast adrift as well."
    "They look at the wall of your room, but are seeing much, much further beyond."
    G "\"Some things... could be done. People could be made to reckon.\""
    "The forest. Without them saying, you know it’s of what they speak."
    H "\"Those things- Those people- \""
    G "\"My people.\""
    H "\"We are your people, I am your people. This village, your parents. You have spent your life with us, is that not enough?\""
    H "\"Does that not give us some measure of worth?\""
    "Glen chews at their lips, can’t meet your eyes as you search for their gaze, trying to pull it back to you."
    G "\"I have to know, even if it’s a disappointment. It’s just something I have to know. Read me?\""
    "Their face is set, their expression firm. Sure. Glen is always sure."
    "H \"I read.\""
    "Glen is going to do this, without or without you. And no one should brave the forest alone."
    H "\"Next week, when pa is making his run.\""
    G "\"Today. Now. I packed us lunch. I fetched us water. Just say yes.\""
    "You suppose it was inevitable. So many end up in the forest."
    "It draws them like moths to the flame and still they stay, stubborn and sure. So sure that they belong in these hills."
    "Perhaps that’s just the order of things, perhaps this is part of the ecosystem, the food chain."
    "The forest sits above them all and the forest needs to feed."
    H "\"Yes. Today. Now.\""
    "You stand and offer your hand. Glen smiles as they take it, and the sunshine on their face is so worth whatever lies ahead."
    return

    

label Violence:
    scene bgFaerie
    with Fade(1.0, 1.0, 1.0)
    "And suddenly, a room."
    "You’re not sure how you know it’s a room- the landscape still stretches for interminable miles in every direction- but you feel the confines."
    "You and Glen."
    "The forest is an illusion."
    "These walls are an illusion."
    "Whichever, doesn’t matter, leads to the same place. In front of you, a ring."
    "Fungus split and seeping like open sores. Delicate flowers intertwined, fragrant petals stained. The fairy ring."
    "If you step inside, there’s no going back, but already, there is no exit."
    "You look at Glen. Glen looks at you."
    "You step, together."
    "..."
    "Nothing, at first, but then, a breeze."
    "It picks up out of nowhere, stirring the leaves and making the circle dance."
    "The rustle of the foliage sounds like whispers, sliding over and sluicing through each other."
    "They’re harsh enough to catch, to illicit the jerk of your head, but no matter how hard you listen, you can’t make out the words."
    "Tiny, serrated edges feather along the petals and they start to seep a viscous, acrid liquid."
    "The fungi bubble and propagate, cancerously spreading across the ground."
    "The ring constricts, tighter and tighter, pushing you and Glen to the center, grasping at each other to stay balanced."
    "You don’t know what will happen if you try to break the barrier, but you’re sure it won’t end well, if there’s anything to say for the sickly spores and effervescent toxins rotting the forest around you."
    "Even as you hold your ground, stay standing, the air grows thick enough to choke."
    "Lights dance around your eyes, vision being blotted out like a lit piece of flash paper."
    show glen at left
    with dissolve
    G "\"Harper! Don’t let go of me, now. Not yet. You can’t, I won’t let you.\""
    "You feel them shake at you, violent with their desperation."
    "Your teeth rattle in your skull and your neck lashes back and forth, dislodging something you didn’t know was stuck."
    "The memories pool into your mind, like blood against your skull."
    hide glen
    with dissolve
    "Father’s trusted knife, betraying him for the first and only time."
    G "\"Wipe your hands. Clean them well. We can’t let anyone see.\""
    G "\"Just have to make it to the woods without suspicion. No one will follow us there.\""
    "The water in the bucket saturated with copper before you could even get underneath your nails."
    "It’s still sitting there- his life in a banded, wooden thing fit to splinter. The way the candlelight shimmered off the surface was so... enthralling."
    "You make sure to take the knife from him before you leave, no matter the mess."
    "Wiped off on his shirt, tucked into your belt."
    "You play it cool, follow Glen’s lead, walk out whistling as they bob and weave around you."
    "Your neighbors wave hi, your smile is set wide. The air is cool and crisp and you can just see the forest’s edge."
    "You’re not even sweating. Not anymore. You breathe easier, stand straighter, the further that you get."
    "By the time you reach the boundary between, well you can hardly even remember why you’re there."
    return

    
    
label Pacifism:
    scene bgFaerie
    with Fade(1.0, 1.0, 1.0)
    "And suddenly, a room."
    "You’re not sure how you know it’s a room- the landscape still stretches for interminable miles in every direction- but you feel the confines."
    "You and Glen."
    "The forest is an illusion."
    "These walls are an illusion."
    "Whichever, doesn’t matter, leads to the same place. In front of you, a ring."
    "Fungus split and seeping like open sores. Delicate flowers intertwined, fragrant petals stained. The fairy ring."
    "If you step inside, there’s no going back, but already, there is no exit."
    "You look at Glen. Glen looks at you."
    "You step, together."
    "..."
    "Nothing, at first, but then, a breeze."
    "It picks up out of nowhere, stirring the leaves and making the circle dance."
    "The rustle of the foliage sounds like whispers, sliding over and sluicing through each other."
    "They’re harsh enough to catch, to illicit the jerk of your head, but no matter how hard you listen, you can’t make out the words."
    "Everything unfolds around you, the fairy ring blooms."
    "It’s lush, heady, overwhelming as pollen and spores fill the space with cloying perfumes."
    "You feel your body slacken, your muscles loose and your form slouch."
    "Memories start floating to the surface, like reflections on the water. They shimmer and shift, never staying in quite the same frame."
    "It’s hard to make out the details, the fine lines, but the players, the notions, can’t be missed."
    "Glen’s voice tries to swim to you, lethargic and low and unintelligible."
    "It pounds inside your head, dull and throbbing as you try to hold onto something, anything. Sand slipping through your fingers. Glen, the forest, these flashes-"
    V "\"At the solstice, before the full moon. They take only two when they could have many.\""
    V "\"Who has such generosity in their hearts?\""
    V "\"Who loves this village more than themselves?\""
    "It was an easy choice, you think."
    "It seemed so, in this echo. You and Glen, together in everything. And oh what an adventure."
    "This didn’t have to be the end. To walk in the forest was not necessarily to die."
    "Perhaps those offered found a better life than could ever be had on the outside, and so that is why they never returned."
    "Perhaps it’s only sense of duty to their contract with the others and now they have their own community, just inside the copse."
    "Whatever the case, there was only one option, only one decision ever to be made."
    "Hand in hand to be anointed with oils, to be prayed over and given thanks by friends, neighbors, family."
    "And then?"
    "And then they simply walked. Along a pebble path, near a cool creek."
    return
    
label Alone:
    scene bgFaerie
    with Fade(1.0, 1.0, 1.0)
    "And suddenly, a room."
    "You’re not sure how you know it’s a room- the landscape still stretches for interminable miles in every direction- but you feel the confines."
    "You, alone."
    "The forest is an illusion." 
    "These walls are an illusion."
    "Whichever, doesn’t matter, leads to the same place. In front of you, a ring."
    "Fungus split and seeping like open sores. Delicate flowers intertwined, fragrant petals stained. The fairy ring." 
    "If you step inside, there’s no going back, but already, there is no exit."
    "You look around."
    "There is no one else to consult, no other voice to console you."
    "Glen is gone."
    "You left Glen behind."
    "You step."
    "..."
    "Nothing, at first, but then, a breeze." 
    "It picks up out of nowhere, stirring the leaves and making the circle dance."
    "The rustle of the foliage sounds like whispers, sliding over and sluicing through each other."
    "They’re harsh enough to catch, to illicit the jerk of your head, but no matter how hard you listen, you can’t make out the words."
    "The flowers begin to shrivel and blacken, their petals shrinking in, dissolving to dust."
    "Pods and fungi burst into rivers of rot."
    "You gag on the stench of decay filling the air and the sight of the withering foliage shakes loose your well-confined feelings."
    "They tumble, raw and hurting, like a waterfall through your ribcage and you gasp."
    "Glen, who you’ve known your whole life."
    "Glen, who stayed steadfast and loyal at your side."
    "Glen, the person who painted most of your world with color."
    "A piece of you is missing, missing because you tore it from yourself and threw it asunder."
    "Your history unfolds within your aching skull."
    "You see it so clearly, the two of you, your lives entwined."
    "You and Glen as children, playing chase and picking flowers."
    "You and Glen, older, weaving stories by the hearth."
    "Naming shapes in clouds side by side in the sun."
    "Neglecting chores to run wild in the fields."
    "Embarking on this grand experiment in freedom, seeking the other side of the woods and the unknown world beyond."
    "..."
    "What changed?"
    "When did you stop caring? When did your insides first begin to atrophy?"
    "The full force of what you’ve become washes over you and you cannot bare it. You drop to your knees, your head in your hands, and you wail."
    "You wail and wail and wail for hours, months, decades, until your voice crumbles like the fairy circle to dust."
    "The walls close in. There is nothing left."
    "You are alone."
    return
    
    
label AloneBaby:
    scene bgFaerie
    with Fade(1.0, 1.0, 1.0)
    "And suddenly, a room."
    "You’re not sure how you know it’s a room- the landscape still stretches for interminable miles in every direction- but you feel the confines."
    "You, alone."
    "The forest is an illusion." 
    "These walls are an illusion."
    "Whichever, doesn’t matter, leads to the same place. In front of you, a ring."
    "Fungus split and seeping like open sores. Delicate flowers intertwined, fragrant petals stained. The fairy ring." 
    "If you step inside, there’s no going back, but already, there is no exit."
    "You look around."
    "There is no one else to consult, no other voice to console you."
    "Glen is gone."
    "You left Glen behind." 
    "You gaze at the infant in your arms and step."
    "..."
    "Nothing, at first, but then, a breeze."
    "It picks up out of nowhere, stirring the leaves and making the circle dance."
    "The rustle of the foliage sounds like whispers, sliding over and sluicing through each other."
    "They’re harsh enough to catch, to illicit the jerk of your head, but no matter how hard you listen, you can’t make out the words."
    "The baby opens its mouth and yowls, the loudest and most painful sound the child has made in these woods, splintering in your ears."
    "Around you, the foliage of the fairy ring rises, grows tall."
    "Limbs sprout from flowers, their stems parting into legs parting into long clawed feet."
    "Fungi expand into hunched, saturnine beasts. Roaring monsters bloom around you and you have no way to retreat."
    "In your arms, the infant continues its drawn-out shriek and fights against your hold."
    "Before your eyes, it too changes"
    "Purple blossoms over cheeks and belly. Teeth sprout in that open mouth. Fingers extend, curve into long talons."
    "They match the horrors around you."
    "The tide of realization washes over you, heavy enough to bring you to your knees."
    "You are surrounded."
    "You cry out, but you know nobody can help you. Nobody will. Nobody is here."
    "Glen is gone"
    "..."
    "The monstrous swarm descends."
    return


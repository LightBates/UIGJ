label InTheTree:
    $ Act2Scenes.pop(nex)
    scene bgAct2
    "The forest runs deeper than any you’ve entered. For a moment, you imagine weaving through its gnarled roots and branches forever."
    G "“Are we lost?” Glen asks as you push the thoughts from your mind."
    H "“No,” you respond firmly. “We just haven’t found our way yet.”"
    "A wail comes from a break in the leaves above you, but all you can see is black."
    if HasBaby = true:
        "“W-What was that?” Glen asks, holding the baby closer. “It sounded like a monster.”"
    else:
        G "“W-What was that?” Glen asks, latching onto your sleeve. “It sounded like a monster.”"
    "You would tell Glen there are no such thing as monsters, but you don’t lie to Glen."
    "You squint at the shadows of the tree, and see two lights. They look like a break in the leaves, where the sun shines through, but then they blink."
    "The voice comes again, ragged and desperate."
    "“Something’s got me! I can’t... get down...!” it pleads, as leaves fall from above you and down to the forest floor."
    G "“Harper.”"
    "Your eyes fall to the left, where an ancient rope wraps around the tree and up into the canopy, where the lights stare back."
    G "You feel a tug at your sleeve. “We need to go, Harper. It’ll catch us if we don’t. Please.”"
    if HasBaby = true:
        G "Glen looks at the baby in their arms, then back at you. “Harper.”"
    
    menu:
        "Cut the rope":
            $ pacifism -= 1
            $ empathy -= 1
            $ renpy.notify("Violence +1\nApathy +1")
            "You pull the knife from your belt. Specks of light between the leaves reflect from its blade."
            "Glen backs away, and you begin to saw at the rope, and watch as the weight it holds starts to pull it apart."
            G "“Harper, it’ll be fine, just come on.”"
            if HasBaby = true:
                "Glen smiles, relieved, and coos softly at the baby as you continue into the woods. Something thuds behind you."
            else:
                "You step away from the tree, and don’t turn to look back. Glen holds out a trembling hand, and you take it until the shaking stops."
                "Something thuds in the woods behind you."
        "Climb up the tree":
            $ pacifism += 1
            $ empathy += 1
            $ renpy.notify("Pacifism +1\nEmpathy +1")
            G "“Harper...” You grasp the lowest branch of the tree, and begin to hoist yourself up."
            H "“I’m going to see what it is.”"
            "The two lights from the canopy stare back at you from within a shadow that looms near a twisted figure, tied with rope."
            "The person opens their mouth to scream again, but the shadow clamps it shut."
            "The knife gleams in the belt at your waist. You pull it free and brandish it at the shadow with two eyes."
            "Its form recoils and splinters, split not by the blade but by the light it reflects."
            "The shadow dissipates, hit by specks of light filtered through leaves and perfected by the knife’s perfect edge."
            "You cut the ropes, carefully."
        "Leave with Glen":
            if HasBaby = true:
                $ pacifism -= 1
                $ empathy += 2
                $ renpy.notify("Violence +1\nEmpathy +2")
            else:
                $ pacifism -= 1
                $ empathy += 1
                $ renpy.notify("Violence +1\nEmpathy +1")
            H "“...Okay. Okay. We’ll leave.”"
            "You turn to go, giving the tree one last look."
            "You walk deeper into the forest, and ignore the thump behind you."
            
    $ nex = renpy.random.randint(0, len(Act3Scenes) - 1)
    $ renpy.jump(Act3Scenes[nex])



label Voices:
    $ Act2Scenes.pop(nex)
    scene bgAct2
    "It’s the cool, damp. It seeps through your skin and settles somewhere along the bones."
    "Glen notices it as surely as you, tugging their clothes closer and hitching their shoulders as though that might shield."
    "You stop to study the sensation, to look for clouds darkening the canopy, a lake reflecting a colder breeze."
    "You find a cave, or the mouth of it. It yawns in the distance, an open maw through which no light breaks, and— breathes."
    C "“Harper, sweet. Could it be?”"
    G "“Could it be?”"
    "Glen turns to you, expression brittle."
    H "“Not, not. Definitely not, how could it be?” "
    C "“Harper, sweet. Come and see me. Don’t you want to see your mother?”"
    "It drifts. It rides along that tepid gust, a breathy sigh."
    "It’s melodic, but discordant, like wind through holes in too smooth stone."
    "It sounds… like her. So like her, sad and sweet and not sure she wants to be heard."
    G "“But the forest— they thought her lost beyond the trees. Perhaps, well perhaps— like us.”"
    "You remember."
    "The bits of her dress, shredded through the tangles of branches."
    "The smell of burnt bread."
    "The way that dad peered down the path for several minutes and then looked no longer."
    C "“Don’t break her heart. Tender one, lovely thing. Come and see your mother, sweet.”"
    "It— hums."
    "The cave, the breeze, your mother..."
    "Dead."
    pause 1
    "Her ghost, perhaps."
    "A specter sent to ask why, why come into the forest now if you didn’t then."
    "More cruel than to never wonder, never wander, never seek to know."
    "The tune is something strange, something so like a knell."
    "And without your notice, without the thought of it, you’re crying."
    "Tears are streaking down your cheeks and your heartbeat feels faint, blood thin."
    H "“Stop.”" 
    H "“Stop crying.”"
    H "“Please, stop.”"
    G "“Go, oh won’t you? Go.”"
    
    menu:
        "Step into the cave":
            "The air turns musty, the fresh damp decaying so quickly you can taste it."
            H "“Mother?”"
            H "“Mother, please.”"
            "You wait in the dark for a reply, for the continuation of her song. You don’t remember when it stopped."
            "Sometime between the outside and now and you wanted it to stop, but now there’s just so much empty."
            "It’s a void that wants to grow, that erodes at you, breaking off bits and pieces to carry away downstream. Just so much silt."
            "And then? And then."
            C "“Harper, sweet? Oh dear, oh dear. You’ve come to see your mother-dust.”"
            C "“She’s waited for you oh, so long. Poor thing, sweet thing, sad thing. She wept oh so long, hoping— only— to see you.”"
            G "“Stop. Please don’t. Stop!” "
            "You turn wildly, thrashing in the empty to find the source of the echoing call."
            "It slides along the walls, slithers on the floor, drips slowly into your ear."
            H "“What do you want?”"
            C "“Oh, stay with me. Sit and stay awhile and talk with your mother. She’s waited so, so long and you have so much to say.”"
            
            menu:
                "Fold to the floor. Talk":
                    $ pacifism += 1
                    $ empathy += 1
                    $ renpy.notify("Pacifism +1\nEmpathy +1")
                    "Your knees give out and Glen puts a hand on your shoulder as you crumple."
                    "You can feel their eyes as they look to you, but your eyes are on the floor as your voice shakes."
                    H "“I don’t know what to say.”"
                    H "“There’s so much and yet, I have nothing.”"
                    C "“Oh, sweet. Lay awhile. Rest. Close your eyes.”"
                    "You think Glen is talking to you too. You think they are shaking you, even."
                    "You blink as your vision tips to the ceiling and you think you catch a glimpse of their face creased with worry, but everything is blurring."
                    "Like raindrops condensing on a window, the shapes and colors bleed and it blends all into one."
                    C "“Tender one, lovely thing.”"
                    "You swear you feel fingers in your hair."
                    
                "Scream and lash out":
                    $ pacisfism -= 1
                    $ empathy += 1
                    $ renpy.notify("Violence +1\nEmpathy +1"
                    "It’s too much."
                    "Much too much."
                    "Her voice, the song, this cold, damp; digging their fingers into your flesh, the pain cannot go on."
                    "Something scratches out your throat."
                    "Something beastial rips and claws."
                    "You are screaming and it is raw and the stone catches the sound and starts to shatter."
                    "The reverberation is too much. It catches and cuts."
                    "Slabs of shale splinter and crash to the ground."
                    C "“Oh, you’ve done it. What’ve you done?”"
                    "Your tears are hot now, they burn in streaks across your face."
                    "The place is coming down around you and you think you see Glen scrambling away, but everything is blurring."
                    "Like raindrops condensing on a window, the shapes and colors bleed and it blends all into one."
                    "Rubble batters at your shoulder, slices down your face."
                    "You ache and bleed, but you are screaming until the real pain stops."
                    "The cave collapses."
                    
                "Do nothing":
                    $ pacifism += 1
                    $ empathy += 1
                    $ renpy.notify("Pacifism +1\nEmpathy +1")
                    G "“We can’t stay here. You can’t stay here.”"
                    "They put their hand on your shoulder, then run their fingers up and through your hair."
                    "You’re not sure you like it, but the touch, it grounds you."
                    G "“That might be your mother, but it’s not her anymore.”"
                    G "“She died.”"
                    G "“She walked into the forest and maybe she’s something else, but the woman you knew, died.”"
                    "Glen is right. You know they’re right, but what’s the threshold on letting go?"
                    "When is the right time?"
                    "What are the right circumstances?"
                    C "“Dear thing, lovely sweet. Do not leave. Stay with me awhile.”"
                    H "“I love you, I really do.”"
                    "You walk away, and every step feels like it’s through broken glass."
                    "Frigid and fractured and compounding cut upon cut."
                    "But Glen is there."
                    "Glen holds you by the elbow, braces you as you buckle."
                    "They are crying, too, but the smile, out in the light."
                   "The further and further that you get, the wind rustles through the leaves, stones no longer present to whistle." 
        
        "Turn away and walk and walk and walk":
            $ pacisfism += 1
            $ empathy -= 1
            $ renpy.notify("Pacifism +1\nApathy +1"
            "The ground moves beneath your feet, fast and faster, starting to blur."
            "Glen calls after you, but it feels like the voice, like the cave calling for you to come back."
            "You don’t raise your head to look, you watch only for your own steps, only to make sure you don’t stumble and fall."
            "You can’t let it catch up with you."
            "Same as before, now you can just feel its breath over your shoulder, warm and wet."
            "It drifts down along your nape and so you run faster."





    
    
    
    $ nex = renpy.random.randint(0, len(Act3Scenes) - 1)
    $ renpy.jump(Act3Scenes[nex])
    

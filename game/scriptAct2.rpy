label InTheTree:
    $ Act2Scenes.pop(nex)
    "The forest runs deeper than any you’ve entered. For a moment, you imagine weaving through its gnarled roots and branches forever."
    G "“Are we lost?” Glen asks as you push the thoughts from your mind."
    H "“No,” you respond firmly. “We just haven’t found our way yet.”"
    "A wail comes from a break in the leaves above you, but all you can see is black."
    G "“W-What was that?” Glen asks, latching onto your sleeve. “It sounded like a monster.”"
    "You would tell Glen there are no such thing as monsters, but you don’t lie to Glen."
    "You squint at the shadows of the tree, and see two lights. They look like a break in the leaves, where the sun shines through, but then they blink."
    "The voice comes again, ragged and desperate."
    "“Something’s got me! I can’t... get down...!” it pleads, as leaves fall from above you and down to the forest floor."
    G "“Harper.”"
    "Your eyes fall to the left, where an ancient rope wraps around the tree and up into the canopy, where the lights stare back."
    G "You feel a tug at your sleeve. “We need to go, Harper. It’ll catch us if we don’t. Please.”"
    
    menu:
        "Cut the rope":
            $ pacifism -= 1
            $ empathy -= 1
            $ renpy.notify("Violence +1\nApathy +1")
            "You pull the knife from your belt. Specks of light between the leaves reflect from its blade."
            "Glen backs away, and you begin to saw at the rope, and watch as the weight it holds starts to pull it apart."
            G "“Harper, it’ll be fine, just come on.”"
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
            $ pacifism -= 1
            $ empathy += 1
            $ renpy.notify("Violence +1\nEmpathy +1")
            H "“...Okay. Okay. We’ll leave.”"
            "You turn to go, giving the tree one last look."
            "The two of you walk deeper into the forest, and ignore the thump behind you."
            
    $ nex = renpy.random.randint(0, len(Act3Scenes) - 1)
    $ renpy.jump(Act3Scenes[nex])


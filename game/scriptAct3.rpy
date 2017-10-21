label Flame: 
    $ Act2Scenes.pop(nex)
    scene bgFlame
    with Fade(2.0)
    "It’s dark, so dark in the center of the forest."
    "Here the things that creep and call do so on the periphery, under cover."
    "It’s a place for nocturnal things, no matter the time. Their eyes glint and their wings flutter and the weight of them is everywhere."
    "But there is a glow, deeper, deeper."
    "It starts as a pinprick between the shadow of the trees, but the longer you walk, the more it feeds."
    "Glen is clutched to you, or you to them. It takes the two to navigate the roots and rocks, stepping slowly over every bump and break in the terrain."
    "The struggle not to stop or stumble grows more and more difficult with every inch gained, but that glow gets brighter too, warmer, worth the awkward effort."
    "So you hope."
    pause 1
    "What you reach— the thing you see— it’s hard to get the grasp of. It moves, constant, shifting its shape from each second to the next."
    "A boy, a girl, a creature, a flame. Caught in a jar. It bats at the glass, curious face tipped to watch its voyeurs back."
    "Tap, tap, tap. Shift, hiss, crackle."
    "Despite the burn, no smoke gathers to cloud the view. This thing, it’s white-hot at the center, molten, throwing off coronas of light and warmth."
    F "“Out. Out!”"
    F "It taps the glass, shifts, pools against the edge and burns."
    G "“We have to let it out, don’t we? It’s not right to leave it like this.”"
    "Glen moves to approach the jar, and the dark almost seems to deepen, the shadows trying their best to press against every inch the light will give."
    "Tendrils reach out like fingers, trees creaking and moaning, groaning, begging ‘no.’"  
    "As Glen’s hand gets closer, the creature ignites, filling its container, cackling, crackling." 
    "They hesitate." 
    F "“No! Out! Burn, forest burn. Trap me and I burn!”"
    F "It beats against the glass again and again, so near to tipping its prison or punching through, but only near."
    H "“Wait, just wait a moment!”" 
    G "Glen draws back and turns to look at you, worrying their lip between their teeth."
    "The creature growls, writhes with its impatience." 
    G "“We can’t just walk away from it! Even if we wanted to, where would we go? Back out into that black? We’d never make it out.”"
    "It felt like hours before they spotted this ember, a day— at least— to reach it."
    "What would they get just walking away? Would they ever see light again?"
    "The trapped thing wailed, pressing at every surface, every groove, desperate."
    
    menu:
        "Let it out":
            $ pacifism -= 1
            $ empathy += 1            
            $ renpy.notify("Violence +1\nEmpathy +1")
            "You can’t stand the way it looks at you, the way it aches to be set free."
            "You can’t stand the idea of being the same, stuck out there in the darkness, interminably, waiting for someone to take pity and help."
            "You reach for the jar and your hands burn and blister the second you make contact."
            "Your eyes tear up from the pain, from the reek of burning flesh, but you grit your teeth against it and set the creature free."
            "It pours out the opening, liquid and eager, instantly alighting the ground. This time, the grass hisses, the leaves, the bark."
            "Light beats the shadows back and it’s the forest’s turn to scream, to writhe, to try and escape." 
            "But the fire is so much less forgiving."
            pause 2
            "Glen reaches for you blindly to pull you close as everything goes up, the path illuminated, but cut off by falling branches."
            "It rings you both, this inferno, travelling in concentric circles, devouring everything in its path."
            "If you squint your eyes against it, brace yourself among the heat and peer deep, deep into the distance, you imagine you can see your home— the pebble path, the cold creek, the edge of the forest."
            "As you burn."
            
        "Walk away":
            $ pacifism += 1
            $ empathy -= 1            
            $ renpy.notify("Pacifism +1\nApathy +1")
            "The dark is better, it must be better."
            "This thing is just like all those other creatures, begging you to feed into the chaos, the suffering, the eternal turn of this wretched wheel."
            "But you don’t have to. Maybe you’ll spend eternity with nothing but your pride, but that’s something. Isn’t it?"
            "Knowing, in the end, you made the choice that mattered. You look to Glen, tip a smile, raise a hand."
            H "“What’s one more adventure? Just you and me.”"
            "They smile back, sad. The creature is screeching, but it’s just the two of you."
            "For the first time since you entered, this forest doesn’t hold command of your interest, your senses."
            "Glen takes your hand, tangible skin on skin. It’s real. It’s the surest thing you’ve ever known."
            G "“A trip, out into the forest. Never to return. They’ll tell stories about us, y’know? Just like your mother.”"
            G "“I think I’d like to be someone else’s fairytale.”" 
            "And so you walk. This time there’s no stress, no worry, no need to be somewhere else. Arm in arm, out into the dark, you have nothing but time."

label TwoGlens:
    $ Act2Scenes.pop(nex)
    scene bgAct3
    with Fade(2.0)
    "The forest runs deep, endless. It’s impossible to say how long you’ve been here, impossible to say how you might get out."
    "You push dark branches out of your way, then turn to hold them open for Glen behind you. But Glen isn’t there."
    H "“Glen?” You call, looking back."
    H "“Glen?” Again, louder, firmer."
    G "“Over here!” Glen’s voice comes from ahead, echoing. You wonder how they got in front of you."
    "You part the branches again, and see the scene, mirrored. Glen wrapped in vines, tied to a stump and next to them... Glen is wrapped in vines, tied to a stump."
    if HasBaby:
        "You hear a murmur beside you. The baby lies in a pile of leaves, and you pick it up in Glen’s stead."
    G "Glen on the right calls out. “Harp, it’s a trick! It’s me, I’m right here!”"
    G "The other Glen pleads. “Harp no, that’s a changeling! You have to believe me!” They struggle against their bindings."
    if HasBaby:
        "The right Glen starts to cry, and the baby joins in."
    else:
        "The right Glen starts to cry, tears falling onto the fallen leaves below them."
    if TwiceGiven:
        $ pacifism -= 2
        $ empathy -= 1            
        $ renpy.notify("Violence +2\nApathy +1")
        "Before you can act, the terrible rustling returns. The figures return from the forest."
        Cr "“Our blood is twice given, and will be thrice repaid.”"
        "With the baby in your arms, you don’t have time to draw the knife. But they are as swift as before."
        "The baby is snatched from your arms, and as the shadows part, you see that you are alone. The stumps lie empty, torn vines littering the forest floor."
        "You are alone. Now, forever more."
        return
    else: 
        menu:
            "Free crying Glen":
                $ pacifism += 1
                $ empathy += 2            
                $ renpy.notify("Pacifism +1\nEmpathy +2")
                if HasBaby:
                    "You walk slowly to the crying Glen, and shift the baby into one arm as the other hand draws the knife. You cut the vines."
                else:
                    "You walk slowly to the right Glen, and draw the knife. The vines are tight against them, but the knife severs them easily."
                G "Glen’s tears return in full force as they hug you. “Please d-don’t leave me here.”"
                G "The other Glen struggles. “No! No, let me go! I don’t belong here! Take me back! Take me home!”"
                "You turn your back on them."

            "Free struggling Glen":
                $ pacifism -= 2
                $ empathy += 1            
                $ renpy.notify("Violence +2\nEmpathy +1")
                G "As you step toward the struggling Glen, the other begins to sob. “Please. Please, Harper. Don’t do this.”"
                if HasBaby = true:
                    "You kneel by the struggling Glen, and shift the baby into one arm as the other hand draws the knife."
                    "They freeze at the sight of it, eyes wide with terror."
                else:
                    "You kneel by the struggling Glen, and draw the knife. They freeze at the sight of it, eyes wide with terror."
                "As you cut the struggling Glen’s bonds, they stare at the other, who is becoming increasingly desperate."
                G "“It wasn’t not my fault! It was them! They switched us! Harper no, I love you!”"
                H "You’ve made your choice. “Let’s go, Glen.”"
                G "“Thank you. Thank you, Harper. I promise. I promise I won’t ever leave you again.”"
                "Glen hugs you, tighter than you ever remember. They smell of the forest."

            "Leave":
                $ pacifism -= 1
                $ empathy -= 2            
                $ renpy.notify("Violence +1\nApathy +2")
                "You look to the trees, to the forest. You look at the Glens. You’re so... tired, of all this."
                G "The crying Glen’s eyes meet yours, piercing. “...I knew you would do this, someday.”"
                G "The struggling Glen stops, and looks at the other, disbelieving. “No... No, this isn’t—it isn’t right!”"
                "You turn back to the forest."
                G "“Don’t leave me here! I don’t belong here! Take me back! Take me BACK!”"
                "Soon enough, you can’t hear them anymore."



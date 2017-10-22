label Flame: 
    $ Act3Scenes.pop(nex)
    scene bgFlame
    with Fade(1.0, 1.0, 1.0)
    "It’s dark, so dark in the center of the forest."
    "Here the things that creep and call do so on the periphery, under cover."
    "It’s a place for nocturnal things, no matter the time. Their eyes glint and their wings flutter and the weight of them is everywhere."
    "But there is a glow, deeper, deeper."
    "It starts as a pinprick between the shadow of the trees, but the longer you walk, the more it feeds."
    "Glen is clutched to you, or you to them. It takes combined effort to navigate the roots and rocks, stepping slowly over every bump and break in the terrain."
    "The struggle not to stop or stumble grows more and more difficult with every inch gained, but that glow gets brighter too, warmer, worth the awkward effort."
    "So you hope."
    "..."
    "What you reach- the thing you see- it’s hard to get the grasp of. It moves, constant, shifting its shape from each second to the next."
    show flame at center
    with dissolve
    "A boy, a girl, a creature, a flame. Caught in a jar. It bats at the glass, curious face tipped to watch its voyeurs back."
    "Tap, tap, tap. Shift, hiss, crackle."
    "Despite the burn, no smoke gathers to cloud the view. This thing, white-hot at the center, molten, throwing off coronas of light and warmth..."
    F "\"Out. Out!\""
    F "It taps the glass, shifts, pools against the edge and burns."
    show flame at center:
        linear .5 right
    pause .5
    if HasBaby:
        show glenbabe at left
        with dissolve
    else:
        show glen at left
        with dissolve
    G "\"We have to let it out, don’t we? It’s not right to leave it like this.\""
    "Glen moves to approach the jar, and the dark almost seems to deepen, the shadows trying their best to press against every inch the light will give."
    "Tendrils reach out like fingers, trees creaking and moaning, groaning, begging ’no.’"  
    "As Glen’s hand gets closer, the creature ignites, filling its container, cackling, crackling." 
    "They hesitate." 
    F "\"No! Out! Burn, forest burn. Trap me and I burn!\""
    F "It beats against the glass again and again, so near to tipping its prison or punching through, but only near."
    H "\"Wait, just wait a moment!\"" 
    G "Glen draws back and turns to look at you, worrying their lip between their teeth."
    "The creature growls, writhes with its impatience." 
    G "\"We can’t just walk away from it! Even if we wanted to, where would we go? Back out into that black? We’d never make it out.\""
    "It felt like hours before they spotted this ember; a day, at least, to reach it."
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
            "If you squint your eyes against it, brace yourself among the heat and peer deep, deep into the distance, you imagine you can see your home- the pebble path, the cold creek, the edge of the forest."
            "As you burn."
            return
            
        "Walk away":
            $ pacifism += 1
            $ empathy -= 1            
            $ renpy.notify("Pacifism +1\nApathy +1")
            "The dark is better, it must be better."
            "This thing is just like all those other creatures, begging you to feed into the chaos, the suffering, the eternal turn of this wretched wheel."
            "But you don’t have to. Maybe you’ll spend eternity with nothing but your pride, but that’s something. Isn’t it?"
            "Knowing, in the end, you made the choice that mattered. You look to Glen, tip a smile, raise a hand."
            H "\"What’s one more adventure? Just you and me.\""
            "They smile back, sad. The creature is screeching, but it’s just the two of you."
            "For the first time since you entered, this forest doesn’t hold command of your interest, your senses."
            "Glen takes your hand, tangible skin on skin. It’s real. It’s the surest thing you’ve ever known."
            G "\"A trip, out into the forest. Never to return. They’ll tell stories about us, y’know? Just like your mother.\""
            G "\"I think I’d like to be someone else’s fairytale.\"" 
            "And so you walk. This time there’s no stress, no worry, no need to be somewhere else. Arm in arm, out into the dark, you have nothing but time."
            jump EndScene

label TwoGlens:
    $ Act3Scenes.pop(nex)
    scene bgAct3
    with Fade(1.0, 1.0, 1.0)
    "The forest runs deep, endless. It’s impossible to say how long you’ve been here, impossible to say how you might get out."
    "You push dark branches out of your way, then turn to hold them open for Glen behind you. But Glen isn’t there."
    H "\"Glen?\" You call, looking back."
    H "\"Glen?\" Again, louder, firmer."
    G "\"Over here!\" Glen’s voice comes from ahead, echoing. You wonder how they got in front of you."
    show glen at left
    show glenmirror at right
    with dissolve
    "You part the branches again, and see the scene, mirrored. Glen wrapped in vines, tied to a stump and next to them... Glen is wrapped in vines, tied to a stump."
    if HasBaby:
        "You hear a murmur beside you. The baby lies in a pile of leaves, and you pick it up in Glen’s stead."
    G "Glen on the right calls out. \"Harp, it’s a trick! It’s me, I’m right here!\""
    G "The other Glen pleads. \"Harp no, that’s a changeling! You have to believe me!\" They struggle against their bindings."
    if HasBaby:
        "The right Glen starts to cry, and the baby joins in."
    else:
        "The right Glen starts to cry, tears falling onto the fallen leaves below them."
    if TwiceGiven:
        $ pacifism -= 2
        $ empathy -= 1            
        $ renpy.notify("Violence +2\nApathy +1")
        "Before you can act, the terrible rustling returns. The figures return from the forest."
        Cr "\"Our blood is twice given, and will be thrice repaid.\""
        "With the baby in your arms, you don’t have time to draw the knife. But they are as swift as before."
        "The baby is snatched from your arms, and as the shadows part, you see that you are alone. The stumps lie empty, torn vines littering the forest floor."
        "You are alone. Now, forever more."
        jump Alone
    else: 
        menu:
            "Free crying Glen":
                $ pacifism += 1
                $ empathy += 1            
                $ renpy.notify("Pacifism +1\nEmpathy +1")
                if HasBaby:
                    "You walk slowly to the crying Glen, and shift the baby into one arm as the other hand draws the knife. You cut the vines."
                else:
                    "You walk slowly to the right Glen, and draw the knife. The vines are tight against them, but the knife severs them easily."
                hide glen 
                with Dissolve(1.0)
                G "Glen’s tears return in full force as they hug you. \"Please d-don’t leave me here.\""
                G "The other Glen struggles. \"No! No, let me go! I don’t belong here! Take me back! Take me home!\""
                "You turn your back on them."
                jump EndScene

            "Free struggling Glen":
                $ pacifism -= 1
                $ empathy += 1            
                $ renpy.notify("Violence +1\nEmpathy +1")
                G "As you step toward the struggling Glen, the other begins to sob. \"Please. Please, Harper. Don’t do this.\""
                if HasBaby:
                    "You kneel by the struggling Glen, and shift the baby into one arm as the other hand draws the knife."
                    "They freeze at the sight of it, eyes wide with terror."
                else:
                    "You kneel by the struggling Glen, and draw the knife. They freeze at the sight of it, eyes wide with terror."
                "As you cut the struggling Glen’s bonds, they stare at the other, who is becoming increasingly desperate."
                hide glenmirror
                with Dissolve(1.0)
                G "\"It wasn’t not my fault! It was them! They switched us! Harper no, I love you!\""
                H "You’ve made your choice. \"Let’s go, Glen.\""
                G "\"Thank you. Thank you, Harper. I promise. I promise I won’t ever leave you again.\""
                "Glen hugs you, tighter than you ever remember. They smell of the forest."
                jump EndScene

            "Leave":
                $ pacifism -= 1
                $ empathy -= 1            
                $ renpy.notify("Violence +1\nApathy +1")
                "You look to the trees, to the forest. You look at the Glens. You’re so... tired, of all this."
                G "The crying Glen’s eyes meet yours, piercing. \"...I knew you would do this, someday.\""
                G "The struggling Glen stops, and looks at the other, disbelieving. \"No... No, this isn’t-it isn’t right!\""
                "You turn back to the forest."
                G "\"Don’t leave me here! I don’t belong here! Take me back! Take me BACK!\""
                hide glen
                hide glenmirror
                with dissolve
                "Soon enough, you can’t hear them anymore."
                $ Alone = True
                if HasBaby:
                    jump AloneBaby
                else:
                    jump Alone
                return


label Wraith:
    $ Act3Scenes.pop(nex)
    scene bgAct3
    with Fade(1.0, 1.0, 1.0)
    
    "Each of the forest’s rustling hisses, distant crackles, animal cries impart the same message: you’ve gone too deep."
    "You feel suffocated within the blanket of darkness. Glen trembles at your side."
    if HasBaby:
        "The baby fusses relentlessly, a miserable bundle."
    "You come upon a clearing, of sorts. More a smattering of tree stumps than anything, but you feel the shift in the air around you."
    "Somehow, impossibly, the world feels more oppressive. Dread coils around your spine."
    "Someone is there."
    "They weren’t there before, you’re certain, but they appear at the corner of your eye."
    "You feel colder. Glen’s breath rattles in their chest."
    show woman at center
    with dissolve
    W "\"My, my. I haven’t had guests in such a long time.\""
    "A woman - no, not quite a woman, not with the subtle wrongness in her form, the sinister cast to her eyes - circles you."
    "Tendrils of thick shadow trail behind her, knitting a thick circle, a cage of icy dark that you can feel in your teeth."
    show woman at center:
        linear .5 left
    pause .5
    show harper at right
    with dissolve
    H "\"We’re just traveling through.\""
    "She clucks her tongue."
    W "\"You refuse my hospitality?\""
    G "\"We,\" Glen squeaks, \"we’re in a hurry, that’s all.\""
    W "\"You insult me,\" the woman says, the words dripping languid from her tongue."
    "The shadows coil closer."
    H "\"What do you want from us?\""
    "The woman offers a snarling smile and reaches out to brush the backs of her fingers against your cheek."
    "Her skin feels wrong - lacy like an insect, cool as a reptile."
    W "\"Merely some company.\""
    "The dark sinks in, down to your marrow." 
    "Glen shutters."
    if HasBaby:
        "The infant gives a weak, warbling cry."
        W "\"I see three of you,\" she continues. \"Surely you won’t miss just one.\""
        jump WraithChoiceBaby
    else: 
        W "\"There’s two of you,\" she continues. \"Surely one of you can stay a while.\""
        jump WraithChoice

label WraithChoiceBaby:
    "Dense and impenetrable, her shadow magic weighs on your shoulders, wraps around your throats."
    "You know there is no way to run."
    
    menu:
        "Offer Glen":
            $ empathy -= 1
            $ pacifism -= 1
            $ renpy.notify("Violence +1\nApathy +1")
            "You snatch the baby from Glen’s arms. The child squirms in your hold."
            H "\"Them. Take them.\""
            show glenmirror at center
            with Dissolve(.3)
            "You shove Glen forward, drawing a broken sound from their throat."            
            G "\"Harper! No, please!\""
            "The woman cackles in delight and her shadowy cage retreats." 
            "Before Glen can stagger away, the woman winds her arms around them."
            W "\"Don’t worry. We’ll have such fun together.\""
            "She begins to hum an eerie tune, one that teases at the back of your memory but you can’t quite place."
            "Tears stream down Glen’s cheeks as you scuttle forward."
            "You clutch the infant. You run."
            "Behind you, before you get too far, you hear Glen’s voice, carried on the wood’s anemic breeze."
            G "\"Harper, why?\""
            "..."
            "....."
            "................"
            pause 5
            "You are alone now."
            $ Alone = True
            jump AloneBaby
            
        "Offer the Baby":
            $ pacifism -= 1
            $ renpy.notify("Violence +1")
            "You snatch the baby from Glen’s arms. The child squirms and whimpers in your hold."
            H "\"Take this!\""
            show babe at center
            with Dissolve(.3)
            G "\"Harper!\" Glen gasps."
            "The woman smiles, toothy and vicious. She holds out her hands to receive the baby."
            "Glen scrambles to take it back, but you dodge their reach."
            H "\"Glen, this is the only way,\" you whisper."
            "Glen weeps."
            W "\"Don’t worry,\" the woman croons."
            W "\"I shan’t harm the child.\""
            W "\"No, no, I’ll take good care.\""
            "You ease the baby into her waiting hands and her shadowy cage retreats."
            "She begins to hum an eerie tune, one that teases at the back of your memory but you can’t quite place."
            "You grab Glen’s hand, winding your fingers together."
            H "\"We have to look out for one another, no matter what.\" You swallow."
            H "\"I’m sorry.\""
            "Glen, tearful, nods."
            "Together you run into the awaiting dark."
            $ HasBaby = False
            jump EndScene
            
        "Offer yourself":
            $ empathy += 1
            $ pacifism += 1
            $ renpy.notify("Pacifism +1\nEmpathy +1")
            "The encroaching shadow magic flows through your blood like ice, rendering your fingers and limbs and cheeks numb with cold."
            "You look at Glen, huddled and shivering in its malevolent cloud."
            "The infant clings to Glen, tiny fist grasping clothes, tiny cry growing smaller in the frigid circle."
            "You swallow and muster your courage."
            H "\"Take me.\""
            show harper at right:
                linear .5 center
            "The woman looks amused, her grin a twisted thing."
            "She slithers close to you, winds her arms around your body, kisses your nose."
            G "\"Harper, no!\" Glen sobs."
            "The shadowy cage retreats."
            H "\"It has to be this way.\" You try to sound reassuring."
            H "\"Don’t worry about me.\""
            G "\"But Harper!\""
            "The woman begins to hum an eerie tune, one that teases at the back of your memory but you can’t quite place."
            "She presses her cheek, damp and strange and ghoulish, to yours."
            H "\"Go now! You must go now, Glenny!\" you hiss."
            "Glen nods and stumbles forward, choking down their distress."
            "The writhing shadows curl around you once again, the magic sharper than before, more heady and with impossibly more weight."
            "As it creeps across your face, your eyes, you steal one last look at Glen darting away."
            "Safe. At least they will be safe."
            return
            
        "Try to kill the woman-creature":
            ## POSSIBLE EXTRA BRANCH HERE - Fail if Violence is too low?
            $ empathy += 1
            $ pacifism -= 1
            $ renpy.notify("Violence +1\nEmpathy +1")
            "Even tangled within the confines of the twisted shadow magic, you’re able to grasp your father’s trusty knife, tucked at your side."
            "You wrap your hand around it tight."
            "The woman keeps pacing circles around you and grinning that poison grin."
            W "\"Who will it be, then? Who will it be? I simply must know.\""
            G "\"Please!\" Glen begs. \"Let us pass!\""
            "You track her movements, their repetition. Calculating."
            "Glen looks at you, eyes wide and frightened and lost."
            "The baby mewls and trembles in their arms."
            W "\"Come on,\" the woman growls. \"My patience wanes.\""
            H "\"Apologies.\""
            "You strike, forcing your arm through the magic’s heavy tendrils to slash and her throat."
            "The knife makes a bare slash but it’s enough to catch the woman off guard, enough to shake the prison of shadows."
            "She yowls. You snarl and advance on her." 
            "You attack again, thrusting the knife into her neck with aim that’s half luck and half rage."
            "The woman lurches back. Her scream, a terrible inhuman void of a tone, shoots pain through and between your ears."
            "You pull out the knife, grab Glen’s hand and run as fast as you can."
            jump EndScene

label WraithChoice:
    "Dense and impenetrable, her shadow magic weighs on your shoulders, wraps around your throats."
    "You know there is no way to run."
    
    menu:
        "Offer Glen":
            $ empathy -= 1
            $ pacifism -= 1
            $ renpy.notify("Violence +1\nApathy +1")
            H "\"Them. Take them.\""
            show glenmirror at center
            with Dissolve(.3)
            "You shove Glen forward, drawing a broken sound from their throat."
            G "\"Harper! No, please!\""
            "The woman cackles in delight and her shadowy cage retreats." 
            "Before Glen can stagger away, the woman winds her arms around them."
            W "\"Don’t worry. We’ll have such fun together.\""
            "She begins to hum an eerie tune, one that teases at the back of your memory but you can’t quite place."
            "Tears stream down Glen’s cheeks as you scuttle forward."
            "You run."
            "Behind you, before you get too far, you hear Glen’s voice, carried on the wood’s anemic breeze."
            G "\"Harper, why?\""
            "..."
            "....."
            "................"
            pause 5
            "You are alone now."
            $ Alone = True
            jump Alone
            
        "Offer yourself":
            $ empathy += 1
            $ pacifism += 1
            $ renpy.notify("Pacifism +1\nEmpathy +1")
            "The encroaching shadow magic flows through your blood like ice, rendering your fingers and limbs and cheeks numb with cold."
            "You look at Glen, huddled and shivering in its malevolent cloud."
            "You swallow and muster your courage."
            H "\"Take me.\""
            show harper at right:
                linear .5 center
            "The woman looks amused, her grin a twisted thing."
            "She slithers close to you, winds her arms around your body, kisses your nose."
            G "\"Harper, no!\" Glen sobs."
            "The shadowy cage retreats."
            H "\"It has to be this way.\" You try to sound reassuring."
            H "\"Don’t worry about me.\""
            G "\"But Harper!\""
            "The woman begins to hum an eerie tune, one that teases at the back of your memory but you can’t quite place."
            "She presses her cheek, damp and strange and ghoulish, to yours."
            H "\"Go now! You must go now, Glenny!\" you hiss."
            "Glen nods and stumbles forward, choking down their distress."
            "The writhing shadows curl around you once again, the magic sharper than before, more heady and with impossibly more weight."
            "As it creeps across your face, your eyes, you steal one last look at Glen darting away."
            "Safe. At least Glen will be safe."
            return
            
        "Try to kill the woman-creature":
            ## POSSIBLE EXTRA BRANCH HERE - Fail if Violence is too low?
            $ empathy += 1
            $ pacifism -= 1
            $ renpy.notify("Violence +1\nEmpathy +1")
            "Even tangled within the confines of the twisted shadow magic, you’re able to grasp your father’s trusty knife, tucked at your side."
            "You wrap your hand around it tight."
            "The woman keeps pacing circles around you and grinning that poison grin."
            W "\"Who will it be, then? Who will it be? I simply must know.\""
            G "\"Please!\" Glen begs. \"Let us pass!\""
            "You track her movements, their repetition. Calculating."
            "Glen looks at you, eyes wide and frightened and lost."
            W "\"Come on,\" the woman growls. \"My patience wanes.\""
            H "\"Apologies.\""
            "You strike, forcing your arm through the magic’s heavy tendrils to slash and her throat."
            "The knife makes a bare slash but it’s enough to catch the woman off guard, enough to shake the prison of shadows."
            "She yowls. You snarl and advance on her." 
            "You attack again, thrusting the knife into her neck with aim that’s half luck and half rage."
            "The woman lurches back. Her scream, a terrible inhuman void of a tone, shoots pain through and between your ears."
            "You pull out the knife, grab Glen’s hand and run as fast as you can."
            jump EndScene
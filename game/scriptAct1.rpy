label Treasure:
 # These display lines of dialogue.
    $ Act1Scenes.pop(nex)
    "Another clearing opened before them. You walk toward the center, looking for another path out."
    G "“Harper, someone’s coming!” Glen whispers, pulling your sleeve. Rustling interrupts the soft silence of the forest."
    H "“Did they follow us?” you whisper back, turning to the sound."
    "A dark figure emerges from the brush, staggering. Glen gasps."
    G "“Harper, I think they’re hurt!”"
    "It’s true. It’s a man, or something that looks like one. He’s covered in dirt, and can barely walk."
    L "“H...Help me, th...they’ll find me.”"
    G "“Should we hide him?” Glen asks you, getting straight to the point."
    L "“P-Please, they’re going to kill me.” His voice becomes hushed. You see he carries a bundle, something precious."
    "More rustling interrupts your thoughts. It’s louder this time. Violent. Your eyes dart to the knife at your belt."

    menu:
        "Hide him":
            $ pacifism += 1
            $ empathy -= 1
            $ renpy.notify("Pacifism +1\nApathy +1")
            H "“Hurry.” You get closer, trying not to dirty yourselves too badly as the two of you lift his arms onto your shoulders."
            H "“In the bushes.” You ease him down into the shade of the bushes, while Glen pushes the dirt around with their boot, trying to hide the man’s footprints."
            "A crowd emerges from the brush. Their eyes fall upon you."
            C "“Where is our treasure?” they ask as one."
            H "“Not here,” you respond evenly, trying to keep your voice from shaking."
            "They spread through the clearing in an elegant wave of shapes, but do not see him."
            G "“What are you going to do if you find him?” Glen asks."
            "They level their gazes on Glen, who you shoot a glare. You hadn’t said it was a “him”."
            C "They respond nonetheless. “We will reclaim what is ours.” Without another word, they return between the branches of the forest."
            G "Glen tugs at your sleeve, frozen until now. “We have to get out of here, Harper. C’mon, please.”"
            "You look back at the shadow under the bush, as Glen drags you away. The man begins to cry, and a baby’s voice joins his."

        "Protect him":
            $ pacifism -= 1
            $ empathy += 1
            $ renpy.notify("Violence +1\nEmpathy +1")
            "You draw your knife, as Glen eases him to the ground behind you."
            "A crowd emerges from the brush. Their eyes fall upon you, and then him."
            C "“Step aside. He has stolen from us, and must be punished.”"
            G "“What has he stolen?”"
            C "“Our child.”"
            L "“She’s not yours! You stole her from me!”"
            "You don’t move. You chose to protect him. A figure lunges at you, swift and silent. But your blade connects."
            "The figure shrieks, and withdraws to its pack. They hiss with a hundred voices."
            "“Our blood is twice given, and will be thrice repaid.”"
            
        "Wait and see":
            $ pacifism -= 1
            $ empathy -= 1
            $ renpy.notify("Violence +1\nApathy +1")
            "As he collapses onto the ground before you, a crowd emerges from the brush. Their eyes fall upon him, and their movements are swift."
            "They take his treasure, and he screams like a man dying. It rings in your ears, familiar."
            "As they vanish into the shadows, you see that they did not kill him. But you see in his downward eyes that he has nothing more to live for."
            "You take Glen’s hand and head deeper into the woods."
            
    $ nex = renpy.random.randint(0, len(Act2Scenes) - 1)
    $ renpy.jump(Act2Scenes[nex])
    
    
    
    
label Merchant:
    $ Act1Scenes.pop(nex)
    "It starts as a tinkling, a clatter of glass and jangle of charms. The sound is familiar to those who trade in wares, traveling the dirt roads to larger cities with the hope of a livelihood."
    "Harper and Glen know it well, always excited for the promise of something new, something never before seen drifting into their sphere."
    "The creak of wheels and heaving, humid groan of something strange signal an approach."
    "It's—"
    "There’s—"
    "He rounds a gnarly trunk, cart almost overturning, before tipping his gaze up and coming to a stop."
    M "“Aha! Oh my. Look at the heft of you two.”"
    "His gaze is more than assessing, it scores against your skin as the beady black flit from you to Glen and back again. "
    G "Glen steps to him, immediate, bouncing as she steps to his stock."
    G "“At us? At you! What a thing, what a wonderful, whimsical thing.”"
    "The merchant grins, teeth— oh the teeth."
    M "“Come, come and look. More I have, if your eye is for such things.”"
    "He stands aside, gestures his arms across the glowing bottles, stringed baubles, powders and liquids and… meats."
    "Something shifts."
    M "“I trade in many things, many things. Find something you fancy, please.”"
    
    menu:
        "Step closer":
            "You move to be at Glen’s side, bumping shoulders as you peruse."
            
        "Stay back":
            "You step so slightly back, watching for the Merchant to track your anxious steps."
    "Glen’s eyes light up as they spot something you don’t, plunging their hands into the cart before reeling back with a yelp. Blood, bright and wet, seeps down a single finger, blackens, and breaks off."
    G "“What was that, what did you do?”"
    M "“An even trade! Your delight costs but a bit of blood. Good business, great business. Thank you!”"
    "The merchant takes a low bow and then snuffles as he straightens out, moving to retake the front of his cart and take to the road." 
    H "“Wait! Sir, you never told us the terms. This is unfair.”"
    "The merchant squints his eyes, sets his jaw, smacks his lips, once."
    M "“If you’re unhappy with your gains, perhaps you should barter better— next time.”"
    "The merchant squares himself towards you, fingers flexing, daring for a challenge."
    
    menu:
        "*Brandish your knife* If blood for blood is the deal you’re wanting, I’d like my fair share.":
            $ pacifism -= 1
            $ empathy -= 1
            $ renpy.notify("Violence +1\nApathy +1")
            "The merchant squeals, nostrils flaring, hands raising up as it shuffles back, stumbling over its own feet as you advance."
        
        "*Brandish your knife* Fair is fair, let Glen choose to make the sale.":
            $ pacifism -= 1
            $ empathy += 1
            $ renpy.notify("Violence +1\nEmpathy +1")
            M "“There are no returns. Your friend can make another deal, only this I can do.”" 
            "Glen keeps an eye on you, as you keep an eye on the merchant, but steps forward nonetheless. This time, their movements are more deliberate, measured, concise."
            "They take their time as they examine every item, hands hovering before making their move."
            "A sack, piecemeal marred with too large stitching. It jerks and struggles as its hefted. A low, lethargic wail is muffled by the confines."
            "As soon as the bag clears the cart, the merchant smiles, raspy laugh reverberating around the forest floor as he starts to fade away."
            M "“A price is paid then. Good business. Good, good business.”"
            "He’s gone. Before you can decide whether or not to make another move, he’s gone. His wares, his cart. All that’s left, a sack that Glen opens, to the cries of a child."
            $ HasBaby = True
            
        "We should go, Glen. A bit of blood is hardly worth a fight.":
            $ pacifism += 1
            $ empathy -= 1
            $ renpy.notify("Pacifism +1\nApathy +1")
            "Glen clutches their hand, though there’s no longer a wound, and steps aside to let the merchant pass, glaring as he does."
            "When he passes, that gaze is turned to you. Glen doesn’t speak again, but this time, as they move forward, they go without you. After a moment’s hesitation, you run after begging after a slower pace."
        
        "Take mine instead then, now that we know the terms.":
            $ pacifism += 1
            $ empathy += 1
            $ renpy.notify("Pacifism +1\nEmpathy +1")
            M "“There are no returns. Your friend can make another deal, only this I can do.”"
            H "“My blood for Glen’s blood then. You own it now, I assume it’s for sale. That is what I want, and what I am willing to pay.”"
            "The merchant stops, snorts, lips curling and skin rankling. It makes manic giggles, angry grunts, hands dragging as it starts to pace." 
            M "“Tricks, tricks! You’re dirty, little pilfer-things.”"
            "You draw your knife and slit your thumb as the merchant shrieks. The blood blots the wagon, while he stamps his feet."
            "Glen gasps as a single, fat drop of blood falls from the sky and splashes on their face." 
            M "“Your deal then, take it and go. Go, go, go!”"
            "You take Glen’s hand and pull them ever deeper, not daring to look behind as the merchant roars and trees shake and the path behind fades away."
        
        "Do Nothing":
            "Glen clutches their hand, though there’s no longer a wound, and steps aside to let the merchant pass, glaring as he does."
            G "“Let him go then, I’ve got little use for such a silly thing.”"
            "The merchant snorts and snuffles as he passes, cart creaking again as it threatens to tip along the gnarled path. Something inside a bag wriggles and whines."

    $ nex = renpy.random.randint(0, len(Act2Scenes) - 1)
    $ renpy.jump(Act2Scenes[nex])
    
    
    
    
label BirchBox:
    $ Act1Scenes.pop(nex)
    
    
    $ nex = renpy.random.randint(0, len(Act2Scenes) - 1)
    $ renpy.jump(Act2Scenes[nex])
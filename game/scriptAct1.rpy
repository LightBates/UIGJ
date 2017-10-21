label Treasure:
 # These display lines of dialogue.
    $ Act1Scenes.pop(nex)
    "Another clearing opened before them. You walk toward the center, looking for another path out."
    G "“Harper, someone’s coming!” Glen whispers, pulling your sleeve. Rustling interrupts the soft silence of the forest."
    H "“Did they follow us?” you whisper back, turning to the sound."
    "A dark figure emerges from the brush, staggering. Glen gasps."
    G "“Harper, I think they’re hurt!” It’s true. It’s a man, or something that looks like one. He’s covered in dirt, and can barely walk."
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
    
    
    $ nex = renpy.random.randint(0, len(Act2Scenes) - 1)
    $ renpy.jump(Act2Scenes[nex])
    
    
    
    
label BirchBox:
    $ Act1Scenes.pop(nex)
    
    
    $ nex = renpy.random.randint(0, len(Act2Scenes) - 1)
    $ renpy.jump(Act2Scenes[nex])
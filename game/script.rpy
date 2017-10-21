# The script of the game goes in this file.

# Declare Background Images
image bgAct1 = "/images/Backgrounds/act_1_bg.png"
image bgAct2 = "/images/Backgrounds/act_2_bg.png"
image bgAct3 = "/images/Backgrounds/act_2_bg.png"

# Declare Sprites
image harper = "/images/Characters/harper_sprite.png"
image glen = "/images/Characters/glen_sprite.png"
image glenbabe = "/images/Characters/glen_sprite_bab.png"
image merchant = "/images/Characters/the_merchant_sprite.png"
image babe = "/images/Characters/BABEE.png"
image box = "/images/Characters/box_sprite.png"
image lost = "/images/Characters/the_lost_sprite.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define C = Character("Cave")
define F = Character("Flame")
define H = Character("Harper")
define G = Character("Glen")
define Cr = Character("Crowd")
define L = Character("Lost")
define B = Character("Baby")
define M = Character("Merchant")
define S = Character("Stranger")



# The game starts here.

label start:
    
    $ Act1Scenes = ["Treasure", "Merchant", "BirchBox"]
    $ Act2Scenes = ["InTheTree", "Voices", "Boa"]
    $ Act3Scenes = ["Flame", "TwoGlens"]
    
    #Flags
    $ HasBaby = False
    
    # empathy++ = caring for others, empathy-- = apathy
    $ empathy = int(0)
    
    # pacifism++ = nonviolence, pacifism-- = violence
    $ pacifism = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgAct1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "You walk down a pebble path, along a narrow creek, leading down to tall, verdant trees. "
    "There’s a forest at the edge of the village, a border between the village and the outside. "
    "Glen walks beside you, at your side for all things, but especially adventure, weaving in and around your own, meandering trail."
    "You can’t remember, exactly, whose idea it first was to come along the path, but it hardly matters as you get nearer and nearer the creeping fringe."
    "You stop just outside it, turn to look at one another, just to be sure."
    show glen at center
    G "“What’re you waiting for?”"
    show glen at center:
        linear .5 left
    pause .5
    show harper at right
    H "“You know we’re not supposed to go in there, Glen. You know what they say is inside.”"
    G "“When has that ever stopped us before?”"
    
    menu:
        "We should really listen to our parents.":
            H "“We should really listen to our parents.”"
            G "“You're such a staunch, Harper.”"
            
        "Right as always, dear.":
            H "“Right as always, dear."
            
        "Aren't you worried about what's inside?":
            H "“Aren't you worried about what's inside?”"
            G "“Aren't {i}you{/i} excited?”"
            
        "*Tap your belt where father's trusted knife sits* I suppose we're safe, no matter.":
            $ pacifism -= 1
            $ renpy.notify("Violence +1")
            H "Your hand brushes against the knifes handle and you grin confidently “I suppose we're safe no matter.”"
            
    "Glen smiles at you, that smile that’s so sure the grass is always greener, and takes your hand."
    hide glen
    hide harper
    "You believe there might be something better out there, something brighter, something magic."
    "Birds chirping, water running, the creak of a cart somewhere far down along the road-"
    "It all cuts out as you step beyond and into the forest."
    $ nex = renpy.random.randint(0, len(Act1Scenes) - 1)
    $ renpy.jump(Act1Scenes[nex])
    
label TheForest:
    $ Act1Scenes.pop(nex)
    show text "THE FOREST" at truecenter
    "To Be Continued"
    return
    
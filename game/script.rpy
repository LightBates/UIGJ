# The script of the game goes in this file.

#init python:
   # import math


# Declare Background Images
image bgAct1 = "/images/Backgrounds/act_1_bg.png"
image bgAct2 = "/images/Backgrounds/act_2_bg.png"
image bgAct3 = "/images/Backgrounds/act_3_bg.png"
image bgFlame = "/images/Backgrounds/flame_bg.png"
image bgCave = "/images/Backgrounds/cave_bg.png"
image bgFaerie = "/images/Backgrounds/faerie_bg.png"

# Declare Sprites
image harper = "/images/Characters/harper_sprite.png"
image glen = "/images/Characters/glen_sprite.png"
image glenbabe = "/images/Characters/glen_sprite_bab.png"
image glenchange = "/images/Characters/glen_changeling_sprite.png"
image glenmirror = "/images/Characters/glen_sprite_mirror.png"
image merchant = "/images/Characters/the_merchant_sprite.png"
image babe = "/images/Characters/BABEE.png"
image box = "/images/Characters/box_sprite.png"
image lost = "/images/Characters/the_lost_sprite.png"
image flame = "/images/Characters/fire_sprite.png"
image crowd = "/images/Characters/crowd_sprite.png"
image crowdt = "/images/Characters/crowd_sprite_transparent.png"
image snake = "/images/Characters/kind_of_upsetting_sprite.png"
image woman = "/images/Characters/monster_lady_sprite.png"
image babevil = "/images/Characters/BABEEVIL.png"


image title = "/images/Backgrounds/title_sprite.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define B = Character("Baby")
define C = Character("Cave")
define Cr = Character("Crowd")
define F = Character("Flame")
define G = Character("Glen")
define H = Character("Harper")
define L = Character("Disheveled Traveler")
define M = Character("Merchant")
define S = Character("Stranger")
define W = Character("Woman")
define V = Character("Village Elder")


# Declare music

define bgm = "/audio/Complect_For.mp3"

# The game starts here.

label start:
    play music bgm loop
    
    $_game_menu_screen = "preferences"
    
    $ Act1Scenes = ["Treasure", "Merchant", "BirchBox"]
    $ Act2Scenes = ["InTheTree", "Voices", "Boa"]
    $ Act3Scenes = ["Flame", "TwoGlens", "Wraith"]
    
    #Flags
    $ HasBaby = False
    $ TwiceGiven = False
    $ Alone = False
    $ Crowd = True
    
    # empathy++ = caring for others, empathy-- = apathy
    $ empathy = 0
    
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
    "You stop just outside it, turning to look at one another, just to be sure."
    show glen at center
    with dissolve
    G "\"What’re you waiting for?\""
    show glen at center:
        linear .5 left
    pause .5
    show harper at right
    with dissolve
    H "\"You know we’re not supposed to go in there, Glen. You know what they say is inside.\""
    G "\"When has that ever stopped us before?\""
    
    menu:
        "\"We should really listen to our parents.\"":
            $ pacifism += 1
            $ renpy.notify("Pacifism +1")
            G "\"You’re such a staunch, Harper.\""
            
        "\"Right as always, dear.\"":
            $ empathy -= 1
            $ renpy.notify("Apathy +1")
            
        "\"Aren’t you worried?\"":
            $ empathy += 1
            $ renpy.notify("Empathy +1")
            G "\"Aren’t {i}you{/i} excited?\""
            
        "Tap your belt where father’s trusted knife sits \"I suppose we’re safe, no matter.\"":
            $ pacifism -= 1
            $ renpy.notify("Violence +1")
            "Your hand brushes against the knife’s handle and you grin confidently."
            
    "Glen smiles at you, that smile that’s so sure the grass is always greener, and takes your hand."
    hide glen
    hide harper
    with dissolve
    "You believe there might be something better out there, something brighter, something magic."
    "Birds chirping, water running, the creak of a cart somewhere far down along the road-"
    "It all cuts out as you step beyond and into the forest."
    window hide
    show title at truecenter
    with Dissolve(2.0)
    pause 3
    hide title
    with Dissolve(2.0)
    $ nex = renpy.random.randint(0, len(Act1Scenes) - 1)
    $ renpy.jump(Act1Scenes[nex])
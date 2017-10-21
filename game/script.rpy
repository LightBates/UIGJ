# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("Harper")
define G = Character("Glen")



# The game starts here.

label start:
    # empathy++ = caring for others, empathy-- = apathy
    $ empathy = 0
    
    # pacifism++ = nonviolence, pacifism-- = violence
    $ pacifism = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "There’s a forest, at the edge of the village. A pebble path along a narrow creek leads down to tall, verdant trees."
    "It’s there Harper and Glen walk, weaving in and around another."
    "Inseparable, the two, in all manners, but especially adventure."
    "They can’t remember exactly whose idea it was to head down first, but it hardly mattered as they walked nearer and nearer the creeping fringe."
    "At the edge of their known world, the border between the village and the outside, they stop to look at one another. To be sure."
    G "What’re you waiting for?"
    H "You know we’re not supposed to go in there, Glen. You know what they say is inside."
    G "When has that ever stopped us before?"
    menu:
        "We should really listen to our parents.":
            H "We should really listen to our parents."
            G "You're such a staunch, Harper."
        "Right as always, dear.":
            H "Right as always, dear."
        "Aren't you worried about what's inside?":
            H "Aren't you worried about what's inside?"
            G "Aren't {i}you{/i} excited?"
        "*Tap your belt where father's trusted knife sits* I suppose we're safe, no matter.":
            $ pacifism -= 1
            $ renpy.notify("Violence +1")
            H "I suppose we're safe no matter."
    "Glen smiles at you, that smile that’s so sure the grass is always greener, and takes your hand."
    "You believe there might be something better out there, something brighter, something magic. Birds chirping, water running, the creak of a cart somewhere far down along the road—"
    "it all cuts out as you step beyond and into— "
    jump TheForest
    
label TheForest:
    show text "THE FOREST" at truecenter
    "To Be Continued"
    return